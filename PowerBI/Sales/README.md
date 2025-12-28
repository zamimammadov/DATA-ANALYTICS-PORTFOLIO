# Sales Insights Dashboard (Power BI + MySQL)

Interactive sales dashboard to track **Revenue** and **Sales Quantity** over time and identify the **best / worst performing markets, customers, and products**.

---

## Overview

In this project, I analyzed a transactional sales dataset stored in **MySQL** and built an interactive **Power BI** dashboard for sales stakeholders.  
The dashboard provides:

- High-level KPIs (Revenue, Sales Qty)
- Monthly trends (time-based performance)
- Top/Bottom breakdowns by **Market**, **Customer**, and **Product**
- Filters (Year, Month) for quick slicing and decision-making

During validation, I also found a **data quality issue**: a **(Blank)** product appearing in Top Products, which highlights the importance of correct product mapping for reliable reporting.

---

## Business Context (Scenario)

**Company:** Atliq Hardwares (computer hardware business)  
**Challenge:** Struggling to increase revenue in a dynamically changing market  
**Stakeholder:** Sales Director  
**Goal:** Provide a dashboard that delivers near real-time sales insights so leaders can make faster, data-informed decisions.

**Function:** Sales  
**Domain:** Sales analytics (distribution / FMCG-style reporting)

---

## Business Problem

Sales stakeholders need a fast and reliable way to answer:

- How is **revenue** and **sales quantity** changing over time?
- Which **markets, customers, and products** drive the most revenue?
- Which segments are underperforming and need attention?
- Are there **data quality issues** that could mislead decisions (negative/zero sales, missing product mapping)?

When reporting is built on database data, invalid values or missing mappings reduce trust and can lead to wrong decisions.

---

## Tech Stack & Skills

**Tools:** Power BI, MySQL  
**Skills:**
- SQL data validation (invalid amounts, missing mappings)
- Data modeling (fact + dimension tables, star schema)
- DAX measures (Revenue, Sales Quantity, time filtering)
- Dashboard design & storytelling (KPIs, trends, Top-N views)

---

## Methodology

### 1) Database Setup
- Restored MySQL database using the provided dump: `db_dump.sql`
- Verified tables exist (fact transactions + dimensions such as customers/products/markets/date)

### 2) Data Quality Validation (SQL)
- Checked invalid sales records (negative or zero amounts)
- Checked missing product mapping that leads to **(Blank)** products in Power BI visuals

### 3) Power BI Connection & Modeling
- Connected Power BI to the MySQL database
- Built a star-schema style model:
  - **Fact:** Sales Transactions  
  - **Dimensions:** Customers, Products, Markets, Date  
- Verified relationships and filter directions

### 4) DAX Measures & Dashboard Build
Core measures:
- **Revenue**
- **Sales Quantity**

Dashboard visuals:
- KPI cards (Revenue, Sales Qty)
- Monthly trend chart
- Top Markets / Top Customers / Top Products
- Filters (Year / Month)

---

## Results (Example: 2019 dashboard view)

- **Total Revenue:** ~336.45M  
- **Total Sales Quantity:** ~847.65K  
- **Top Market by Revenue:** Delhi (~171.75M)  
- **Top Customer:** Electricalsara Stores (~138.77M)  
- **Trend Insight:** Revenue peaks around mid-2019 and declines toward year-end  
- **Data Quality Note:** A **(Blank)** product appears in Top Products → indicates missing product mapping

---

## Business Recommendations

### Data reliability (before production reporting)
- Remove/flag **negative or zero** sales amounts (depending on business rules for returns/credits)
- Resolve missing product mappings to eliminate **(Blank)** products
- Standardize reporting rules:
  - currency handling
  - returns/credits logic
  - consistent KPI definitions

### Growth actions (based on insights)
- Protect and expand high-performing markets (example: **Delhi**)
- Review weak markets/products for pricing, availability, or sales strategy improvements

---

## Dashboard Preview

<img width="1006" height="565" alt="Screenshot 2025-12-26 022705" src="https://github.com/user-attachments/assets/de14d28f-3e54-44ba-aac5-a74dd0104974" />

---

## Repository Structure

- `Sales_Project.pbix` → Power BI report  
- `db_dump.sql` → MySQL database dump  
- `assets/` → screenshots / images used in README  

---

## How to Run Locally

1) Restore database:
- Import `db_dump.sql` into MySQL (Workbench or CLI)

2) Open Power BI:
- Open `Sales_Project.pbix`

3) Connect Power BI to MySQL:
- Update server/credentials if needed
- Refresh visuals

---

## Resume Section (STAR Method)

**Situation:** A computer hardware business was struggling to scale revenue in a fast-changing market and lacked actionable sales insights.  
**Task:** Build a dashboard to track revenue trends and identify top/bottom performance across markets, customers, and products.  
**Action:** Restored and validated sales data in MySQL, built a star-schema model in Power BI, and created DAX measures + interactive visuals (KPIs, trends, Top-N, filters).  
**Result:** Delivered a dashboard that supports faster data-driven decisions and can help improve sales focus and execution (e.g., targeting best markets/customers). Potential impact can be estimated (example: **up to ~7% revenue improvement next quarter**) based on better prioritization and faster actions.

### Resume bullet (short version)
- Built a Power BI + MySQL sales insights dashboard (KPIs, trends, Top/Bottom markets/customers/products), improved decision speed, and flagged data quality issues (missing product mapping causing “Blank” products).

---

## How to Explain in an Interview (Talking Points)

- Start with the stakeholder need: “Sales leadership needed a single place to monitor revenue, sales quantity, and performance drivers.”
- Explain your workflow clearly:
  1) Restore DB → 2) Validate data quality → 3) Model (star schema) → 4) DAX measures → 5) Visual storytelling
- Mention the real-world detail (data quality):
  - “I found a (Blank) product in Top Products, which usually means missing mapping. I flagged it because it can mislead decisions.”
- If asked about the “7% impact” estimate:
  - Frame it as a realistic business assumption:
    - Better targeting of high-performing markets/customers
    - Faster reaction to declining trends
    - Reduced mistakes from dirty data
  - Emphasize it’s an estimate and explain the logic, not a guaranteed number.

---

## Next Steps

- Add a “data rules” layer (returns/credits handling, currency conversions, zero/negative amounts)
- Add more KPIs:
  - Profit/Margin (if cost data exists)
  - Average order value, revenue per customer, repeat rate
- Add time intelligence:
  - YoY / MoM growth
  - rolling 3-month revenue
- Improve refresh reliability:
  - scheduled refresh
  - incremental refresh (if dataset grows)
- Add a dedicated data quality page:
  - counts of invalid rows, missing mappings, duplicates

---





