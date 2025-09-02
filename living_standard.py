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

#scrape population data
population_data=fetch_gdp_data("https://api.worldbank.org/v2/country/IN/indicator/SP.POP.TOTL?format=json")
population_data.to_csv("population_data.csv")


print("Data saved successfully as gdp_per_capita_data.csv")

print("All data fetched successfully 3")

# rename columns before merging
living_cost_data.rename(columns={'value': 'living_cost'}, inplace=True)
gdp_data.rename(columns={'value': 'gdp'}, inplace=True)
gdp_per_capita_data.rename(columns={'value': 'gdp_per_capita'}, inplace=True)
population_data.rename(columns={'value': 'population'}, inplace=True)


#merge the data
merged_data = pd.merge(living_cost_data, gdp_data, how='inner', left_index=True, right_index=True)
merged_data = pd.merge(merged_data, gdp_per_capita_data, how='inner', left_index=True, right_index=True)
merged_data = pd.merge(merged_data, population_data, how='inner', left_index=True, right_index=True)
print("merged success")
'''# specific rename
merged_data.rename(columns={
    'value_x': 'living_cost',
    'value_y': 'gdp',
    'value_z': 'gdp_per_capita',
    'value_w': 'population'
}, inplace=True)'''

# save the merged data as a CSV file
merged_data.to_csv('living_standard.csv')

print("All data merged successfully and saved as living_standard.csv")

#visualize the merged data
sns.scatterplot(data=merged_data, x='living_cost', y='gdp')
plt.savefig('living_cost_vs_gdp.png')

print("All data visualizations saved successfully 3")

# calculate correlation coefficient
correlation_coefficient = merged_data['living_cost'].corr(merged_data['gdp'])
print(f"Correlation coefficient: {correlation_coefficient:.2f}")

print("All calculations completed successfully")

# calculate the percentage change in GDP and Living Cost
percentage_change_gdp = ((merged_data['gdp'].iloc[-1] - merged_data['gdp'].iloc[0]) / merged_data['gdp'].iloc[0]) * 100
percentage_change_living_cost = ((merged_data['living_cost'].iloc[-1] - merged_data['living_cost'].iloc[0]) / merged_data['living_cost'].iloc[0]) * 100

print(f"Percentage change in GDP: {percentage_change_gdp:.2f}%")
print(f"Percentage change in Living Cost: {percentage_change_living_cost:.2f}%")

# calculate the average GDP and Living Cost
average_gdp = merged_data['gdp'].mean()
average_living_cost = merged_data['living_cost'].mean()

print(f"Average GDP: {average_gdp:.2f}")
print(f"Average Living Cost: {average_living_cost:.2f}")

# visualize the GDP per capita
sns.lineplot(data=merged_data, x='date', y='gdp_per_capita')
plt.savefig('gdp_per_capita_chart.png')

# correlation coefficient between GDP per capita and Living Cost
correlation_coefficient_gdp_per_capita = merged_data['gdp_per_capita'].corr(merged_data['living_cost'])
print(f"Correlation coefficient between GDP per capita and Living Cost: {correlation_coefficient_gdp_per_capita:.2f}")

# average GDP per capita
average_gdp_per_capita = merged_data['gdp_per_capita'].mean()
print(f"Average GDP per capita: {average_gdp_per_capita:.2f}")

#percentage change in GDP per capita
percentage_change_gdp_per_capita = ((merged_data['gdp_per_capita'].iloc[-1] - merged_data['gdp_per_capita'].iloc[0]) / merged_data['gdp_per_capita'].iloc[0]) * 100

print(f"Percentage change in GDP per capita: {percentage_change_gdp_per_capita:.2f}%")

# Visualize the GDP per capita and Living Cost scatterplot
sns.scatterplot(data=merged_data, x='living_cost', y='gdp_per_capita')
plt.xlabel('Living Cost')
plt.ylabel('GDP per Capita')
plt.savefig('gdp_per_capita_scatter.png')
plt.show()

# Visualize the GDP per capita and Living Cost line plot
sns.lineplot(data=merged_data, x='date', y='living_cost', label='Living Cost')
sns.lineplot(data=merged_data, x='date', y='gdp_per_capita', label='GDP per Capita')
plt.legend()
plt.savefig('gdp_per_capita_line.png')
plt.show()

# Visualize the GDP per capita and Living Cost box plot
plt.figure(figsize=(12, 6))
sns.boxplot(data=merged_data[['living_cost', 'gdp_per_capita']])
plt.savefig('gdp_per_capita_box.png')
plt.show()

# Visualize the histogram of GDP per capita 
sns.histplot(data=merged_data['gdp_per_capita'])
plt.savefig('gdp_per_capita_hist.png')
plt.show()

# visualize gdp per capita by population
sns.scatterplot(data=merged_data, x='population', y='gdp_per_capita')
plt.xlabel('Population')
plt.ylabel('GDP per Capita')
plt.savefig('gdp_per_capita_by_population.png')
plt.show()

# visualize gdp by population
sns.scatterplot(data=merged_data, x='population', y='gdp')
plt.xlabel('Population')
plt.ylabel('GDP')
plt.savefig('gdp_by_population.png')
plt.show()

# visualize population by year
sns.lineplot(data=merged_data, x='date', y='population')
plt.xlabel('Year')
plt.ylabel('Population')
plt.savefig('population_by_year.png')
plt.show()

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
cursor.execute(f"DROP TABLE IF EXISTS living_standard")
print("Old table dropped successfully")

# Create table
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {"living_standard"} (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    country VARCHAR(255),
    population INT,
    living_cost FLOAT,
    gdp FLOAT,
    gdp_per_capita FLOAT
)
"""
cursor.execute(create_table_query)
print("Table created successfully")

# change column names to match MySQL requirements
merged_data.rename(columns={'date': 'date', 'country_x': 'country','population': 'population', 'living_cost': 'living_cost', 'gdp': 'gdp', 'gdp_per_capita': 'gdp_per_capita'}, inplace=True)
# Insert data
for index, row in merged_data.iterrows():
    insert_query = f"""
    INSERT INTO {table_name} (date, country, population, living_cost, gdp, gdp_per_capita)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (index.date(), row['country'], row['population'], row['living_cost'], row['gdp'], row['gdp_per_capita']))

cnx.commit()
cursor.close()
cnx.close()
print("Data inserted into MySQL successfully")


