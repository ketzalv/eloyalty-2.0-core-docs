# Figma Maker — prompt individual (splash por marca)

Plantilla para generar **una sola marca** a la vez: dos PNG de listing (App Store + Google Play), según el contrato actual del repo.

---

## Antes de pegar el prompt

1. Elige la marca y su carpeta: `docs/02-ux-ui/brands/<brand_id>/`
2. Ahí deben existir:
   - `brand.splash.json` — configuración (colores, modo de fondo, tamaños de referencia del logo)
   - `assets/logo.png` — logo local (el `logo_path` del JSON apunta aquí)
3. Sustituye `<brand_id>` en el bloque siguiente (ejemplo: `roby`, `ham`, `eloyalty`).

Lista de marcas: `docs/02-ux-ui/brands/README.md`  
Checklist tras generar: `docs/02-ux-ui/qa-checklist-splash.md`

---

## Prompt (copiar y pegar en Figma Maker)

```text
Genera el splash de listing de tienda para UNA marca de la app eLoyalty.

Fuente de verdad:
- Contrato: docs/02-ux-ui/ui-schema.md
- Config de esta marca: docs/02-ux-ui/brands/<brand_id>/brand.splash.json

Pasos:
1. Abre y valida el JSON (campos requeridos, hex válidos, background_mode solid|gradient).
2. Usa el logo del campo logo_path del JSON (en el repo suele ser docs/02-ux-ui/brands/<brand_id>/assets/logo.png). Si el archivo no existe, detente y reporta error claro.
3. Crea exactamente dos frames (solo composición / export):
   - iOS listing: 1290 × 2796 px, retrato
   - Android listing: 1080 × 1920 px, retrato

Reglas visuales:
- Logo centrado en ambos frames.
- Fondo según background_mode del JSON.
- Si solid: background_color; si falta, usa primary_color.
- Si gradient: degradado vertical primary_color → secondary_color.
- Sin texto, sin iconos extra, sin animación, sin marcos decorativos.

Proporción del logo (como en ui-schema.md):
- Frame iOS: escala el logo como si estuviera en un lienzo de referencia 390 × 844 pt con logo cuadrado de lado logo_size_pt_ios (del JSON).
- Frame Android: escala como en 360 × 800 dp con caja logo_width_dp_android × logo_height_dp_android (del JSON).

Entregables — solo estos dos archivos, nada más:
- Ruta: docs/02-ux-ui/brands/<brand_id>/exports/
- Nombres exactos: splash_iOS.png y splash_android.png
- Dimensiones exactas: splash_iOS.png = 1290×2796 px; splash_android.png = 1080×1920 px

No generes variantes mdpi/hdpi/xhdpi/xxhdpi/xxxhdpi ni 1x/2x/3x.

Nombres sugeridos de frames en Figma:
- Splash/Store/iOS/<brand_id>
- Splash/Store/Android/<brand_id>

Al terminar: confirma que pasan las comprobaciones de docs/02-ux-ui/qa-checklist-splash.md para esta marca (2 archivos, medidas, contraste razonable).
```

*(Recuerda reemplazar las dos apariciones de `<brand_id>` por el slug real, p. ej. `roby`.)*

---

## Notas para el operador

- **Otra marca:** cambia solo `<brand_id>` en las rutas del prompt (misma plantilla).
- Si Figma Maker **no lee archivos del disco**, pega el contenido completo de `brand.splash.json` bajo el prompt y adjunta o referencia el logo desde `assets/logo.png` de esa carpeta.
- Generación local alternativa (mismos dos PNG):  
  `docs/02-ux-ui/brands/scripts/generate_all_splashes.py` (procesa todas las marcas; para una sola puedes ejecutarlo y tomar solo la carpeta de la marca).
