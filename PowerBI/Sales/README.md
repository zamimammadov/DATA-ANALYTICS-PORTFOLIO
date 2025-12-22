# Sales Insights Dashboard (Power BI + MySQL)

## Goal
Build an interactive sales dashboard to track revenue and sales quantity over time, and identify the best/worst performing markets, customers, and products.

## Description
This project analyzes a transactional sales dataset stored in **MySQL** and visualizes the results in **Power BI**.  
The dataset includes sales transactions (date, customer, product, market, quantity, amount, currency) and supporting dimension tables (customers, products, markets, date).

The workflow:
- Load / restore the database from a dump file
- Validate data quality (e.g., negative or zero sales amounts)
- Connect Power BI to MySQL and model relationships (star-schema style)
- Create measures (Revenue, Sales Qty) and build an interactive dashboard with filters (Year / Month)
- Summarize performance by Market, Customer, and Product + monthly trend

## Skills
- Data validation & cleaning checks (invalid sales amounts, missing product labels, etc.)
- Data modeling (fact + dimension tables, relationships)
- DAX measures (Revenue, Sales Qty, time-based analysis)
- Dashboard design & storytelling (KPIs, trends, Top-N breakdowns)

## Technology
- **Power BI** (Dashboarding, DAX, data modeling)
- **MySQL** (data storage, basic validation queries)
- Optional: SQL dump restore via MySQL Workbench

## Results (Example: 2019 view)
From the 2019 dashboard view:
- Total **Revenue:** ~336.45M  
- Total **Sales Quantity:** ~847.65K  
- Top Market by revenue: **Delhi** (~171.75M)
- Top Customer: **Electricalsara Stores** (~138.77M)
- Revenue trend peaks around **mid-2019** and then declines towards year-end
- A “(Blank)” product appears in Top Products, which indicates a **data quality issue** (missing product mapping) that should be handled in production reporting

> Numbers can change depending on filters (Year/Month) and the dataset version.

## Dashboard Preview

<img width="1644" height="837" alt="image" src="https://github.com/user-attachments/assets/97d49b50-ab58-42aa-9de5-dce25cc2263b" />



## Repository Files
- `Sales_Project.pbix` → Power BI dashboard file
- `db_dump.sql` → MySQL database dump (tables + data)



