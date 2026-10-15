
# Supply Chain & Inventory Intelligence

An end-to-end analytics project using Python, MySQL, and Power BI to explore sales performance, product categories, regional trends, and delivery operations.

## Tools Used
- Python: Pandas, Matplotlib
- MySQL: Data storage and SQL analysis
- Power BI: Interactive dashboard

## Dataset
DataCo Smart Supply Chain Dataset.

The CSV files are excluded from this repository. Obtain the dataset from its original source before running the analysis.

## Project Work
- Profiled and cleaned the dataset using Python.
- Analyzed category and product performance.
- Evaluated sales across regions and months.
- Compared recorded late-delivery rates across shipping modes.
- Built a Power BI dashboard with KPI cards, charts, and interactive filters.

## Key Findings
- Total sales: 36,784,735.01
- Distinct orders: 65,752
- Order items: 180,519
- Top sales category: Fishing
- Top sales region: Western Europe
- Highest recorded item-level late-delivery rate by shipping mode: First Class (95.32%)

Note: `Order Profit Per Order` totals are reported as a profit indicator and have not been independently validated as accounting profit. Late-delivery rates are calculated at the item level.

## Project Structure
- `python/` — Data profiling, cleaning, and EDA scripts
- `sql/` — SQL analysis queries
- `powerbi/` — Power BI dashboard
- `images/` — Dashboard screenshots
- `data/` — Local dataset files, excluded from Git

