# UI Constraints

## Platform

- iOS (SwiftUI)
- Android (XML + Fragments)

---

## Navigation

- Tab-based navigation (MainView)
- Modal navigation (sheet / fullScreenCover)
- Stack navigation (NavigationLink)

---

## State Management

- @State
- @Binding
- @ObservedObject
- UserDefaults (persistent state)

---

## Network

- Alamofire for API calls

---

## QR / Scanner

- CodeScanner dependency
- QR-based flows are core

---

## Multi-brand Constraints

- Branding via:
  - Bundle Identifier
  - Assets (images, colors)
  - Settings.swift

→ No runtime config layer yet

Source:
Settings.swift :contentReference[oaicite:2]{index=2}

---

## Limitations Identified

1. No centralized theme system (tokens are static)
2. No feature flag system (hardcoded conditions)
3. No layout system (spacing inline)
4. No UI abstraction (views acopladas a lógica)
5. No design system formal

---

## Missing to Complete Constraints

To fully define constraints:

- Supported screen sizes / responsiveness
- Accessibility rules
- Offline behavior
- Error handling patterns (UI)
- Animation rules