# Title
**Presence Insights Dashboard (Power BI)**  
Attendance analytics to track **Presence %**, **WFH %**, and **Sick Leave (SL) %** from an Excel source.

---

# Executive Summary
This project converts an Excel-based attendance tracker into an interactive Power BI dashboard.  
Using **Power Query** for data cleaning/combining and **DAX** for KPI calculations, the report provides a clear view of overall attendance performance and patterns by **date**, **day of week**, and **employee**. The dashboard helps stakeholders quickly monitor trends (Presence/WFH/SL) and identify outliers that may require attention.

---

# Business Problem
Attendance data stored in Excel (often split across multiple sheets/months) is difficult to analyze consistently and takes time to review manually. The main questions are:
- What is the overall **Presence %** for a selected period?
- How do **WFH %** and **SL %** change over time?
- Are there any clear **weekday patterns** (e.g., lower presence on specific days)?
- Which employees are significantly above/below the overall average?

A Power BI dashboard is needed to standardize KPIs and make these insights easy to access.

---

# Methodology
1. **Data Source (Excel)**
   - Imported an Excel workbook containing attendance records.
   - Core fields used: **Sheet Name/Period**, **Employee Code**, **Name**, **Date**, **Value** (e.g., `P`, `WFH`, `SL`, `WO`, `HO`, etc.).

2. **Data Preparation (Power Query)**
   - Combined/appended sheets into a single dataset (**Final Data**).
   - Removed unnecessary columns and ensured correct data types (especially **Date** and **Text**).
   - Standardized the attendance **Value** field for consistent reporting.

3. **Measures (DAX)**
   - Created measures to calculate:
     - **Presence %**
     - **WFH %**
     - **SL %**
     - **Total Working Days** (excluding non-working values such as `WO`/`HO`, if applicable)

4. **Dashboard (Power BI Visuals)**
   - KPI cards for Presence/WFH/SL
   - Trend charts by date for Presence, WFH, and SL
   - Day-of-week breakdown tables
   - Employee comparison table and daily status matrix

---

# Skills
- **Power BI**: dashboard building, slicers/filters, data visualization, reporting
- **Power Query (M)**: ETL, combining sheets, cleaning, transforming, data typing
- **DAX**: measures, filtering logic, KPI calculations, working day definitions
- **Analytical thinking**: trend analysis, identifying patterns/outliers

---

# Results & Business Recommendation
**Results**
- Delivered a “Presence Insights” dashboard that summarizes attendance into clear KPIs and trends:
  - Fast visibility into overall **Presence %**, **WFH %**, and **SL %**
  - Trend tracking across time to detect changes early
  - Weekday analysis to identify consistent attendance patterns
  - Employee-level comparison to quickly spot outliers

**Business Recommendation**
- Review the dashboard weekly/monthly to detect:
  - low presence or high SL cases that may need follow-up/support
  - weekday patterns that affect staffing and planning
- Standardize attendance code definitions (`P`, `WFH`, `SL`, `WO`, `HO`, etc.) to improve reporting consistency.
- If WFH trends upward, use the report to monitor impact and adjust hybrid-work policies accordingly.

---

# Next Steps
1. Add a dedicated **Date table** and time intelligence (MoM change, rolling averages, MTD/QTD/YTD).
2. Add **department/team/manager** fields (if available) for deeper slicing.
3. Create an **outlier flag** (e.g., Presence < X% or SL > Y%) for automated monitoring.
4. Add data quality checks (unexpected codes, missing values, duplicates).
5. If used operationally, move the Excel file to **OneDrive/SharePoint** and enable scheduled refresh.

---
