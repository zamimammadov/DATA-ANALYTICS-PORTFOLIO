Title

Presence Insights Dashboard (Power BI)
Tracking Presence %, WFH %, and Sick Leave (SL) % from an Excel attendance file.

Executive Summary

This project turns an Excel-based attendance tracker into an interactive Power BI dashboard that shows overall attendance performance and patterns by employee, date, and weekday.
Using Power Query for cleaning/reshaping and DAX for KPI logic, the report provides a single place to monitor Presence, Work From Home, and Sick Leave rates, spot trends over time, and quickly identify outliers (e.g., low presence or rising SL).

Business Problem

Attendance data stored in Excel (often across multiple sheets/months) is difficult to analyze consistently. Manually checking rows makes it hard to answer questions like:

What is the overall Presence % for a selected period?

Is WFH increasing over time?

Are there weekday patterns (e.g., lower presence on certain days)?

Which employees differ significantly from the team average?

The business need is a clear dashboard that standardizes KPI definitions and makes attendance insights fast and reliable.

Methodology

Data Source (Excel)

Used an Excel workbook containing attendance records (multiple sheets such as monthly tabs).

Key fields: Sheet Name / Period, Employee Code, Name, Date, Value (examples: P, WFH, SL, WO, HO, etc.).

Power Query (ETL / Data Preparation)

Imported the Excel file into Power BI.

Combined/appended sheets into one table (final “Final Data” dataset).

Cleaned columns (kept only required fields) and set correct data types (especially Date and Text).

Standardized the “Value” field so it can be used consistently in measures.

DAX Measures (KPI Logic)

Built measures to calculate:

Presence %

WFH %

SL %

Working day logic (excluding non-working statuses like WO/HO if applicable)

Report & Visuals

KPI cards for quick snapshot (Presence/WFH/SL).

Trend charts by date for Presence, WFH, and SL.

Day-of-week breakdown tables to compare weekday patterns.

Employee table and a daily status matrix to drill into details.

Skills

Power BI: report design, slicers/filters, interactive visuals

Power Query (M): importing Excel, cleaning, appending queries, data typing

DAX: measures for counts/percentages, filtering attendance codes, working-day calculations

Data analysis & storytelling: trends, outliers, operational insights

Results & Business Recommendation

Results

Delivered a “Presence Insights” dashboard that summarizes attendance into clear KPIs and trends:

Presence %, WFH %, and SL % at a glance

Trend visibility across months/days to detect changes early

Weekday comparisons to see consistent patterns

Employee-level comparison to spot outliers quickly

Business Recommendations

Use the dashboard monthly to identify:

employees/teams with low presence or high SL for follow-up/support

days of the week with consistently lower presence to plan staffing and important meetings

Standardize attendance code usage (e.g., clear definitions for WFH, SL, WO, HO) to improve reporting accuracy.

If WFH is rising, define target ranges and monitor whether it impacts productivity or staffing needs.

Next Steps

Add a dedicated Date table and time intelligence (MoM changes, rolling averages, MTD/QTD/YTD).

Add department/team/manager fields (if available) for deeper filtering and accountability.

Create an outlier flag (e.g., Presence < threshold or SL > threshold) to automate review.

Add a small data quality check inside Power Query (unexpected codes, missing names, duplicates).

If used in a team, store the Excel source in OneDrive/SharePoint and enable scheduled refresh.
