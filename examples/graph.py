import dash
import json
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import dash_core_components as dcc
import dash_html_components as html
from modules.dataADT import DataADT

d = DataADT()
with open('modules/data.json', 'r', encoding='utf-8') as ff:
    data = json.load(ff)

# write all data into DataADT
d.insert(data)

# Write names of all categories into list x
# amount of devices of each category into list y.
categories = d.category_count()
x, y = [], []
for i in categories:
    x.append(i)
    y.append(categories[i]) 

# Write number of devices of each category into list z.
categories_avail = d.category_count_avail()
z = []
for i in categories_avail:
    z.append(categories_avail[i]) 


# Create two bars with available devices and all devices.
fig = go.Figure(data=[
    go.Bar(name='Available', x=x, y=z),
    go.Bar(name='All', x=x, y=y, marker_color='lightslategrey')
])

# Change the bar title and name of y-axis.
fig.update_layout(barmode='group', title='Comparison of categories',yaxis=dict(
        title='Number of devices'
    ))
# Show bar
fig.show()