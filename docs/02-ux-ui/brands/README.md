# Brand splash (Figma Maker + exports)

Cada marca tiene **su propia carpeta** con configuración y entregables.

## Estructura

```text
brands/
  <brand_id>/
    brand.splash.json    # input (contrato)
    assets/
      logo.png            # logo local copiado desde sample-code
    exports/
      splash_iOS.png      # 1290 × 2796 — App Store (6.7" portrait)
      splash_android.png  # 1080 × 1920 — Google Play (teléfono portrait)
  scripts/
    generate_all_splashes.py
  README.md
  splash-batch-report.md
```

El contrato completo está en `docs/02-ux-ui/ui-schema.md`.

## Marcas

| Carpeta | `logo_path` actual | `background_color` (criterio) |
|---------|----------------------|-------------------------------|
| `eloyalty/` | `brands/eloyalty/assets/logo.png` | `#FFFFFF` (`colorBackgroundSplash` en `main`) |
| `fideligas/` | `brands/fideligas/assets/logo.png` | `#5D318F` (`colorBackgroundSplash` en flavor) |
| `ham/` | `brands/ham/assets/logo.png` | `#009FE3` (primario; sin splash override en flavor) |
| `roby/` | `brands/roby/assets/logo.png` | `#001E61` |
| `rutaelite/` | `brands/rutaelite/assets/logo.png` | `#1D1B1B` |
| `swapoints/` | `brands/swapoints/assets/logo.png` | `#0200CE` |
| `gilga/` | `brands/gilga/assets/logo.png` | `#04007E` |
| `novogas/` | `brands/novogas/assets/logo.png` | `#1D1B1B` |
| `gasher/` | `brands/gasher/assets/logo.png` | `#8D8674` |
| `cargogas/` | `brands/cargogas/assets/logo.png` | `#052183` |
| `gocoz/` | `brands/gocoz/assets/logo.png` | `#2A38FF` |
| `petrolaguna/` | `brands/petrolaguna/assets/logo.png` | `#0B5092` |

## Uso con Figma Maker

1. Abre `docs/02-ux-ui/figma-maker-splash-prompt.md`.
2. Apunta al JSON de la marca: `docs/02-ux-ui/brands/<brand_id>/brand.splash.json`.
3. Exporta solo **`splash_iOS.png`** y **`splash_android.png`** en `exports/` (tamaños del contrato).
4. Completa `docs/02-ux-ui/qa-checklist-splash.md`.

## Generación local (mismos dos PNG)

Desde la raíz del repo (requiere Pillow en `.venv`):

```bash
.venv/bin/python docs/02-ux-ui/brands/scripts/generate_all_splashes.py
```

Se actualiza `splash-batch-report.md` y se escriben los dos PNG por marca en `exports/`.

## Nota

Si una marca necesita **fondo blanco** en lugar del primario, edita `background_color` en su `brand.splash.json`.

Los logos ya fueron copiados desde `sample-code` a cada carpeta de marca para que el flujo sea autocontenido.
