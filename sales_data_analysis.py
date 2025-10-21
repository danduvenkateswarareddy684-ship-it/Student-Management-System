# Sales Data Analysis using Pandas
# Calculates total, average, and maximum sales from sample data

import pandas as pd

# Sample sales data
data = {
    'Product': ['Laptop', 'Phone', 'Tablet', 'Headphones', 'Smartwatch'],
    'Sales': [85000, 45000, 30000, 15000, 20000],
    'Quantity': [10, 25, 15, 40, 30]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the data
print("Sales Data:\n", df)

# Basic Analysis
print("\nTotal Sales Amount:", df['Sales'].sum())
print("Average Sales Amount:", df['Sales'].mean())
print("Highest Sales Amount:", df['Sales'].max())

# Extra: Product with highest sales
top_product = df.loc[df['Sales'].idxmax(), 'Product']
print("\nTop Selling Product:", top_product)
