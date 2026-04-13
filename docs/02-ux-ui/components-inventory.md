# UI Components Inventory

## Layout Components

- HeaderStationsView
- HeaderRedeemView
- HeaderMyRedeemView
- HeaderAddPointsView

## Cards / Containers

- CardInfoView

## List Items

- StationItemView
- ProductItemView
- ItemRedeemView
- ItemNotificationView

## Buttons / Actions

- ButtonStations
- ButtonAddPoints

## Feedback / Indicators

- PushBadgeView

## Scanner / Input Components

- CodeScannerView (external dependency)

## Media / Content

- AsyncImage (remote images)
- WebView (HTML rendering)

## Supporting Components (Not reusable UI but relevant)

- SelectionTableView (modal selection)
- LottieView (empty states)

---

## Notes

- Components are reused across modules (Stations, Redeem, Add Points)
- Headers are module-specific but structurally similar
- Strong reliance on card-based UI