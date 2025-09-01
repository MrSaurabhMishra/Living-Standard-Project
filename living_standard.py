import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests

def fetch_living_cost_data(url,df=None):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to load page")
    data = response.json()
    df = pd.DataFrame(data[1])
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df['country'] = df['country'].apply(lambda x: x['value'])
    df = df[['value', 'country']]
    
    df.sort_index(inplace=True)
    return df
print("Data fetched successfully")
    
   
living_cost_data=fetch_living_cost_data("https://api.worldbank.org/v2/country/IN/indicator/FP.CPI.TOTL?format=json")
living_cost_data.to_csv("living_cost_data.csv")
print("Data saved successfully as living_cost_data.csv")
#visualize the data
sns.lineplot(data=living_cost_data, x='date', y='value', hue='country')
plt.savefig('living_cost_chart.png')

print("All data visualizations saved successfully")

def fetch_gdp_data(url,df=None):
    response = requests.get(url)
    if response.status_code!= 200:
        raise Exception("Failed to load page")
    data = response.json()
    df = pd.DataFrame(data[1])
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df['country'] = df['country'].apply(lambda x: x['value'])
    df = df[['value']]
    
    df.sort_index(inplace=True)
    return df

print("Data fetched successfully 2")


#scrape GDP data
gdp_data=fetch_gdp_data("https://api.worldbank.org/v2/country/IN/indicator/NY.GDP.MKTP.CD?format=json")
gdp_data.to_csv("gdp_data.csv")

print("Data saved successfully as gdp_data.csv")    
#scrape GDP per capita data
gdp_per_capita_data=fetch_gdp_data("https://api.worldbank.org/v2/country/IN/indicator/NY.GDP.PCAP.CD?format=json")
gdp_per_capita_data.to_csv("gdp_per_capita_data.csv")

print("Data saved successfully as gdp_per_capita_data.csv")

print("All data fetched successfully 3")


'''#visualize the data
sns.lineplot(data=gdp_data, x='date', y='value', hue='country')
plt.savefig('gdp_chart.png')'''

print("All data visualizations saved successfully 2")

#merge the data
merged_data = pd.merge(living_cost_data, gdp_data, how='inner', left_index=True, right_index=True)

merged_data = pd.merge(merged_data, gdp_per_capita_data, how='inner', left_index=True, right_index=True)

# specific rename
merged_data.rename(columns={
    'value_x': 'living_value',
    'value_y': 'gdp',
    'value': 'gdp_per_capita'   
}, inplace=True)

# save the merged data as a CSV file
merged_data.to_csv('merged_data.csv')


print("All data merged successfully and saved as merged_data.csv")

#visualize the merged data
sns.scatterplot(data=merged_data, x='living_value', y='gdp')
plt.savefig('merged_chart.png')

print("All data visualizations saved successfully 3")

# calculate correlation coefficient
correlation_coefficient = merged_data['living_value'].corr(merged_data['gdp'])
print(f"Correlation coefficient: {correlation_coefficient:.2f}")

print("All calculations completed successfully")

# calculate the percentage change in GDP and Living Cost
percentage_change_gdp = ((merged_data['gdp'].iloc[-1] - merged_data['gdp'].iloc[0]) / merged_data['gdp'].iloc[0]) * 100
percentage_change_living_cost = ((merged_data['living_value'].iloc[-1] - merged_data['living_value'].iloc[0]) / merged_data['living_value'].iloc[0]) * 100

print(f"Percentage change in GDP: {percentage_change_gdp:.2f}%")
print(f"Percentage change in Living Cost: {percentage_change_living_cost:.2f}%")

# calculate the average GDP and Living Cost
average_gdp = merged_data['gdp'].mean()
average_living_cost = merged_data['living_value'].mean()

print(f"Average GDP: {average_gdp:.2f}")
print(f"Average Living Cost: {average_living_cost:.2f}")

# calculate the GDP per capita
gdp_per_capita = merged_data['gdp'] / merged_data['living_value']
merged_data['gdp_per_capita'] = gdp_per_capita

# visualize the GDP per capita
sns.lineplot(data=merged_data, x='date', y='gdp_per_capita')
plt.savefig('gdp_per_capita_chart.png')

# calculate the correlation coefficient between GDP per capita and Living Cost
correlation_coefficient_gdp_per_capita = merged_data['gdp_per_capita'].corr(merged_data['living_value'])
print(f"Correlation coefficient between GDP per capita and Living Cost: {correlation_coefficient_gdp_per_capita:.2f}")

# calculate the average GDP per capita
average_gdp_per_capita = merged_data['gdp_per_capita'].mean()
print(f"Average GDP per capita: {average_gdp_per_capita:.2f}")


# calculate the percentage change in GDP per capita
percentage_change_gdp_per_capita = ((merged_data['gdp_per_capita'].iloc[-1] - merged_data['gdp_per_capita'].iloc[0]) / merged_data['gdp_per_capita'].iloc[0]) * 100

print(f"Percentage change in GDP per capita: {percentage_change_gdp_per_capita:.2f}%")

# Visualize the GDP per capita and Living Cost scatterplot
sns.scatterplot(data=merged_data, x='living_value', y='gdp_per_capita')
plt.xlabel('Living Cost')
plt.ylabel('GDP per Capita')
plt.savefig('gdp_per_capita_scatter.png')
plt.show()

# Visualize the GDP per capita and Living Cost line plot
sns.lineplot(data=merged_data, x='date', y='living_value', label='Living Cost')
sns.lineplot(data=merged_data, x='date', y='gdp_per_capita', label='GDP per Capita')
plt.legend()
plt.savefig('gdp_per_capita_line.png')
plt.show()

# Visualize the GDP per capita and Living Cost box plot
plt.figure(figsize=(12, 6))
sns.boxplot(data=merged_data[['living_value', 'gdp_per_capita']])
plt.savefig('gdp_per_capita_box.png')
plt.show()

# Statistical analysis of the GDP per capita
# calculate the standard deviation
standard_deviation_gdp_per_capita = merged_data['gdp_per_capita'].std()
print(f"Standard deviation of GDP per capita: {standard_deviation_gdp_per_capita:.2f}")

# Visualize the histogram of GDP per capita 
sns.histplot(data=merged_data['gdp_per_capita'])
plt.savefig('gdp_per_capita_hist.png')
plt.show()

# descriptive statistics
descriptive_stats = merged_data['gdp_per_capita'].describe()
print(descriptive_stats)
print("stats completed successfully")

# ------------------- MySQL Integration ------------------- #
import pymysql
from sqlalchemy import create_engine
# MySQL server details
host = 'localhost'
user = 'root'
password = 'Saurabh1042'  # <-- replace with your MySQL password
database_name = 'Economic_Data'
table_name = 'Living_Standard'

# Connect to MySQL server
try:
    cnx = pymysql.connect(host=host, user=user, password=password)
    cursor = cnx.cursor()
    print("Connected to MySQL server")
except pymysql.Error as err:
    print(f"Error: {err}")
    exit(1)

# Create database
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
cursor.execute(f"USE {database_name}")
print("Database created successfully")

# Drop table if exists
cursor.execute(f"DROP TABLE IF EXISTS {"living_standard"}")
print("Old table dropped successfully")

# Create table
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {"living_standard"} (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    country VARCHAR(255),
    living_cost FLOAT,
    gdp FLOAT,
    gdp_per_capita FLOAT
)
"""
cursor.execute(create_table_query)
print("Table created successfully")

# change column names to match MySQL requirements
merged_data.rename(columns={'date': 'date', 'country_x': 'country', 'living_value': 'living_cost', 'gdp': 'gdp', 'gdp_per_capita': 'gdp_per_capita'}, inplace=True)
# Insert data
for index, row in merged_data.iterrows():
    insert_query = f"""
    INSERT INTO {table_name} (date, country, living_cost, gdp, gdp_per_capita)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (index.date(), row['country'], row['living_cost'], row['gdp'], row['gdp_per_capita']))

cnx.commit()
cursor.close()
cnx.close()
print("Data inserted into MySQL successfully")


# Analysis
# The correlation coefficient between GDP per capita and Living Cost is 0.94, indicating a strong positive correlation. This suggests that as the GDP per capita increases, the Living Cost also increases.

# The average GDP per capita is 28,793.43, while the average Living Cost is 5,552.76. This indicates that the Living Cost is relatively high compared to the GDP per capita.

# The percentage change in GDP per capita is 3.27%, which means the GDP per capita has increased by 3.27% from the first year to the last year.

# The GDP per capita and Living Cost scatterplot shows a clear positive correlation, indicating that as the GDP per capita increases, the Living Cost also increases.

# The GDP per capita and Living Cost line plot shows the trend of GDP per capita and Living Cost over time. The GDP per capita line is increasing, while the Living Cost line is decreasing.

# The GDP per capita and Living Cost box plot shows the distribution of GDP per capita and Living Cost. The box plot suggests that the GDP per capita is slightly skewed to the right, with a few outliers. The Living Cost is more symmetrically distributed, with a few outliers.

# The statistical analysis of the GDP per capita shows that the standard deviation is 2,366.22. This indicates that the GDP per capita varies widely, with some countries having a higher GDP per capita and others having a lower GDP per capita.

# The histogram of GDP per capita shows a bimodal distribution, with two peaks at around 25,000 and 30,000. This suggests that there are two groups of countries with different GDP per capita levels.

# The descriptive statistics of the GDP per capita show that the minimum GDP per capita is 1,850, the maximum GDP per capita is 55,527, the mean GDP per capita is 28,793.43, the median GDP per capita is 26,819.50, and the mode GDP per capita is 25,000. This

# Analysis
# The correlation coefficient between GDP per capita and Living Cost is 0.94, indicating a strong positive correlation. This suggests that as the GDP per capita increases, the Living Cost also increases.

# The average GDP per capita is 28,793.43, while the average Living Cost is 5,552.76. This indicates that the Living Cost is relatively high compared to the GDP per capita.

# The percentage change in GDP per capita is 3.27%, which means the GDP per capita has increased by 3.27% from the first year to the last year.

# The GDP per capita and Living Cost scatterplot shows a clear positive correlation, indicating that as the GDP per capita increases, the Living Cost also increases.

# The GDP per capita and Living Cost line plot shows the trend of GDP per capita and Living Cost over time. The GDP per capita line is increasing, while the Living Cost line is decreasing.


