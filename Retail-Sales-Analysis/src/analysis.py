import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("data/cleaned_sales_data.csv")

df['Date'] = pd.to_datetime(df['Date'])

# Create Month column
df['Month'] = df['Date'].dt.to_period('M')

# 1. Monthly Sales
monthly_sales = df.groupby('Month')['Total_Amount'].sum()

plt.figure()
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/monthly_sales.png")

# 2. Category Analysis
category_sales = df.groupby('Product_Category')['Total_Amount'].sum()

plt.figure()
category_sales.plot(kind='bar')
plt.title("Category Sales")
plt.savefig("images/category_sales.png")

# 3. Gender Analysis
gender_sales = df.groupby('Gender')['Total_Amount'].sum()

plt.figure()
gender_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Gender Sales")
plt.ylabel("")
plt.savefig("images/gender_sales.png")

# 4. Age Group Analysis
df['Age_Group'] = pd.cut(df['Age'], bins=[0,18,30,45,60,100],
                        labels=['<18','18-30','30-45','45-60','60+'])

age_sales = df.groupby('Age_Group', observed=False)['Total_Amount'].sum()

plt.figure()
age_sales.plot(kind='bar')
plt.title("Age Group Sales")
plt.savefig("images/age_sales.png")

print("✅ Analysis Completed!")