-- Run against the bundled sales database in MySQL 8.0 or newer.
-- Raw inventory. The original report excludes amounts of zero and minus one.
SELECT COUNT(*) AS raw_rows, MIN(order_date) AS first_sale, MAX(order_date) AS last_sale,
       SUM(CASE WHEN sales_amount = 0 THEN 1 ELSE 0 END) AS zero_amount_rows,
       SUM(CASE WHEN sales_amount = -1 THEN 1 ELSE 0 END) AS minus_one_rows
FROM transactions;

-- Inspect raw bytes so that trailing carriage returns remain visible.
SELECT HEX(currency) AS currency_hex, COUNT(*) AS transaction_rows,
       SUM(sales_amount) AS amount_in_source_currency
FROM transactions
GROUP BY HEX(currency)
ORDER BY currency_hex;

-- The legacy model converts only the literal "USD" plus carriage return.
-- Apply the exercise's same 75 INR / USD factor to both USD spellings for comparison.
-- Keep source rows and reject totals for unexpected currency codes.
WITH report_rows AS (
    SELECT YEAR(order_date) AS sale_year, sales_qty, sales_amount, currency,
           UPPER(REGEXP_REPLACE(currency, '^[[:space:]]+|[[:space:]]+$', '')) AS currency_code
    FROM transactions
    WHERE sales_amount NOT IN (-1, 0)
),
valued AS (
    SELECT sale_year, sales_qty,
           CASE WHEN HEX(currency) = '5553440D' THEN sales_amount * 75
                ELSE sales_amount END AS saved_model_amount,
           CASE currency_code WHEN 'INR' THEN sales_amount
                              WHEN 'USD' THEN sales_amount * 75 END AS normalized_amount
    FROM report_rows
)
SELECT CASE WHEN sale_year IS NULL THEN 'All years' ELSE CAST(sale_year AS CHAR) END AS period,
       COUNT(*) AS included_rows, SUM(sales_qty) AS units,
       SUM(saved_model_amount) AS saved_model_amount,
       CASE WHEN COUNT(normalized_amount) = COUNT(*) THEN SUM(normalized_amount) END AS normalized_inr,
       COUNT(*) - COUNT(normalized_amount) AS unknown_currency_rows
FROM valued
GROUP BY sale_year WITH ROLLUP;

-- Reconcile the 2019 market ranking to the saved Power BI report.
SELECT m.markets_name, SUM(CASE WHEN HEX(t.currency) = '5553440D'
                                THEN t.sales_amount * 75 ELSE t.sales_amount END) AS saved_model_amount
FROM transactions AS t
JOIN markets AS m ON m.markets_code = t.market_code
WHERE t.order_date >= '2019-01-01' AND t.order_date < '2020-01-01'
  AND t.sales_amount NOT IN (-1, 0) AND m.zone <> ''
GROUP BY m.markets_code, m.markets_name
ORDER BY saved_model_amount DESC, m.markets_code;

-- An unmatched transaction retains its value in the fact total.
-- This counts the missing assignments separately from the ranked products.
SELECT YEAR(t.order_date) AS sale_year, COUNT(*) AS unmapped_rows,
       COUNT(DISTINCT t.product_code) AS absent_product_codes,
       SUM(CASE WHEN HEX(t.currency) = '5553440D'
                THEN t.sales_amount * 75 ELSE t.sales_amount END) AS unmapped_model_amount
FROM transactions AS t
LEFT JOIN products AS p ON p.product_code = t.product_code
WHERE t.sales_amount NOT IN (-1, 0) AND p.product_code IS NULL
GROUP BY YEAR(t.order_date)
ORDER BY sale_year;

-- Inspect the USD source records before making any deduplication decision.
SELECT product_code, customer_code, market_code, order_date, sales_qty, sales_amount,
       HEX(currency) AS currency_hex
FROM transactions
WHERE UPPER(REGEXP_REPLACE(currency, '^[[:space:]]+|[[:space:]]+$', '')) = 'USD'
ORDER BY order_date, product_code, customer_code, market_code, sales_qty, sales_amount, currency_hex;
