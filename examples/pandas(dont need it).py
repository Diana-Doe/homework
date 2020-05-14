'''
!Require data.json. You can get it by using scr.py!
Require pandas and json libraries.
'''
import json
import pandas as pd


# Get data about products from JSON file.
with open('modules/data.json', 'r', encoding='utf-8') as ff:
    data = json.load(ff)

count = 0
data = data['data']
for i in data:
    for j in data[i]:
        if len(j['category']) > 1:
            count += 1
print(count)

# Create a pandas dataframe from data ejected from JSON file.
# DataFrame contains dates, names of products, categories,
# prices, customers and rates.
da = pd.concat({key: pd.DataFrame(val) for key, val in data['data'].items()}).reset_index()
del da['level_1']
da = da.rename(columns={"level_0": "date"}).set_index(['name'])

# All categories in lists but they need to be separate values.
# So split a list inside a Dataframe.
categories, names, dates, prices, customers, rates = [], [], [], [], [], []
for _, row in da.iterrows():
    date, name, price, customer, rate = row.date, row.name, row.price, row.customers, row.rate
    for category in row.category:
        dates.append(date)
        names.append(name)
        prices.append(price)
        customers.append(customer)
        rates.append(rate)
        categories.append(category)
# Create new DataFrame with separate categories.
data = pd.DataFrame({
    "date" : dates,
    "category": categories,
    "name": names,
    "price" : prices,
    "customers" : customers,
    "rate" : rates
})

# Set date and name of item as indexes.
data = data.set_index(['date', 'name'])
print(data.shape)
