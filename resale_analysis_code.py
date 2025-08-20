import pandas as pd

### Hello from Hong En

# Load the CSV file
df = pd.read_csv("ResaleflatpricesbasedonregistrationdatefromJan2017onwards.csv")

# Extract year from the 'month' column
df['year'] = pd.to_datetime(df['month']).dt.year

# Group by year and calculate average resale price
avg_prices = df.groupby('year')['resale_price'].mean().reset_index()

# Display results
print(avg_prices)

# Optionally save to CSV
avg_prices.to_csv("average_resale_prices_by_year.csv", index=False)
