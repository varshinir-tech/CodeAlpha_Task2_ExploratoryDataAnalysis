import pandas as pd
import random

categories = ["Electronics", "Furniture", "Clothing", "Sports", "Books"]
regions = ["North", "South", "East", "West"]

data = []

for i in range(1, 1001):
    category = random.choice(categories)
    region = random.choice(regions)

    sales = random.randint(500, 10000)
    profit = int(sales * random.uniform(0.1, 0.4))

    data.append([
        i,
        category,
        region,
        sales,
        profit
    ])

df = pd.DataFrame(
    data,
    columns=["OrderID", "Category", "Region", "Sales", "Profit"]
)

df.to_csv("sales_dataset.csv", index=False)

print("1000 Records Generated Successfully!")