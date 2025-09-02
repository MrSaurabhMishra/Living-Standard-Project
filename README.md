# 🌍 Living Standard Data Analysis – India 🇮🇳

![Banner](https://img.shields.io/badge/Data-Analysis-blue) ![Python](https://img.shields.io/badge/Python-3.11-green) ![MySQL](https://img.shields.io/badge/MySQL-Database-orange)

---

## 📖 Project Overview

This project explores **India's economic indicators** using World Bank data.  
It focuses on:

- 📈 **Living cost (CPI)**
- 💰 **GDP**
- 👤 **GDP per capita**

We perform **data fetching, merging, visualization, and statistical analysis**, and store the results in a **MySQL database** for further use.  

---

## 🛠️ Technologies Used

- **Python** 🐍
  - `pandas` – Data manipulation
  - `numpy` – Numerical operations
  - `matplotlib` & `seaborn` – Data visualization
  - `requests` – Fetching API data
- **MySQL** 🗄️ – Database to store merged data
- **World Bank API** 🌐 – Source for economic indicators

---

## 📥 Data Sources

1. **Living Cost (CPI):** 🌟 `https://api.worldbank.org/v2/country/IN/indicator/FP.CPI.TOTL?format=json`
2. **GDP (Current US$):** 💹 `https://api.worldbank.org/v2/country/IN/indicator/NY.GDP.MKTP.CD?format=json`
3. **GDP per Capita (Current US$):** 👤 `https://api.worldbank.org/v2/country/IN/indicator/NY.GDP.PCAP.CD?format=json`

---

## ⚡ Features & Analysis

1. **Data Cleaning & Preparation** 🧹  
   - Converts dates to datetime objects 🗓️  
   - Sets `date` as the index  
   - Extracts country names 🌎  

2. **Merging Datasets** 🔗  
   - Living cost, GDP, and GDP per capita merged by date  

3. **Visualizations** 📊  
   - **Living Cost Trend**: 🏠 `living_cost_chart.png`  
   - **Living Cost vs GDP**: 💰 `merged_chart.png`  
   - **GDP per Capita Trend**: 👤 `gdp_per_capita_chart.png`  
   - **GDP vs GDP per Capita**: 💹 `gdp_vs_gdp_per_capita.png`  
   - **Living Cost vs GDP per Capita**: 🌟 `gdp_per_capita_scatter.png`  
   - **Living Cost & GDP per Capita Line Plot**: 🔄 `gdp_per_capita_line.png`  
   - **Histogram of GDP per Capita**: 📊 `gdp_per_capita_hist.png`  

4. **Statistical Analysis** 📐  
   - Correlation between:  
     - Living cost & GDP: 📈  
     - Living cost & GDP per capita: 👤  
     - GDP & GDP per capita: 💹  
   - Average & standard deviation calculations  
   - Percentage change over time 🔄

---

## 🗄️ Database Integration (MySQL)

- **Database:** `Economic_Data` 🗃️  
- **Table:** `Living_Standard`  
- **Columns:**  
  | Column | Type | Description |
  |--------|------|-------------|
  | id | INT | Auto-increment primary key 🔑 |
  | date | DATE | Date of data point 📅 |
  | country | VARCHAR(255) | Country name 🌎 |
  | living_cost | FLOAT | CPI / Living cost index 🏠 |
  | gdp | FLOAT | GDP in USD 💰 |
  | gdp_per_capita | FLOAT | GDP per capita in USD 👤 |

✅ Old data is cleared before inserting new data to maintain accuracy.  

---

## 📂 Output Files

| File | Description |
|------|-------------|
| `living_cost_data.csv` | Raw living cost data 🏠 |
| `gdp_data.csv` | Raw GDP data 💰 |
| `gdp_per_capita_data.csv` | Raw GDP per capita data 👤 |
| `merged_data.csv` | Combined dataset 🔗 |
| `living_cost_chart.png` | Line plot of living cost 🏠📈 |
| `merged_chart.png` | Scatter plot: Living cost vs GDP 💰 |
| `gdp_per_capita_chart.png` | Line plot of GDP per capita 👤 |
| `gdp_vs_gdp_per_capita.png` | Scatter plot: GDP vs GDP per capita 💹 |
| `gdp_per_capita_scatter.png` | Scatter plot: Living cost vs GDP per capita 🌟 |
| `gdp_per_capita_line.png` | Line plot comparison: Living cost & GDP per Capita 🔄 |
| `gdp_per_capita_hist.png` | Histogram of GDP per capita 📊 |

---

## ❓ Problem Statement  
The objective of this analysis is to evaluate India’s **living standards and economic growth trends** by examining the relationship between **GDP, GDP per capita, population growth, and living cost** over time (1975–2023).  

Despite consistent growth in GDP and GDP per capita, rising population and increasing living costs may influence the overall economic well-being of citizens.  

This study aims to identify:  
- 👥 How population growth impacts GDP and GDP per capita  
- 💰 The relationship between **living cost and GDP per capita**  
- ⚖️ Whether improvements in GDP per capita are sufficient to offset the rising living costs  
- 🔑 Key influencers driving changes in population and economic indicators  

The goal is to uncover patterns, correlations, and challenges that can guide **policy makers, economists, and businesses** in making informed decisions to improve **living standards and sustainable economic growth**.  

---

## 🎯 Objective  
To analyze the relationship between **GDP, GDP per capita, population, and living cost** in India (1975–2023) in order to identify **growth trends, key influencers, and their impact on living standards**.  

## 📊 Insights

- Strong correlation between **GDP** 💹 and **GDP per capita** 👤  
- Positive relationship between **living cost** 🏠 and **GDP per capita** 👤  
- Historical trends show percentage growth in GDP 💰 and CPI 🏠 over the years  

---
