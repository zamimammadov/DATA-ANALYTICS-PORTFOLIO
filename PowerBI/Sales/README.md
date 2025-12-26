# Title
**Sales Insights Dashboard (Power BI + MySQL)**  
Interactive sales dashboard to track **Revenue** and **Sales Quantity** over time and identify the best/worst performing **markets, customers, and products**.

---

# Executive Summary
In this project, I analyzed a transactional sales dataset stored in **MySQL** and built an interactive **Power BI** dashboard.  
The dashboard provides a clear view of total performance (Revenue, Sales Qty), monthly trends, and Top/Bottom breakdowns by Market, Customer, and Product using filters such as **Year** and **Month**.  
During validation, I also found a data quality issue (a `(Blank)` product appearing in Top Products), which highlights the importance of proper product mapping for reliable reporting.

---

# Business Problem
Sales stakeholders need a fast and reliable way to answer:
- How is revenue and sales quantity changing over time?
- Which markets, customers, and products drive the most revenue?
- Where are the weak-performing segments that need attention?
- Are there data quality issues that could mislead decisions (e.g., invalid amounts or missing product labels)?

When data is stored in a database and used for reporting, incorrect values (negative/zero sales) or missing mappings can directly reduce trust in the dashboard and lead to wrong decisions.

---

# Methodology
1. **Database Setup**
   - Restored the MySQL database using the provided SQL dump file: `db_dump.sql`
   - Verified tables exist (fact transactions + dimension tables like customers/products/markets/date)

2. **Data Quality Validation (SQL)**
   - Checked for invalid sales records (e.g., negative or zero amounts)
   - Looked for missing mappings that could create `(Blank)` products in Power BI visuals

3. **Power BI Connection & Modeling**
   - Connected Power BI to the MySQL database
   - Built a star-schema style model:
     - Fact: Sales Transactions
     - Dimensions: Customers, Products, Markets, Date
   - Verified relationships and filter directions

4. **DAX Measures & Dashboard Build**
   - Created core measures such as:
     - **Revenue**
     - **Sales Quantity**
   - Built dashboard visuals:
     - KPI cards (Revenue, Sales Qty)
     - Monthly trend chart
     - Top Markets / Top Customers / Top Products views
     - Filters (Year / Month)

**Repository files**
- `Sales_Project.pbix` → Power BI report
- `db_dump.sql` → MySQL database dump

---

# Skills
- SQL data validation (invalid sales amounts, missing product mapping checks)
- Data modeling (fact + dimension tables, relationships, star schema thinking)
- DAX measures (Revenue, Sales Quantity, time filtering)
- Dashboard design & storytelling (KPIs, trends, Top-N breakdowns)

---

# Results & Business Recommendation
**Results (Example: 2019 dashboard view)**
- **Total Revenue:** ~336.45M  
- **Total Sales Quantity:** ~847.65K  
- **Top Market by revenue:** Delhi (~171.75M)  
- **Top Customer:** Electricalsara Stores (~138.77M)  
- **Trend insight:** Revenue peaks around mid-2019 and declines toward year-end  
- **Data quality note:** `(Blank)` product appears in Top Products → indicates missing product mapping

**Business Recommendation**
1. Fix data quality issues before production reporting:
   - remove/flag negative or zero sales amounts
   - resolve missing product mappings to eliminate `(Blank)` products
2. Use market/customer insights to guide actions:
   - protect and expand high-performing markets (e.g., Delhi)
   - review underperforming markets/products for pricing, availability, or sales strategy changes
3. Standardize reporting rules (currency handling, returns/credits logic) so KPIs stay consistent.

---

**Preview of Dahsboard**

<img width="1006" height="565" alt="Screenshot 2025-12-26 022705" src="https://github.com/user-attachments/assets/de14d28f-3e54-44ba-aac5-a74dd0104974" />

---

# Next Steps
1. Add a clear “data rules” layer (how to treat returns, zero/negative amounts, currency conversions).
2. Create additional KPIs:
   - Profit / Margin (if cost data exists)
   - Average order value, revenue per customer, repeat rate
3. Add time intelligence (YoY / MoM growth, rolling 3-month revenue).
4. Improve reliability and refresh:
   - scheduled refresh
   - incremental refresh (if dataset grows)
5. Add a dedicated data quality page (counts of invalid rows, missing mappings, duplicates).

