# QA Checklist - Splash v1 (store listing)

Use this checklist after each Figma Maker run (or after `generate_all_splashes.py`).

Brand:
Date:
Reviewer:

---

## Input validation

- [ ] Brand config exists: `docs/02-ux-ui/brands/<brand_id>/brand.splash.json`.
- [ ] Config follows `docs/02-ux-ui/ui-schema.md`.
- [ ] `brand_id`, `brand_name`, `logo_path`, `primary_color`, `secondary_color`, `background_mode` are present.
- [ ] `logo_path` resolves to an existing file.
- [ ] Color values are valid hex (`#RRGGBB`).

## Exports (exactly two files)

- [ ] `docs/02-ux-ui/brands/<brand_id>/exports/splash_iOS.png` exists.
- [ ] `docs/02-ux-ui/brands/<brand_id>/exports/splash_android.png` exists.
- [ ] **No** extra density exports (`mdpi`, `hdpi`, `1x`, `2x`, `3x`, etc.) are required for this workflow.

## Pixel size

- [ ] `splash_iOS.png` is **1290 × 2796** px.
- [ ] `splash_android.png` is **1080 × 1920** px.

## Visual

- [ ] Background matches `background_mode` / colors from JSON.
- [ ] Logo is centered on both images.
- [ ] No clipping or obvious distortion.
- [ ] Acceptable contrast (logo vs background).
- [ ] No text, icons, or effects outside the contract.

## Final decision

- [ ] Approved
- [ ] Rejected (add reason below)

Notes:
