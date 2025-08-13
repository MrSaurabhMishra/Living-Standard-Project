import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from bs4 import BeautifulSoup

def fetch_living_cost_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to load page")
    data = response.json()
    df = pd.DataFrame(data[1])
    df.to_csv("living_cost_data.csv", index=False)
    print("Data fetched and saved to living_cost_data.csv")


fetch_living_cost_data("https://api.worldbank.org/v2/country/IN/indicator/FP.CPI.TOTL?format=json")