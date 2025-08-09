let
    Source = Csv.Document(File.Contents("marketing_campaign_effectiveness.csv"),[Delimiter=",", Columns=9, Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    PromoteHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    ChangeTypes = Table.TransformColumnTypes(PromoteHeaders,{
        {"Campaign_ID", type text},
        {"Channel", type text},
        {"Start_Date", type date},
        {"End_Date", type date},
        {"Impressions", Int64.Type},
        {"Clicks", Int64.Type},
        {"Conversions", Int64.Type},
        {"Spend_USD", type number},
        {"Revenue_USD", type number}
    }),
    // Add basic calculated columns (optional in PQ; we will do KPIs in DAX)
    AddDuration = Table.AddColumn(ChangeTypes, "Duration_Days", each Duration.Days([End_Date]-[Start_Date])+1, Int64.Type)
in
    AddDuration