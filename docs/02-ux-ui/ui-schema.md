# UI Schema - Splash Contract v1

This document defines the minimum contract to generate splash visuals per brand
using Figma Maker (or the repo script).

Goal: receive brand input (logo + palette) and produce **two** store-ready PNGs
per brand: `splash_iOS` and `splash_android`.

---

## Scope

Included in v1:

- Static splash (no animation)
- One centered logo
- Solid or gradient background
- Light mode only
- **Exactly two exports per brand** (App Store + Google Play listing sizes)

Out of scope in v1:

- Motion / Lottie splash
- Dark mode variants
- Localization text on splash
- Multiple densities (`mdpi`…`xxxhdpi`, `1x`/`2x`/`3x`) — not required for store listing

---

## Input Schema (per brand)

Config file location: `docs/02-ux-ui/brands/<brand_id>/brand.splash.json`

Required fields:

- `brand_id`: unique slug (example: `roby`)
- `brand_name`: display name (example: `Roby`)
- `logo_path`: path to primary logo asset (transparent PNG or SVG), relative to repo root
- `primary_color`: hex `#RRGGBB`
- `secondary_color`: hex `#RRGGBB`
- `background_mode`: `solid` or `gradient`

Optional fields:

- `accent_color`: hex `#RRGGBB`
- `background_color`: hex `#RRGGBB` (used when `background_mode = solid`)
- `logo_width_dp_android`: default `150` (logical dp on a **360×800** reference frame)
- `logo_height_dp_android`: default `50`
- `logo_size_pt_ios`: default `128` (square logo side on a **390×844** reference frame)
- `safe_area_margin`: default `24` (reserved for future safe-area rules)

Validation rules:

- Colors must be valid hex format.
- `logo_path` must exist and be transparent-background compatible.
- If `background_mode = gradient`, both `primary_color` and `secondary_color` are required.
- If `background_mode = solid` and `background_color` is omitted, fallback to `primary_color`.

---

## Output Schema (store listing)

All exports live in:

`docs/02-ux-ui/brands/<brand_id>/exports/`

| File | Pixel size | Intended use |
|------|------------|----------------|
| `splash_iOS.png` | **1290 × 2796** | App Store — iPhone 6.7" portrait screenshot slot |
| `splash_android.png` | **1080 × 1920** | Google Play — phone portrait screenshot |

Naming (exact):

- `splash_iOS.png`
- `splash_android.png`

Logo scale on those canvases is derived from the reference frames above (same visual proportions as a 360×800 / 390×844 design).

### In-app implementation (reference)

Android and iOS **in-repo** splash/lauch behavior may still use `drawable` / `LaunchScreen.storyboard` at other sizes; this contract only standardizes **what you ship to the stores** as two PNGs per marca.

---

## Acceptance Checklist

A generated splash set is accepted only if:

- Input file validates against required fields.
- Exactly two files exist: `splash_iOS.png`, `splash_android.png`.
- Pixel dimensions match the table above.
- Logo is centered; background follows `background_mode`.
- Visual contrast is acceptable (logo distinguishable from background).

---

## Example Input (`brand.splash.json`)

```json
{
  "brand_id": "roby",
  "brand_name": "Roby",
  "logo_path": "docs/02-ux-ui/sample-code/android/eloyalty-canje-android/app/src/roby/res/drawable/logo.png",
  "primary_color": "#001E61",
  "secondary_color": "#000F31",
  "background_mode": "solid",
  "background_color": "#001E61",
  "logo_width_dp_android": 150,
  "logo_height_dp_android": 50,
  "logo_size_pt_ios": 128
}
```

---

## Local generation (optional)

From repo root, with Pillow installed:

```bash
.venv/bin/python docs/02-ux-ui/brands/scripts/generate_all_splashes.py
```

---

## Notes for Next Iteration (v1.1)

- Add dark mode variant inputs (`logo_dark`, `background_dark`).
- Optional JSON overrides for `store_ios_width` / `store_android_height` if Apple/Google change requirements.
