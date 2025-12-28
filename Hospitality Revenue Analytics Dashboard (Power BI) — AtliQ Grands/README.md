# AtliQ Grands Revenue Performance Dashboard (Power BI)

## Table of Contents
- [Project Background](#project-background)
- [Executive Summary](#executive-summary)
- [Insights Deep-Dive](#insights-deep-dive)
- [Recommendations](#recommendations)
- [Assumptions and Caveats](#assumptions-and-caveats)

## Project Background
AtliQ Grands is a multi-city hotel chain. The Revenue team needs a clear way to monitor performance and take action on the right levers (pricing, occupancy, category mix, booking platforms, cancellations, and guest experience).

## Executive Summary
This analysis reviews **AtliQ Grands’ performance in 2022 (Weeks W19–W32)** using a Power BI dashboard built on booking-level and room-night data. During this period, the portfolio generated **1.71bn** in revenue with **RevPAR 7.35K**, **ADR 12.70K**, **Occupancy 57.87%**, and **Realisation 70.15%**. Revenue is mainly driven by the **Luxury** segment (**61.61%, 1.05bn**) compared to **Business** (**38.39%, 0.66bn**), while weekends show stronger utilization than weekdays. A key risk is booking leakage through cancellations (**24.84% overall**) and uneven property performance, so improving platform mix (higher-realisation channels) and targeting low-rating/high-cancellation properties will help protect realized revenue and lift RevPAR.

<img width="856" height="526" alt="Screenshot 2025-12-28 231703" src="https://github.com/user-attachments/assets/c700b84d-e38b-45d6-a431-dee5ab072c30" />

## Insights Deep-Dive

### Revenue Trend and Category Mix (Business vs Luxury)
- For **2022 (W19–W32)**, AtliQ Grands generated **1.71bn** total revenue.
- Revenue is driven mainly by the **Luxury** segment: **1.05bn (61.61%)**, while **Business** contributes **0.66bn (38.39%)**.
- Across the weekly trend view, **Luxury consistently stays above Business**, meaning overall revenue movement is more sensitive to Luxury demand/pricing changes.
- There is a **sharp revenue drop in W32** for both categories, which likely indicates a **partial week / missing data** rather than a true performance crash (should be validated in the raw data).
- Implication: to lift total revenue, the highest leverage is to **protect Luxury performance** (availability, pricing, and experience), while using Business as a **stability lever** (weekday/corporate demand) to smooth volatility.
<img width="572" height="475" alt="image" src="https://github.com/user-attachments/assets/37e15671-daaa-48d5-bfd7-1f213e88dd94" />

### 2) RevPAR Drivers: Occupancy vs ADR (What actually moves RevPAR)
- The weekly trend chart shows **ADR remains relatively stable** throughout W19–W32, staying in a narrow band with only small week-to-week movement. This suggests pricing was not the main variable changing during the period.
- In contrast, **Occupancy % fluctuates noticeably** across weeks, with visible dips and recoveries. These occupancy shifts align with the ups and downs seen in **RevPAR**.
- **RevPAR closely tracks Occupancy**, meaning the main reason RevPAR rises or falls is how many room nights are actually utilized, not large changes in daily rate.
- Business implication: during this period, the highest-leverage way to improve RevPAR is to **increase utilized room nights** (demand capture + reducing booking leakage), while keeping ADR stable.
- Practical actions that fit this insight:
  - reduce booking leakage (cancellations / no-shows) to convert DBRN into DURN,
  - strengthen demand in weaker weeks (promotions, corporate/weekday push),
  - optimize channel mix toward platforms that bring reliable, realized bookings.
<img width="761" height="427" alt="image" src="https://github.com/user-attachments/assets/4f4b6008-9f63-4dfa-9fb7-fe15057e2a24" />

### Property Performance (Top/Bottom Hotels)
### Platform Performance (ADR & Realisation)
### Occupancy and Capacity Utilization (DSRN/DBRN/DURN)
### Cancellations, Realisation, and Ratings (Risk Signals)
