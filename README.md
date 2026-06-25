# Project Portfolio: Spatiotemporal Analysis of Insecurity in Nigeria

## Stage 1: Problem Definition & Question Formulation

**The problem:**
Insecurity in Nigeria is complex, fluid, and varied. Criminal activities (like banditry, kidnapping, and communal clashes) shift patterns based on geography and time. Policy-makers, security agencies, and NGOs often lack unified, data-driven frameworks to allocate response resources efficiently.

**Core Research Questions**
This project aims to answer three specific operational questions:
* **The Regional Question:** Which geopolitical zones/states are currently experiencing the highest density of violent incidents?
* **The Temporal Question:** Are violent events escalating month-over-month, or do they follow seasonal trends?
* **The Severity Question:** Which categories of conflict (e.g., battles, strategic developments, violence against civilians) yield the highest casualty-to-incident ratio?

## Stage 2: Logic Design (Flowchart & Pseudocode)

Before writing code, we map out how data moves through our pipeline. [1]

**Operational Flowchart**
```text
Start Project -> Data Gathering: Request ACLED API / Local CSV -> Successful Download?
  ├── No -> [ Log Error & Terminate ]
  └── Yes -> [ Data Cleaning Pipeline ]
   
[ Data Cleaning Pipeline ]
 ├─► 1. Drop records lacking critical geographic keys (State/LGA)
 ├─► 2. Cast 'fatalities' to integer types & 'event_date' to Datetime
 ├─► 3. Group messy local names into standardized Nigerian States
 └─► 4. Calculate a derived column: 'Month_Year'
       │
       ▼
[ Aggregation & Analysis Matrix ]
 ├─► Group by State ──► Total Incidents & Fatalities
 ├─► Group by Month ──► Chronological Timeline Trends
 └─► Group by Event Type ──► Calculate Casualty-to-Incident Ratio
```

## Stage 3: Data Gathering

We will fetch real data from open-source repositories tracking Nigerian security events (such as the ACLED framework or Council on Foreign Relations data models). For seamless local execution without complex API authentication errors, we use an automated Python request script pulling a simulated production dataset.

## Stage 4: Data Cleaning Pipeline

Raw conflict data contains human entry errors, whitespace anomalies, and incorrect structural types. We clean them programmatically.

*(Note: There are other stages, but this is our focus for week 1.)*

---

## Project Structure

Here is a breakdown of what each file and folder in this repository is for:

* **`data/`**: This directory is intended to store the raw and cleaned datasets (e.g., downloaded CSVs or simulated production datasets) used for the analysis.
* **`notebooks/`**: This folder contains Jupyter notebooks used for exploratory data analysis (EDA), visualization, and interactive experimentation.
* **`src/`**: The main source code directory containing the Python scripts that power the data pipeline.
  * **`src/fetch_data.py`**: The automated Python script responsible for data gathering (fetching from APIs or simulating the production dataset).
  * **`src/clean_data.py`**: The script implementing the data cleaning pipeline to handle missing keys, type casting, standardization, and derived columns.
* **`requirements.txt`**: Lists all the Python dependencies and libraries required to execute the project's scripts and notebooks.
* **`README.md`**: This documentation file, providing an overview of the project, its operational stages, and the directory structure.
