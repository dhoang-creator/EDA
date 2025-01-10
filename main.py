import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

sales_data = pd.read_csv('sales_data.csv')
sales_data.head()

print(sales_data.isnull().sum())
print(sales_data.duplicated)
sales_data['Date'] = pd.to_datetime(sales_data['Date'])
print(sales_data.dtypes)

