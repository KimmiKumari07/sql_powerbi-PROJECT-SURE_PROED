# 📊 SQL & Power BI Projects

This repository contains three individual projects that demonstrate data analysis, visualization, and automation using **SQL, Python, and Power BI**:

1. **Smartphone Sales Analytics Dashboard**
2. **OTT Media Analytics Dashboard**
3. **Formflow_SQL (Google Sheets → MySQL Integration)**

---

## 📑 Table of Contents
- [Project 1: Smartphone Sales Analytics Dashboard](#project-1-smartphone-sales-analytics-dashboard)
- [Project 2: OTT Media Analytics Dashboard](#project-2-ott-media-analytics-dashboard)
- [Project 3: Formflow_SQL](#project-3-formflow_sql)
- [Tech Stack](#tech-stack)

---

## 🚀 Project 1: Smartphone Sales Analytics Dashboard
**Description:**  
A Power BI dashboard that analyzes smartphone sales data across brands, regions, and customer demographics.  
**Key Features:**  
- KPIs: Transactions, Units Sold, Revenue, Average Price  
- Sales analysis by **Brand, Country, and Demographics**  
- Visual insights for decision-making  

**Architecture:**  
`Excel Dataset → Power Query → Power BI Data Model → DAX Measures → Dashboard Visuals → Insights`

---

## 🎬 Project 2: OTT Media Analytics Dashboard
**Description:**  
A Power BI dashboard to analyze OTT media consumption, genre preferences, and viewer demographics.  
**Key Features:**  
- KPIs: Watch Time, Average Ratings, Active Users  
- Genre popularity and user behavior analysis  
- Top shows & platform performance insights  

**Architecture:**  
`OTT Dataset (Users, Shows, Genres, Platforms, Ratings, Watch Time) → Power Query → Power BI Data Model → DAX Measures → Dashboard Visuals → Insights`

---

## 🗄️ Project 3: Formflow_SQL
**Description:**  
A Python + SQL project that automates the transfer of Google Form responses from Google Sheets into a MySQL database.  
**Key Features:**  
- Fetches Google Form responses from Sheets using **gspread**  
- Inserts data into MySQL (`formflow_db.responses`)  
- Skips duplicate entries using timestamp check  
- Easily configurable with `config.py` and `credentials.json`  

**Architecture:**  
`Google Form Responses → Google Sheets → Python Script → MySQL Database → Data Analysis & Reporting`

---

## 🛠️ Tech Stack
- **Languages & Tools:** Python, SQL, Power BI  
- **Libraries:** `gspread`, `oauth2client`, `mysql-connector-python`  
- **Database:** MySQL (via XAMPP)  
- **Visualization:** Microsoft Power BI  


