# Presence Insights

An interactive Power BI report compares attendance and remote work from April through June 2022. Each published row covers one month and weekday across the workforce. The dataset has 15 rows and contains no person-level records.

[Power BI project](Presence%20Insights.pbip) · [Source totals](attendance_summary.csv)

## What the report shows

| Month | Recorded workdays | Present day equivalents | Presence rate | Remote share of presence | Sick leave rate |
|---|---:|---:|---:|---:|---:|
| April 2022 | 1,622 | 1,534 | 94.57% | 9.03% | 0.43% |
| May 2022 | 1,726 | 1,567.5 | 90.82% | 11.10% | 1.68% |
| June 2022 | 1,091 | 1,003.5 | 91.98% | 14.00% | 1.10% |
| **All three months** | **4,439** | **4,105** | **92.48%** | **11.04%** | **1.08%** |

June has the highest remote share and the fewest recorded workdays. This describes the mix of recorded attendance. The summary contains no headcount or contracted-hours data to explain the difference in coverage.

## How the measures work

- A recorded workday is one populated worker-date entry after excluding weekly offs (`WO`) and holidays (`HO`). Missing entries are excluded.
- **Presence rate** divides present day equivalents by recorded workdays. An office or remote day counts as one. A half-day of leave contributes half a present day.
- **Remote share of presence** divides remote day equivalents by present day equivalents. A half-day of remote work (`HWFH`) contributes half a remote day and one present day.
- **Sick leave rate** divides sick day equivalents by recorded workdays, counting half-day sick leave as 0.5.

The overall percentages use summed numerators and denominators. For example, the 453 remote day equivalents account for 11.04% of the 4,105 present day equivalents.

## Open the dashboard

Download this folder and keep the `.Report` and `.SemanticModel` directories next to **Presence Insights.pbip**. Open the project in a recent Power BI Desktop for Windows with PBIP/PBIR and TMDL support. Select **Home → Refresh** to load the embedded monthly summary. Use the month slicer to filter the four KPI cards, the presence trend and the weekday comparison. Selecting **2022-05** returns **1,726 recorded workdays**.

To refresh from another aggregate CSV with the same header, enter its absolute path in **Transform data → Edit parameters → SummaryCsvPath**. Leaving the parameter blank selects the embedded example.

## Rebuild the summary

The sample was aggregated from the multi-sheet attendance workbook used in the original project. For a workbook you are authorised to use, the optional converter reads dated columns from monthly sheets, validates attendance codes and exports only the month/weekday counts shown above.

```console
python -m pip install openpyxl
python summarize_attendance.py /path/to/attendance.xlsx /path/to/summary.csv
```

The source workbook and individual-level report are excluded from the current project. Use the CSV to inspect or reproduce every published KPI without Power BI.
