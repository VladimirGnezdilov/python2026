import csv
import json
from collections import defaultdict
with open('sales_data.csv', 'r') as f:
    data = list(csv.DictReader(f))
date = input("Введите дату (формат YYYY-MM-DD): ")
product_sales = defaultdict(int)
store_revenue = defaultdict(float)
for row in data:
    if row['Date'] == date:
        product = row['Product']
        store = row['Store']
        revenue = float(row['Price']) * int(row['Quantity'])
        product_sales[product] += int(row['Quantity'])
        store_revenue[store] += revenue
if store_revenue:
    top_store = max(store_revenue, key=store_revenue.get)
    print(f"Наибольшие продажи за {date}: {top_store} с объёмом продаж {int(store_revenue[top_store])}")
else:
    print("Нет данных за указанную дату")
report = {date: [{"product": p, "total_sales": s} for p, s in product_sales.items()]}
with open('sales_report.json', 'w') as f:
    json.dump(report, f, indent=4)
