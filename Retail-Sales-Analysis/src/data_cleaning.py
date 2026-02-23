import pandas as pd

# Load data
df = pd.read_csv("data/raw_sales_data.csv")

print("Before Cleaning:")
print(df.head())

# Fix column names
df.columns = df.columns.str.replace(" ", "_")

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Quantity'] = df['Quantity'].fillna(df['Quantity'].median())
df['Price_per_Unit'] = df['Price_per_Unit'].fillna(df['Price_per_Unit'].mean())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Recalculate total
df['Total_Amount'] = df['Quantity'] * df['Price_per_Unit']

# Clean text columns
df['Gender'] = df['Gender'].str.strip().str.title()

# Save cleaned data
df.to_csv("data/cleaned_sales_data.csv", index=False)

print("✅ Data Cleaning Completed!")