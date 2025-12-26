# Title
**Presence Insights Dashboard (Power BI)**  
Attendance analytics dashboard to track **Presence %, WFH %, and Leave patterns** using an Excel attendance file.

---

# Executive Summary
This project transforms an Excel attendance tracker into an interactive Power BI dashboard called **Presence Insights**.  
Using **Power Query** to combine and clean the data, and **DAX** to calculate KPIs, the dashboard helps quickly monitor:
- **Presence %** (how often employees are present)
- **WFH %** (work from home frequency)
- **SL %** (sick leave rate)

It also highlights trends over time, weekday patterns, and employee-level differences, so HR or managers can make faster and clearer decisions.

---

# Business Problem
When attendance is recorded in Excel with many different status codes (present, leave types, half-days, weekends, holidays), it becomes hard to:
- calculate consistent KPIs across months
- compare employees fairly
- spot trends (e.g., rising sick leave)
- understand weekday patterns (e.g., lower presence on Fridays)

This dashboard provides a single, standardized view of attendance performance and leave distribution.

---

# Methodology
1. **Data Source (Excel)**
   - Imported an Excel workbook containing attendance data (multiple sheets, e.g., monthly sheets).
   - Main columns used: **Employee Code**, **Name**, **Date**, **Value** (attendance status code).

2. **Data Preparation (Power Query)**
   - Appended all sheets into one clean table (**Final Data**).
   - Kept only required columns and set correct data types.
   - Ensured the attendance codes are consistent and ready for DAX calculations.

3. **KPIs & Measures (DAX)**
   - Built measures for:
     - **Presence %**
     - **WFH %**
     - **SL %**
     - **Total Working Days** (excludes `WO` and `HO`)

4. **Dashboard (Power BI Visuals)**
   - KPI cards (Presence %, WFH %, SL %)
   - Trend charts by date (Presence/WFH/SL over time)
   - Day-of-week tables (Presence/WFH/SL by weekday)
   - Employee comparison table + daily status matrix



# Skills
- **Power BI**: dashboard design, slicers, reporting, visualization
- **Power Query (M)**: data cleaning, combining sheets, transformations, data types
- **DAX**: KPI measures, filtering by codes, working-day logic
- **Data Analysis**: trend analysis, employee comparison, weekday insights

---

# Results & Business Recommendation
**Results**
- Created a dashboard that shows overall attendance performance and leave behavior:
  - Clear KPI tracking for Presence, WFH, and Sick Leave
  - Trends over time (to detect changes early)
  - Weekday patterns (to support planning)
  - Employee-level visibility (to identify outliers)

**Business Recommendation**
- Use the dashboard monthly to track leave trends and take action early (especially SL increases).
- Standardize how attendance codes are entered in Excel to keep the KPIs accurate.
- If WFH is increasing, use the trend + weekday view to adjust hybrid work planning.

---

#Preview of Dashboard
<img width="1146" height="762" alt="image" src="https://github.com/user-attachments/assets/d7e80a63-a5b4-4fda-897a-2318fc469786" />



---


# Next Steps
1. Add a **Date table** and time intelligence (Month-over-Month, rolling averages, YTD).
2. Add **department/team** fields (if available) for deeper analysis.
3. Create an **outlier rule** (e.g., low Presence % or high SL %) for automatic monitoring.
4. Add data quality checks (unknown codes, missing values, duplicates).
5. Move Excel to **OneDrive/SharePoint** and enable scheduled refresh (if needed).

---
