<div align="center">

# 🏥 Medical Sales & Clinical Profitability Analytics Suite
### *An end-to-end multi-platform data solution combining Python web applications and Power BI business intelligence.*

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Dash](https://img.shields.io/badge/Dash-Plotly-004B6B?style=for-the-badge&logo=plotly&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-Desktop-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Production_Ready-success?style=for-the-badge)

</div>

---

##  Executive Summary
This repository delivers an enterprise-grade reporting and data visualization architecture built around a global pharmaceutical dataset. By integrating a lightweight **Python Dash web application** with deep **Power BI relational data modeling**, the project tracks multi-dimensional performance vectors including unit margins, gross profits, and transactional volumes segmented by geography, demographics, and chronological ranges.

---

##  Architecture & Directory Layout

```text

├── dash.app/                 # Interactive web dashboard (Python, Dash, Plotly, OpenPyXL)
│   ├── app.py                # Main application entry point & reactive layout callbacks
│   └── requirements.txt      # Pinned dependency manifest
├── dashboard with Power BI/  # Executive BI environment (.pbix models & DAX metrics)
├── data/                     # Cleaned relational dataset repository (medical_sales.xlsx)
└── README.md                 # Technical specification and documentation
```
---

##  Part 1: Interactive Web Application (`dash.app/`)
The interactive web tier is engineered using **Dash** and **Plotly**, leveraging multi-table relational joins to drive real-time graphical outputs.

### Key Technical Features:
* **Relational Data Pipeline:** Automatically ingests, cleans, and merges normalized sheets (`Transactions`, `Products`, `Customers`) on runtime.
* **Dynamic Calculations:** Computes gross financial returns via vectorized transformations:
  * Total Sales = Units Sold * Unit Sales Price
  * Total Cost = Units Sold * Cost Of Production
  * Gross Profit = Total Sales - Total Cost
* **Reactive Filtering:** Context-aware UI binding enabling instantaneous multi-variable filtering by international market and custom time horizons.

### Local Execution Guide:
1. Navigate to the application folder:
   cd dash.app
2. Install the required environment packages:
   pip install -r requirements.txt
3. Execute the server script:
   python app.py
4. Access the local instance in your web browser at: http://127.0.0.1:8050

---

##  Part 2: Business Intelligence Suite (`dashboard with Power BI/`)
The enterprise BI segment provides exhaustive data storytelling through structured dimensional modeling.

* **Schema Design:** Implements a star-schema configuration linking transactional fact tables to dimensional attributes.
* **DAX Measures:** Custom calculations tracking year-over-year profitability growth, product performance matrices, and regional market penetration.
* **Interactive Visuals:** Cross-filtering dashboards optimized for executive decision-making.

---

##  Technology Stack & Dependencies
* **Core Language:** Python 3.x
* **Data Processing & Manipulation:** Pandas, NumPy, OpenPyXL
* **Data Visualization:** Plotly, Dash, Power BI Desktop
* **Version Control:** Git & GitHub

---

##  License & Academic Context
Developed as part of the advanced data analytics curriculum (**CMC CS-Morocco**). All analytical scripts and database structures are maintained under standard academic deployment frameworks.
