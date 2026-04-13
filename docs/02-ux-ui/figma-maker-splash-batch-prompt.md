# Figma Maker — prompt batch (todas las marcas, 2 PNG c/u)

Copia y pega en Figma Maker.

```text
Genera los splash de **listing de tienda** para todas las marcas eLoyalty usando el contrato:

- Schema: docs/02-ux-ui/ui-schema.md
- QA: docs/02-ux-ui/qa-checklist-splash.md
- Índice: docs/02-ux-ui/brands/README.md

Para **cada** marca, lee su `brand.splash.json` y genera **solo 2 exportaciones PNG** en
`docs/02-ux-ui/brands/<brand_id>/exports/`:

- splash_iOS.png — 1290 × 2796 px (App Store, iPhone 6.7" portrait)
- splash_android.png — 1080 × 1920 px (Google Play, teléfono portrait)

Procesa en este orden (una carpeta = una marca):

1. docs/02-ux-ui/brands/eloyalty/brand.splash.json
2. docs/02-ux-ui/brands/fideligas/brand.splash.json
3. docs/02-ux-ui/brands/ham/brand.splash.json
4. docs/02-ux-ui/brands/roby/brand.splash.json
5. docs/02-ux-ui/brands/rutaelite/brand.splash.json
6. docs/02-ux-ui/brands/swapoints/brand.splash.json
7. docs/02-ux-ui/brands/gilga/brand.splash.json
8. docs/02-ux-ui/brands/novogas/brand.splash.json
9. docs/02-ux-ui/brands/gasher/brand.splash.json
10. docs/02-ux-ui/brands/cargogas/brand.splash.json
11. docs/02-ux-ui/brands/gocoz/brand.splash.json
12. docs/02-ux-ui/brands/petrolaguna/brand.splash.json

Reglas por marca:
- Logo centrado; fondo según background_mode / colores del JSON.
- Proporción del logo: misma lógica que docs/02-ux-ui/figma-maker-splash-prompt.md (referencias 390×844 y 360×800).
- Sin texto, sin animación, sin mdpi/hdpi ni 1x/2x/3x.

Al final: tabla PASS/FAIL por brand_id y lista de incidencias. Si una marca falla, continúa con las demás.
```
