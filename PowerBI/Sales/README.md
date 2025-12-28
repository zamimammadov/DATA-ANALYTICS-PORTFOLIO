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

