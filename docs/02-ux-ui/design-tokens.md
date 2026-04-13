# Design Tokens

## Colors

Defined in Settings.swift

- primaryColor
- secondaryColor
- accentColor

- greenButtonColor
- fontColor
- cardColor
- backgroundColor
- colorToolbar
- colorBgTransparent

Source:
Settings.swift :contentReference[oaicite:0]{index=0}

---

## Typography

### System Fonts

- fontMedium10
- fontLight12
- fontLight18
- fontMedium18
- fontBold18

### Custom Fonts

- Circular Std Bold
- Circular Std Medium

Used in:
MainView, LoginView, RegisterView

---

## Spacing & Layout

No centralized spacing tokens detected.

Spacing is defined inline:
- padding()
- frame()
- fixed values (16, 20, 32, etc.)

---

## Radius

- 20 (inputs, buttons)
- 16 (badges, borders)
- 10 / 12 (cards)

---

## Shadows

- shadow(radius: 1)
- shadow(radius: 3)
- shadow(radius: 8)

---

## Gradients

Primary usage:

- LinearGradient(primaryColor → secondaryColor)

Used in:
- Backgrounds
- Buttons
- Headers

---

## Branding Strategy

Brand is injected via:

- Bundle Identifier → Settings.swift
- Colors (Assets)
- Logos (Images)

→ Multi-brand is resolved at runtime
