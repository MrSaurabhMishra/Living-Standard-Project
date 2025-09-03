# 🌍 Living Standard Data Analysis – India 🇮🇳

![Banner](https://img.shields.io/badge/Data-Analysis-blue) ![Python](https://img.shields.io/badge/Python-3.13-green) ![MySQL](https://img.shields.io/badge/MySQL-Database-orange)

---

## 📖 Project Overview

This project analyzes **India's Living standard & economic indicators** using World Bank data.  
It focuses on:

- 📈 **Living cost (CPI)**  
- 💰 **GDP**  
- 👤 **GDP per capita**  
- 👥 **Population**  

The project performs **data fetching, cleaning, merging, visualization, statistical analysis**, and stores the results in a **MySQL database** for further use.  

---

## 🛠️ Technologies Used

- **Python** 🐍  
  - `pandas` – Data manipulation  
  - `matplotlib` & `seaborn` – Data visualization  
  - `requests` – Fetching API data  
- **MySQL** 🗄️ – Database for storing merged data  
- **World Bank API** 🌐 – Source for economic indicators  

---

## 📥 Data Sources

1. **Living Cost (CPI):** 🌟 `https://api.worldbank.org/v2/country/IN/indicator/FP.CPI.TOTL?format=json`  
2. **GDP (Current US$):** 💹 `https://api.worldbank.org/v2/country/IN/indicator/NY.GDP.MKTP.CD?format=json`  
3. **GDP per Capita (Current US$):** 👤 `https://api.worldbank.org/v2/country/IN/indicator/NY.GDP.PCAP.CD?format=json`  
4. **Population (Total):** 👥 `https://api.worldbank.org/v2/country/IN/indicator/SP.POP.TOTL?format=json`  

---

## ⚡ Features & Analysis

1. **Data Fetching & Cleaning** 🧹  
   - Converts `date` to datetime and sets it as index  
   - Extracts `country` name  
   - Sorts data by date  

2. **Merging Datasets** 🔗  
   - Living cost, GDP, GDP per capita, and population merged.

3. **Visualizations** 📊  
   - **Living Cost Trend** 🏠  
   - **Living Cost vs GDP** 💰  
   - **GDP per Capita Trend** 👤  
   - **GDP vs GDP per Capita** 💹  
   - **Living Cost vs GDP per Capita** 🌟  
   - **Living Cost & GDP per Capita Line Plot** 🔄  
   - **GDP per Capita Box Plot** 📦  
   - **GDP per Capita Histogram** 📊  
   - **Population Trend** 👥  
   - **GDP vs Population** 💹👥  
   - **GDP per Capita vs Population** 👤👥  

4. **Statistical Analysis** 📐  
   - Correlation between:  
     - Living cost & GDP: 📈  
     - Living cost & GDP per capita: 👤  
     - GDP & GDP per capita: 💹  
     - Population & GDP: 👥💰  
     - Population & GDP per capita: 👥👤  
   - Average and percentage change calculations for:  
     - GDP 💰  
     - Living Cost 🏠  
     - GDP per Capita 👤  

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
| population | BIGINT | Total population 👥 |
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
| `population_data.csv` | Raw population data 👥 |
| `living_standard.csv` | Merged dataset 🔗 |
| `living_cost_chart.png` | Line plot of living cost 🏠 |
| `living_cost_vs_gdp.png` | Scatter plot: Living cost vs GDP 💰 |
| `gdp_per_capita_chart.png` | Line plot of GDP per capita 👤 |
| `gdp_per_capita_scatter.png` | Scatter plot: Living cost vs GDP per capita 🌟 |
| `gdp_per_capita_line.png` | Line plot: Living cost & GDP per capita 🔄 |
| `gdp_per_capita_box.png` | Box plot of GDP per capita 📦 |
| `gdp_per_capita_hist.png` | Histogram of GDP per capita 📊 |
| `population_by_year.png` | Line plot of Population 👥 |
| `gdp_by_population.png` | Scatter plot: GDP vs Population 💹👥 |
| `gdp_per_capita_by_population.png` | Scatter plot: GDP per Capita vs Population 👤👥 |

---

## ❓ Problem Statement  

The goal is to analyze India’s **living standards and economic growth trends** (1975–2023) by examining relationships among **GDP, GDP per capita, population growth, and living cost**.  

Key questions:  
- 👥 How population growth impacts GDP, GDP per capita, and living standards  
- 💰 Relationship between **living cost and GDP per capita**  
- ⚖️ Whether GDP per capita growth offsets rising living costs  
- 🔑 Key influencers driving changes in population and economic indicators  

---

## 🎯 Objective  

To analyze **GDP, GDP per capita, population, and living cost** in India (1975–2023) to identify **trends, correlations, and impact on living standards**.  

---

## 📊 Insights

- Strong correlation between **GDP** 💹 and **GDP per capita** 👤  
- Positive correlation between **living cost** 🏠 and **GDP per capita** 👤  
- Population growth 👥 influences both GDP 💰 and living cost 🏠  
- Historical trends show significant growth in **GDP, CPI, GDP per capita, and population**  

---

## 🌟 Future Scope

- 🏭 **Industry Contribution Analysis:** Evaluate industry contributions to GDP growth and their effect on population, employment, and living cost.  
- 🌍 **Global Comparison:** Compare India’s economic growth, population trends, and living standards with other countries to identify best practices.  
- 📊 **Population Impact Study:** Assess demographic effects on urban planning, healthcare, education, and policy-making.  
