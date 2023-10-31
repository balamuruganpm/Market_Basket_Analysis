import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from apyori import apriori
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# load & read the datasets
mba_data = pd.read_excel("mba.xlsx")
print(mba_data)

# head of datasets
print(mba_data.head())

# Clean the dataset by removing rows with missing or duplicate values
missing_values = mba_data['BillNo'].isnull().sum()
duplicate_values = mba_data['BillNo'].duplicated().sum()
print(f"Missing values in 'BillNo' column: {missing_values}")
print(f"Duplicate values in 'BillNo' column: {duplicate_values}")

# Clean the dataset by removing rows with missing or duplicate values in the "BillNo" column
mba_data_cleaned = mba_data.dropna(subset=['BillNo']).drop_duplicates(subset=['BillNo'])
mba_data_cleaned.to_csv("cleaned_mba.csv", index=False)
print("Cleaned dataset saved as 'cleaned_mba.csv'")

# Group the data by Date and calculate the total sales for each date
date_sales = mba_data.groupby('Date')['Price'].sum()
# Find the date with the highest total sales
date_with_highest_sales = date_sales.idxmax()
print(f"The date with the highest sales is {date_with_highest_sales} with a total sales of {date_sales.max()}")

# Group the data by Country and calculate the total sales for each country
country_sales = mba_data.groupby('Country')['Price'].sum()
# Find the country with the highest total sales
country_with_highest_sales = country_sales.idxmax()
print(f"The country with the highest sales is {country_with_highest_sales} with a total sales of {country_sales.max()}")

# Group the data by Itemname and calculate the total quantity sold for each item
item_sales = mba_data.groupby('Itemname')['Quantity'].sum()
sorted_items = item_sales.sort_values(ascending=False)
plt.figure(figsize=(10, 6))
plt.bar(sorted_items.index, sorted_items)
plt.xlabel('Item Names')
plt.ylabel('Totally Sold by Value')
plt.title('Items with Highest Sales (by Quantity)')
plt.xticks(rotation=100)
plt.show()

# Sales Distribution of Items using Seaborn
plt.figure(figsize=(12, 6))
sns.countplot(data=data, x='Itemname', order=data['Itemname'].value_counts().index)
plt.title('Item Distribution')
plt.xticks(rotation=90)
plt.show()

# Calculate item popularity
item_popularity = data['Itemname'].value_counts().head(10)

# Top 10 Most Popular Items using Seaborn
plt.figure(figsize=(12, 6))
sns.barplot(x=item_popularity.index, y=item_popularity.values, palette='viridis')
plt.title(f'Top 10 Most Popular Items')
plt.xticks(rotation=90)
plt.show()


# Calculate average quantity and spending per customer
customer_behavior = data.groupby('CustomerID').agg({'Quantity': 'mean', 'Price': 'sum'}).reset_index()

# Create a scatter plot
plt.figure(figsize=(12, 6))
plt.scatter(customer_behavior['Quantity'], customer_behavior['Price'], s=100, c='coral', label='Customers')
plt.title('Customer Behavior')
plt.xlabel('Average Quantity')
plt.ylabel('Total Spending')

# Add a table to the plot
cell_text = []
for row in customer_behavior.itertuples(index=False):
    cell_text.append([row.CustomerID, row.Quantity, row.Price])

plt.table(cellText=cell_text, colLabels=['CustomerID', 'Average Quantity', 'Total Spending'], loc='bottom', cellLoc='center')
plt.show()
