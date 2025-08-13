import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from bs4 import BeautifulSoup

def fetch_living_cost_data(url,df=None):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to load page")
    data = response.json()
    df = pd.DataFrame(data[1])
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df = df[['value']]
    df.rename(columns={'value': 'Living Cost Index'}, inplace=True)
    df['Living Cost Index'] = pd.to_numeric(df['Living Cost Index'], errors='coerce')
    df.dropna(inplace=True)
    df.sort_index(inplace=True)
    df.plot(figsize=(12, 6))
    plt.title('Living Cost Index Over Time')
    plt.xlabel('Year')
    plt.ylabel('Living Cost Index')
    plt.grid()
    plt.show()
    
    
    








fetch_living_cost_data("https://api.worldbank.org/v2/country/IN/indicator/FP.CPI.TOTL?format=json")



