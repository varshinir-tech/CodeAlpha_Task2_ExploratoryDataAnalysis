import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("sales_dataset.csv")

print("\n===== DATASET OVERVIEW =====")
print(df.head())

print("\n===== DATASET INFO =====")
print(df.info())

print("\n===== STATISTICS =====")
print(df.describe())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Total Sales by Category
plt.figure(figsize=(8,5))
sns.barplot(x="Category", y="Sales", data=df)
plt.title("Sales by Category")
plt.savefig("sales_by_category.png")
plt.show()

# Profit by Region
plt.figure(figsize=(8,5))
sns.barplot(x="Region", y="Profit", data=df)
plt.title("Profit by Region")
plt.savefig("profit_by_region.png")
plt.show()

# Sales Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Sales"], bins=10, kde=True)
plt.title("Sales Distribution")
plt.savefig("sales_distribution.png")
plt.show()

print("\nEDA Completed Successfully!")

# =========================
# BUSINESS INSIGHTS REPORT
# =========================

top_region = df.groupby("Region")["Profit"].sum().idxmax()
top_category = df.groupby("Category")["Sales"].sum().idxmax()

with open("reports/business_insights.txt", "w") as f:
    f.write("===== BUSINESS INSIGHTS REPORT =====\n\n")

    f.write(f"Top Performing Region: {top_region}\n")
    f.write(f"Best Selling Category: {top_category}\n\n")

    f.write("Strategic Recommendations:\n")
    f.write("- Increase marketing budget in high profit regions.\n")
    f.write("- Expand inventory for best selling categories.\n")
    f.write("- Focus on customer retention programs.\n")
    f.write("- Monitor low performing regions.\n")

print("Business Insights Report Generated!")

# =========================
# CORRELATION HEATMAP
# =========================

plt.figure(figsize=(8,6))

correlation = df[["Sales","Profit"]].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title("Sales vs Profit Correlation")
plt.savefig("visualizations/correlation_heatmap.png")
plt.close()

print("Correlation Heatmap Generated!")





print("\n===== PROJECT SUMMARY =====")
print(f"Dataset Records : {len(df)}")
print(f"Total Revenue   : ₹{df['Sales'].sum():,.2f}")
print(f"Total Profit    : ₹{df['Profit'].sum():,.2f}")

profit_margin = (df['Profit'].sum()/df['Sales'].sum())*100
print(f"Profit Margin   : {profit_margin:.2f}%")