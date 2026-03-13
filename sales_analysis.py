import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

print(df.head())

# Monthly Sales
monthly_sales = df.groupby('Month')['Sales'].sum()

plt.bar(monthly_sales.index, monthly_sales.values)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.show()

# Orders by Hour
hour_orders = df.groupby('Hour')['Order ID'].count()

plt.plot(hour_orders.index, hour_orders.values)
plt.xlabel("Hour")
plt.ylabel("Orders")
plt.title("Orders by Hour")
plt.show()

# Price vs Quantity
plt.scatter(df['Price Each'], df['Quantity Ordered'])
plt.xlabel("Price")
plt.ylabel("Quantity")
plt.title("Price vs Quantity")
plt.show()