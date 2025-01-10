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

print(sales_data.describe())
print(sales_date.info())

# Mapping and Trending the data
sales_data['Year-Month'] = sales_data['Date'].dt.to_period('M')
monthly_sales = sales_data.groupby('Year-Month')['Sales'].sum().reset_index()

# Sales Trend over time
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales['Year-Month'].astype(str), monthly_sales['Sales'], makrer = 'o', color='b')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Sales by Product
product_sales = sales_data.groupby('Product')['Sales'].sum().reset_index()
product_sales = product_sales.sort_values('Sales', ascending=False)

plt.figure(figzie=(10,6))
sns.barplot(x='Sales', y='Product', data=product_sales, palette='viridis')
plt.title('Sales by Product')
plt.xlabel('Total Sales')
plt.ylabel('Product')
plt.show()

# Sales by Region
region_sales = sales_data.groupby('Region')['Sales'].sum().reset_index()
region_sales = region_sales.sort_values('Sales', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x='Sales', y='Region', data=region_sales, palette='magma')
plt.title('Sales by Region')
plt.xlabel('Total Sales')
plt.ylabel('Region')
plt.show()

# Seasonality Analysis
sales_date['Month'] = sales_data['Date'].dt.month 
sales_data['Year'] = sales_data['Date'].dt.year 

monthly_seasonality = sales_data.groupby('Month')['Sales'].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(x='Month', y='Sales', data=monthly_seasonality, marker='o')
plt.title('Sales Seasonality by Month')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(ticks=np.arange(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid(True)
plt.show()
