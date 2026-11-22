let
    Source = MySQL.Database("localhost", "sales", [ReturnSingleDatabase = true]),
    Transactions = Source{[Schema = "sales", Item = "transactions"]}[Data],
    IncludedSales = Table.SelectRows(
        Transactions, each [sales_amount] <> null and [sales_amount] <> 0 and [sales_amount] <> -1
    ),
    WithCurrencyCode = Table.AddColumn(
        IncludedSales, "currency_code",
        each if [currency] = null then null else
            Text.Upper(Text.Trim([currency], {" ", "#(cr)", "#(lf)", "#(tab)"})),
        type nullable text
    ),
    WithReportingAmount = Table.AddColumn(
        WithCurrencyCode, "norm_sales_amount",
        each if [currency_code] = "INR" then [sales_amount]
            else if [currency_code] = "USD" then [sales_amount] * 75
            else error Error.Record("Currency", "Unrecognized source currency", [currency]),
        Currency.Type
    )
in
    WithReportingAmount
