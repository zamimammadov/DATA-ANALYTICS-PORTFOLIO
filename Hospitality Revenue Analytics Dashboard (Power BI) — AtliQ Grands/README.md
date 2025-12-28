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
This analysis reviews **AtliQ Grands’ performance in 2022 (Weeks W19–W31)** using a Power BI dashboard built on booking-level and room-night data. During this period, the portfolio generated **1.71bn** in revenue with **RevPAR 7.35K**, **ADR 12.70K**, **Occupancy 57.87%**, and **Realisation 70.15%**. Revenue is mainly driven by the **Luxury** segment (**61.61%, 1.05bn**) compared to **Business** (**38.39%, 0.66bn**), while weekends show stronger utilization than weekdays. A key risk is booking leakage through cancellations (**24.84% overall**) and uneven property performance, so improving platform mix (higher-realisation channels) and targeting low-rating/high-cancellation properties will help protect realized revenue and lift RevPAR.

<img width="856" height="526" alt="Screenshot 2025-12-28 231703" src="https://github.com/user-attachments/assets/c700b84d-e38b-45d6-a431-dee5ab072c30" />

## Insights Deep-Dive

### Revenue Trend and Category Mix (Business vs Luxury)
- For **2022 (W19–W32)**, AtliQ Grands generated **1.71bn** total revenue.
- Revenue is driven mainly by the **Luxury** segment: **1.05bn (61.61%)**, while **Business** contributes **0.66bn (38.39%)**.
- Across the weekly trend view, **Luxury consistently stays above Business**, meaning overall revenue movement is more sensitive to Luxury demand/pricing changes.
- Implication: to lift total revenue, the highest leverage is to **protect Luxury performance** (availability, pricing, and experience), while using Business as a **stability lever** (weekday/corporate demand) to smooth volatility.
<img width="572" height="475" alt="image" src="https://github.com/user-attachments/assets/37e15671-daaa-48d5-bfd7-1f213e88dd94" />

### RevPAR Drivers: Occupancy vs ADR (What actually moves RevPAR)
- The weekly trend chart shows **ADR remains relatively stable** throughout W19–W31, staying in a narrow band with only small week-to-week movement. This suggests pricing was not the main variable changing during the period.
- In contrast, **Occupancy % fluctuates noticeably** across weeks, with visible dips and recoveries. These occupancy shifts align with the ups and downs seen in **RevPAR**.
- **RevPAR closely tracks Occupancy**, meaning the main reason RevPAR rises or falls is how many room nights are actually utilized, not large changes in daily rate.
- Business implication: during this period, the highest-leverage way to improve RevPAR is to **increase utilized room nights** (demand capture + reducing booking leakage), while keeping ADR stable.
- Practical actions that fit this insight:
  - reduce booking leakage (cancellations / no-shows) to convert DBRN into DURN,
  - strengthen demand in weaker weeks (promotions, corporate/weekday push),
  - optimize channel mix toward platforms that bring reliable, realized bookings.
<img width="675" height="387" alt="image" src="https://github.com/user-attachments/assets/18557f22-e4de-44a9-ac12-64b568a32184" />

### Weekday vs Weekend Performance (Demand Pattern)
- Performance is meaningfully stronger on weekends:
  - **Weekend:** RevPAR **7,971** | Occupancy **63%** | ADR **12,725** | Realisation **71%**
  - **Weekday:** RevPAR **7,101** | Occupancy **56%** | ADR **12,683** | Realisation **70%**
- The uplift is primarily driven by **higher occupancy** (63% vs 56%); ADR is almost the same, meaning demand (not price) is the main difference.
- Weekend demand creates a clear opportunity for **rate protection** (avoid unnecessary discounting on peak days).
- Weekdays are the larger gap: improving weekday occupancy by strengthening Business/corporate demand can raise RevPAR while keeping ADR stable.
- Practical implication: use weekday-specific packages and partnerships to reduce the weekday utilization gap without harming overall pricing.
<img width="722" height="540" alt="image" src="https://github.com/user-attachments/assets/6f251822-0729-47b6-8f5e-216e81fc8090" />

---

### Booking Leakage: Realisation % (Luxury vs Business)
- Realisation % stays **around ~0.69–0.71** across the selected weeks, meaning only ~70% of booked room nights translate into realized stays (a consistent leakage signal).
- **Business and Luxury move differently week to week**, but neither category shows a sustained improvement trend; performance is mostly stable with short spikes/dips.
- The sharpest dips appear around **W26 (Business)** and **late weeks for Luxury**, which indicates periods of weaker booking quality (more cancellations/no-shows or higher booking drop-off).
- Because Realisation % is relatively flat, major revenue gains are more likely to come from **reducing cancellation/no-show leakage** (improving conversion from booked to utilized nights) rather than expecting Realisation to “naturally” improve over time.
- Recommended follow-up: break Realisation % by **booking_platform** and **property** to identify where leakage is concentrated and apply targeted fixes (policies, overbooking strategy, confirmation flows, and channel mix).


<img width="1004" height="500" alt="Screenshot 2025-12-29 005044" src="https://github.com/user-attachments/assets/e43d4c9b-3cb3-427d-ae6a-6eb1d22d0cc8" />

---

### Sales by Platforms & Channels (Booking Platform Performance)
- Realisation % by platform is tightly clustered around ~70%:
  - logtrip **70.59%**, journey **70.52%**, direct online **70.27%**, direct offline **70.20%**, others **70.07%**, makeyourtrip **69.99%**, tripster **69.83%**
- Since Realisation differences are small, platform strategy should be decided mainly by:
  - **volume contribution** (which platforms bring meaningful bookings),
  - **ADR differences** (pricing power),
  - and **cancellation behavior** (which platforms cause leakage).
- Even small improvements in platform mix can materially impact RevPAR because RevPAR is sensitive to occupancy and realized bookings.
- Practical implication: prioritize platforms that deliver reliable utilization and acceptable ADR, and review policies/flows for platforms associated with higher cancellations.
<img width="871" height="486" alt="image" src="https://github.com/user-attachments/assets/54de1249-af7e-42c7-9caf-fdf87c144ec5" />

---

### Property Performance (Top/Bottom Hotels)
- Top performers combine **high occupancy + premium ADR**, which produces strong RevPAR:
  - **Atliq Exotica (Mumbai): 117M** | RevPAR **10,629** | Occ **65.85%** | ADR **16,141**
  - **Atliq Palace (Mumbai): 100M** | RevPAR **10,592** | Occ **66.13%** | ADR **16,016**
- Delhi shows a clear pricing gap even at similar occupancy:
  - **Atliq Palace (Delhi): 88M** with **66.25%** occupancy but **ADR 12,480**, leading to **RevPAR 8,269**. This suggests a pricing/rate positioning opportunity (if demand allows).
- Some hotels have acceptable ADR but weaker occupancy (~53–54%), which limits RevPAR and points to demand capture issues:
  - **Atliq City (Delhi):** Occ **53.07%** | ADR **14,629** | RevPAR **7,763**
  - **Atliq Grands (Mumbai):** Occ **53.60%** | ADR **14,839** | RevPAR **7,953**
- Ratings and cancellations provide risk signals on sustainability:
  - Portfolio average rating is **3.62**, but some properties are near **~3.04–3.05**, which can hurt future demand and increase cancellations.
- Business implication: property-level actions should differ by pattern:
  - High ADR + low occupancy → demand/channel visibility issue
  - High occupancy + low ADR → pricing optimization opportunity
  - Low rating + high cancellations → operational/experience fix to protect realisation
<img width="897" height="430" alt="Screenshot 2025-12-29 002040" src="https://github.com/user-attachments/assets/7bd86dae-cfc9-47d3-bb80-ef651252d2c1" />

## Recommendations

### 1) RevPAR Growth (Occupancy-First)
- **Strengthen Weekday Demand:** Weekdays lag weekends on occupancy (**0.56 vs 0.63**) and RevPAR (**7,101 vs 7,971**). Run weekday-focused offers (corporate tie-ups, long-stay packages, midweek discounts with rate floors) to lift occupancy without damaging ADR.
- **Protect Peak-Weekend Pricing:** ADR is similar on weekdays and weekends (~12.7K), yet weekends deliver higher RevPAR due to demand. Maintain rate discipline on peak days and avoid unnecessary discounting.

### 2) Booking Leakage Reduction (Realisation, Cancellations, DBRN → DURN)
- **Reduce Cancellation Leakage:** Portfolio cancellation rate is high (**24.84%**) and Realisation hovers around **~70%**. Tighten policies where needed (cutoff windows, partial prepayment for high-risk platforms), and improve confirmation flows (reminders, easy rescheduling).
- **Convert Booked Nights into Utilized Nights:** The portfolio shows a large DBRN → DURN gap (**1,461 vs 1,025**). Focus on no-show prevention, overbooking rules (where safe), and proactive re-selling of canceled inventory.

### 3) Category Strategy (Business vs Luxury)
- **Double Down on Luxury as the Main Revenue Driver:** Luxury contributes **61.61% (1.05bn)** of revenue. Protect Luxury ADR and experience quality to preserve pricing power and reduce cancellations.
- **Use Business to Stabilize Volatility:** Business contributes **38.39% (0.66bn)** and can be leveraged to fill weekdays through corporate contracts and bundled value-adds rather than deep rate cuts.

### 4) Property Performance Improvements (Top/Bottom Hotel Actions)
- **Replicate Playbooks from Top Properties:** Top Mumbai hotels combine ~**66% occupancy** with **~15–16K ADR**, producing RevPAR above **10K**. Document their winning mix (platform share, room mix, rate strategy) and apply it to similar properties.
- **Fix Properties with Low Occupancy Despite Decent ADR:** Some hotels show solid ADR but ~**53–54% occupancy**, indicating demand capture/channel visibility issues. Prioritize platform mix changes, localized campaigns, and content improvements (photos, descriptions, offers).

### 5) Platform Optimization (Channel Mix)
- **Prioritize Reliable Platforms, Not Just High ADR:** Realisation by platform is tightly clustered (~**69.8–70.6%**), so platform decisions should be driven by booking volume and cancellation behavior. Shift share toward platforms that deliver higher utilized nights (DURN) and stable demand.
- **Platform-Level Leakage Monitoring:** Track Cancellation % and Realisation % by booking platform weekly to quickly detect which channels are generating leakage.

### 6) Guest Experience & Quality (Ratings Impact)
- **Target Low-Rated Properties for Operational Fixes:** Portfolio average rating is **3.62**, with some properties near ~**3.0**. Improve service and room readiness to reduce complaints and cancellations, protecting Realisation and future demand.
- **Link Experience to Revenue Protection:** Monitor rating drops alongside cancellation spikes; treat these as early warning signals and respond with on-ground corrective actions.

