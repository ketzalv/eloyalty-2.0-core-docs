#!/usr/bin/env python3
"""Generate store-listing splash PNGs for all eLoyalty brands (2 files per brand)."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from PIL import Image, UnidentifiedImageError

HEX_RE = re.compile(r"^#[0-9A-Fa-f]{6}$")

ROOT = Path(__file__).resolve().parents[4]
BRANDS_DIR = ROOT / "docs" / "02-ux-ui" / "brands"
OUTPUT_REPORT = BRANDS_DIR / "splash-batch-report.md"

# Procesar en este orden (índice de marcas / solicitudes de lote).
BRAND_ORDER = [
    "eloyalty",
    "fideligas",
    "ham",
    "roby",
    "rutaelite",
    "swapoints",
    "gilga",
    "novogas",
    "gasher",
    "cargogas",
    "gocoz",
    "petrolaguna",
]

# App Store: iPhone 6.7" portrait (listing screenshot size).
STORE_IOS_W = 1290
STORE_IOS_H = 2796
# Google Play: common phone screenshot portrait (1080 × 1920).
STORE_ANDROID_W = 1080
STORE_ANDROID_H = 1920

# Design reference frames (used to scale logo from JSON dp/pt hints).
REF_IOS_W = 390
REF_IOS_H = 844
REF_ANDROID_W = 360
REF_ANDROID_H = 800

EXPORT_IOS_NAME = "splash_iOS.png"
EXPORT_ANDROID_NAME = "splash_android.png"

REQUIRED_FIELDS = [
    "brand_id",
    "brand_name",
    "logo_path",
    "primary_color",
    "secondary_color",
    "background_mode",
]


@dataclass
class BrandResult:
    brand_id: str
    source_file: str
    status: str = "PASS"
    missing: list[str] = field(default_factory=list)
    incidents: list[str] = field(default_factory=list)
    exported: list[str] = field(default_factory=list)


def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    value = hex_color.lstrip("#")
    return int(value[0:2], 16), int(value[2:4], 16), int(value[4:6], 16)


def fit_logo(logo: Image.Image, max_w: int, max_h: int) -> Image.Image:
    w, h = logo.size
    scale = min(max_w / w, max_h / h)
    new_w = max(1, int(round(w * scale)))
    new_h = max(1, int(round(h * scale)))
    return logo.resize((new_w, new_h), Image.Resampling.LANCZOS)


def create_background(frame_w: int, frame_h: int, spec: dict[str, Any]) -> Image.Image:
    mode = spec["background_mode"]
    primary = hex_to_rgb(spec["primary_color"])
    secondary = hex_to_rgb(spec["secondary_color"])
    if mode == "solid":
        color = hex_to_rgb(spec.get("background_color", spec["primary_color"]))
        return Image.new("RGBA", (frame_w, frame_h), (*color, 255))

    bg = Image.new("RGBA", (frame_w, frame_h), (*primary, 255))
    px = bg.load()
    denom = max(frame_h - 1, 1)
    for y in range(frame_h):
        t = y / denom
        r = int(round(primary[0] + (secondary[0] - primary[0]) * t))
        g = int(round(primary[1] + (secondary[1] - primary[1]) * t))
        b = int(round(primary[2] + (secondary[2] - primary[2]) * t))
        for x in range(frame_w):
            px[x, y] = (r, g, b, 255)
    return bg


def composite(logo: Image.Image, frame_w: int, frame_h: int, logo_w: int, logo_h: int, spec: dict[str, Any]) -> Image.Image:
    canvas = create_background(frame_w, frame_h, spec)
    fitted = fit_logo(logo, logo_w, logo_h)
    x = (frame_w - fitted.width) // 2
    y = (frame_h - fitted.height) // 2
    canvas.alpha_composite(fitted, (x, y))
    return canvas.convert("RGB")


def srgb_to_linear(c: float) -> float:
    if c <= 0.03928:
        return c / 12.92
    return ((c + 0.055) / 1.055) ** 2.4


def rel_luminance(rgb: tuple[int, int, int]) -> float:
    r, g, b = [v / 255.0 for v in rgb]
    return 0.2126 * srgb_to_linear(r) + 0.7152 * srgb_to_linear(g) + 0.0722 * srgb_to_linear(b)


def contrast_ratio(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    l1 = rel_luminance(a)
    l2 = rel_luminance(b)
    light = max(l1, l2)
    dark = min(l1, l2)
    return (light + 0.05) / (dark + 0.05)


def estimate_logo_color(logo: Image.Image) -> tuple[int, int, int] | None:
    rgba = logo.convert("RGBA")
    data = rgba.getdata()
    acc_r = acc_g = acc_b = count = 0
    for r, g, b, a in data:
        if a > 10:
            acc_r += r
            acc_g += g
            acc_b += b
            count += 1
    if count == 0:
        return None
    return (acc_r // count, acc_g // count, acc_b // count)


def validate_brand(_path: Path, payload: dict[str, Any], result: BrandResult) -> bool:
    ok = True
    for field in REQUIRED_FIELDS:
        if field not in payload:
            result.missing.append(field)
            ok = False

    for color_field in ("primary_color", "secondary_color"):
        value = payload.get(color_field)
        if value is not None and not HEX_RE.match(value):
            result.incidents.append(f"Color invalido en {color_field}: {value}")
            ok = False

    mode = payload.get("background_mode")
    if mode not in {"solid", "gradient"}:
        result.incidents.append(f"background_mode invalido: {mode}")
        ok = False
    if mode == "solid":
        bg = payload.get("background_color", payload.get("primary_color"))
        if bg is None or not HEX_RE.match(bg):
            result.missing.append("background_color (o primary_color valido para fallback)")
            ok = False
    if mode == "gradient":
        if not payload.get("primary_color") or not payload.get("secondary_color"):
            result.missing.append("primary_color y secondary_color para gradient")
            ok = False

    for size_field, default_value in (
        ("logo_width_dp_android", 150),
        ("logo_height_dp_android", 50),
        ("logo_size_pt_ios", 128),
        ("safe_area_margin", 24),
    ):
        value = payload.get(size_field, default_value)
        if not isinstance(value, (int, float)) or value <= 0:
            result.incidents.append(f"Tamano invalido en {size_field}: {value}")
            ok = False
        payload[size_field] = int(round(value))

    logo_rel = payload.get("logo_path")
    if isinstance(logo_rel, str):
        logo_abs = ROOT / logo_rel
        if not logo_abs.is_file():
            result.missing.append(f"logo_path no existe: {logo_rel}")
            ok = False
    else:
        result.missing.append("logo_path")
        ok = False

    if not ok:
        result.status = "FAIL"
    return ok


def iter_brand_json_paths_ordered() -> list[tuple[str, Path]]:
    pairs: list[tuple[str, Path]] = []
    for brand_id in BRAND_ORDER:
        cfg = BRANDS_DIR / brand_id / "brand.splash.json"
        pairs.append((brand_id, cfg))
    return pairs


def process_brand(brand_folder: str, json_path: Path) -> BrandResult:
    result = BrandResult(brand_id=brand_folder, source_file=str(json_path.relative_to(ROOT)))

    if not json_path.is_file():
        result.status = "FAIL"
        result.missing.append(f"Archivo no existe: {json_path.relative_to(ROOT)}")
        return result

    try:
        payload = json.loads(json_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        result.status = "FAIL"
        result.incidents.append(f"JSON invalido: {exc}")
        return result

    if "brand_id" in payload:
        result.brand_id = str(payload["brand_id"])

    if not validate_brand(json_path, payload, result):
        return result

    logo_abs = ROOT / payload["logo_path"]
    try:
        logo = Image.open(logo_abs).convert("RGBA")
    except (UnidentifiedImageError, OSError) as exc:
        result.status = "FAIL"
        result.incidents.append(f"No se pudo abrir logo: {exc}")
        return result

    logo_estimate = estimate_logo_color(logo)
    background_color = payload.get("background_color", payload["primary_color"])
    bg_rgb = hex_to_rgb(background_color)
    if logo_estimate is None:
        result.incidents.append("Logo sin pixeles visibles (transparente completo)")
        result.status = "FAIL"
        return result

    ratio = contrast_ratio(logo_estimate, bg_rgb)
    if ratio < 1.5:
        result.incidents.append(f"Contraste bajo estimado ({ratio:.2f}:1)")

    out_dir = BRANDS_DIR / brand_folder / "exports"
    out_dir.mkdir(parents=True, exist_ok=True)

    # Scale logo from reference design frame -> store pixel frame.
    ios_logo = int(round(payload["logo_size_pt_ios"] * STORE_IOS_W / REF_IOS_W))
    img_ios = composite(logo, STORE_IOS_W, STORE_IOS_H, ios_logo, ios_logo, payload)
    path_ios = out_dir / EXPORT_IOS_NAME
    img_ios.save(path_ios, "PNG", optimize=True)
    result.exported.append(EXPORT_IOS_NAME)

    aw = int(round(payload["logo_width_dp_android"] * STORE_ANDROID_W / REF_ANDROID_W))
    ah = int(round(payload["logo_height_dp_android"] * STORE_ANDROID_H / REF_ANDROID_H))
    img_android = composite(logo, STORE_ANDROID_W, STORE_ANDROID_H, aw, ah, payload)
    path_android = out_dir / EXPORT_ANDROID_NAME
    img_android.save(path_android, "PNG", optimize=True)
    result.exported.append(EXPORT_ANDROID_NAME)

    return result


def write_report(results: list[BrandResult]) -> None:
    passed = sum(1 for r in results if r.status == "PASS")
    failed = len(results) - passed

    lines = [
        "# Splash batch report (store listing)",
        "",
        f"- Total marcas: {len(results)}",
        f"- PASS: {passed}",
        f"- FAIL: {failed}",
        "",
        f"- Export iOS: `{EXPORT_IOS_NAME}` — {STORE_IOS_W}×{STORE_IOS_H} px (App Store 6.7\" portrait)",
        f"- Export Android: `{EXPORT_ANDROID_NAME}` — {STORE_ANDROID_W}×{STORE_ANDROID_H} px (Play phone portrait)",
        "",
        "## Resumen por marca",
        "",
        "| Marca | Estado | Config | Incidencias |",
        "|---|---|---|---|",
    ]
    for r in results:
        incidents = "; ".join(r.missing + r.incidents) if (r.missing or r.incidents) else "-"
        lines.append(f"| `{r.brand_id}` | **{r.status}** | `{r.source_file}` | {incidents} |")

    lines.extend(["", "## Entregables por marca", ""])
    for r in results:
        lines.append(f"### `{r.brand_id}` ({r.status})")
        lines.append(f"- Carpeta: `docs/02-ux-ui/brands/{r.brand_id}/exports/`")
        if r.exported:
            for item in sorted(r.exported):
                lines.append(f"  - `{item}`")
        else:
            lines.append("  - (ninguno)")
        lines.append("")

    OUTPUT_REPORT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    pairs = iter_brand_json_paths_ordered()
    results = [process_brand(folder, path) for folder, path in pairs]
    write_report(results)
    print(f"Reporte generado: {OUTPUT_REPORT}")
    for r in results:
        issues = len(r.missing) + len(r.incidents)
        print(f"{r.brand_id}: {r.status} (issues={issues}, exports={len(r.exported)})")


if __name__ == "__main__":
    main()
