# DV0101EN - Final Assignment Part 1
# Data Visualization with Python

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv")

# Task 1.1 - Line plot of total sales per year
sales_per_year = df.groupby("Year")["Automobile_Sales"].sum()
plt.figure(figsize=(10, 6))
sales_per_year.plot(marker='o')
plt.title("Total Automobile Sales per Year")
plt.xlabel("Year")
plt.ylabel("Automobile Sales")
plt.grid(True)
plt.savefig("Line_plot_1.png")
plt.show()

# Task 1.2 - Line plot by vehicle type during recession
recession_data = df[df['Recession'] == True]
pivot = recession_data.pivot_table(values='Automobile_Sales', index='Year', columns='Vehicle_Type', aggfunc='sum')
plt.figure(figsize=(12, 6))
pivot.plot(marker='o')
plt.title("Vehicle Type Sales During Recession Period")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.legend(title="Vehicle Type")
plt.grid(True)
plt.savefig("Line_plot_2.png")
plt.show()

# Task 1.3 - Seaborn bar chart: Recession vs Non-Recession
rec = df[df['Recession'] == True]
non_rec = df[df['Recession'] == False]
rec['Period'] = 'Recession'
non_rec['Period'] = 'Non-Recession'
combined = pd.concat([rec, non_rec])
grouped = combined.groupby(['Vehicle_Type', 'Period'])['Automobile_Sales'].sum().reset_index()
plt.figure(figsize=(10,6))
sns.barplot(data=grouped, x="Vehicle_Type", y="Automobile_Sales", hue="Period")
plt.title("Sales by Vehicle Type: Recession vs Non-Recession")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Bar_Chart.png")
plt.show()

# Task 1.4 - GDP Subplot Comparison
fig, ax = plt.subplots(1, 2, figsize=(14, 5))
df[df['Recession'] == True].groupby("Year")['GDP'].mean().plot(ax=ax[0], marker='o', title="GDP During Recession")
ax[0].set_xlabel("Year")
ax[0].set_ylabel("GDP")
df[df['Recession'] == False].groupby("Year")['GDP'].mean().plot(ax=ax[1], marker='o', title="GDP During Non-Recession")
ax[1].set_xlabel("Year")
ax[1].set_ylabel("GDP")
plt.tight_layout()
plt.savefig("Subplot.png")
plt.show()

# Task 1.5 - Bubble plot (seasonality impact)
plt.figure(figsize=(12, 6))
plt.scatter(df['Year'], df['Month'], s=df['Automobile_Sales']/1000, alpha=0.5, c='skyblue', edgecolors='k')
plt.title("Bubble Plot: Seasonality Impact on Sales")
plt.xlabel("Year")
plt.ylabel("Month")
plt.grid(True)
plt.savefig("Bubble.png")
plt.show()

# Task 1.6 - Scatter Plot: Price vs Sales During Recession
rec_data = df[df['Recession'] == True]
plt.figure(figsize=(8,6))
plt.scatter(rec_data['Average_Vehicle_Price'], rec_data['Automobile_Sales'], alpha=0.6)
plt.title("Scatter Plot: Vehicle Price vs Sales During Recession")
plt.xlabel("Average Vehicle Price")
plt.ylabel("Automobile Sales")
plt.grid(True)
plt.savefig("Scatter.png")
plt.show()

# Task 1.7 - Pie chart: Ad spend during vs non-recession
recession_total = df[df['Recession'] == True]['Advertising_Expenditure'].sum()
non_recession_total = df[df['Recession'] == False]['Advertising_Expenditure'].sum()
plt.figure(figsize=(6,6))
plt.pie([recession_total, non_recession_total], labels=['Recession', 'Non-Recession'], autopct='%1.1f%%', colors=['#ff9999','#66b3ff'])
plt.title("Ad Spend: Recession vs Non-Recession")
plt.savefig("Pie_1.png")
plt.show()

# Task 1.8 - Pie chart: Ad spend by vehicle type during recession
vehicle_ads = df[df['Recession'] == True].groupby("Vehicle_Type")['Advertising_Expenditure'].sum()
plt.figure(figsize=(8, 8))
plt.pie(vehicle_ads, labels=vehicle_ads.index, autopct='%1.1f%%', startangle=140)
plt.title("Ad Expenditure by Vehicle Type (Recession)")
plt.savefig("Pie_2.png")
plt.show()

# Task 1.9 - Line Plot: Unemployment vs Sales by Vehicle Type (Recession)
recession = df[df['Recession'] == True]
vehicle_unemp = recession.groupby(['Year', 'Vehicle_Type'])[['Unemployment_Rate', 'Automobile_Sales']].mean().reset_index()
plt.figure(figsize=(12,6))
for vt in vehicle_unemp['Vehicle_Type'].unique():
    vt_data = vehicle_unemp[vehicle_unemp['Vehicle_Type'] == vt]
    plt.plot(vt_data['Year'], vt_data['Automobile_Sales'], label=vt)
plt.title("Effect of Unemployment on Vehicle Sales (Recession)")
plt.xlabel("Year")
plt.ylabel("Automobile Sales")
plt.legend(title="Vehicle Type")
plt.grid(True)
plt.savefig("Line_plot_3.png")
plt.show()
