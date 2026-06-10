# 01 - Sales Performance Dashboard

**Business Value**: Identified key drivers of profit and built a forecasting model to support data-driven inventory and marketing decisions.

![Dashboard Preview](visualizations/dashboard_preview.png)

## Business Problem
The Superstore is losing visibility into sales trends and wants to optimize performance across regions and categories.

## Objectives
- Perform comprehensive EDA
- Identify trends, seasonality, and top performers
- Build sales forecast
- Create interactive dashboard for stakeholders

## Tech Stack
- Python, Pandas, NumPy
- Plotly, Seaborn
- Prophet (Forecasting)
- Streamlit (Dashboard)

## Key Insights
- Technology category drives highest profit but Office Supplies has highest volume
- East region underperforms in certain segments
- Strong seasonality in Q4

## Business Recommendations
1. Focus marketing budget on high-margin Technology sub-categories
2. Investigate causes of low performance in East region
3. Use forecast to optimize stock levels ahead of peak seasons

## How to Run
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the dashboard
streamlit run dashboard/app.py
```

## Dataset
Superstore Sales - Download from Kaggle and place in `data/` folder.