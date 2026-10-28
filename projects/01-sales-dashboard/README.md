# Sales Performance Dashboard

[Back to portfolio](../../README.md) · [Black Rock Data](https://github.com/rebecca-bit-eng/BlackRockData)

A Streamlit prototype for exploring sales performance across regions and product categories.

**Status:** dashboard code and a CSV are committed. The data setup needs resolving before the app can run as documented. Forecasting, validated analytical findings and a dashboard preview are not yet available.

## Business question

How do sales trends and category profitability vary across regions, and which areas warrant further investigation?

## Available implementation

The [dashboard source](dashboard/app.py) includes:

- a regional multiselect filter;
- total sales, total profit and profit-margin metrics;
- an order-row count labelled “Orders”;
- a sales trend chart and profit-by-category bar chart.

**Tools:** Python, Pandas, Plotly and Streamlit. Prophet is imported, but the forecast tab currently contains placeholder text.

## Review the work

| File | Purpose |
|---|---|
| [dashboard/app.py](dashboard/app.py) | Dashboard implementation |
| [data/train.csv](data/train.csv) | Committed dataset; compatibility with the app must be checked |
| [requirements.txt](requirements.txt) | Python dependencies |

The EDA notebook is currently empty. No saved analysis supports category rankings, regional performance conclusions or seasonal findings yet.

## Local setup and known limitations

From the repository root:

```bash
cd projects/01-sales-dashboard
python -m pip install -r requirements.txt
```

Before launching, resolve these requirements:

1. The app reads `data/superstore.csv`, while this repository supplies `data/train.csv`. Verify the source and schema before changing the filename or loader.
2. The app requires `Order Date`, `Region`, `Sales`, `Profit` and `Category` columns. Profit calculations require a dataset containing `Profit`.
3. Confirm date parsing against the selected dataset.
4. The “Orders” metric counts rows, which may represent order lines rather than distinct orders. Empty selections and zero sales also need handling.

Once compatible data is configured:

```bash
streamlit run dashboard/app.py
```

These commands describe the intended setup; a successful end-to-end run has not been verified.

## Next deliverables

- Resolve dataset provenance and compatibility.
- Add a populated EDA notebook with validated findings and limitations.
- Correct order-count semantics and handle empty or zero-sales selections.
- Add a dashboard screenshot and implement and evaluate forecasting before claiming forecast results.

## Connection to Black Rock Data

This personal portfolio prototype explores sales reporting relevant to Black Rock Data's business intelligence services. For the company's public research workflow, see [Kenya Household Welfare & Labour Intelligence](https://github.com/rebecca-bit-eng/BlackRockData/tree/main/projects/kchs-2022).
