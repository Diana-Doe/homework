'''
The simple module that demonstrates the work of libraries dash and Plotly. 
Requires JSON file that you can get using module scraping.py.
Creates bar with x-axis as names of categories and y as numbers of products in each category.
Copyright (c) 2020 Diana Hromyak
'''
import dash
import json
import plotly.graph_objects as go 
import dash_core_components as dcc
import dash_html_components as html

# firstly we need to get data from our JSON file
with open("information.json", "r") as read_file:
    data = json.load(read_file)['data']

# Write each category into a dictionary as key and 
# list with names of products as its value.
categories = dict()
for item in data:
    for category in item['category']:
        if category not in categories:
            categories[category] = []
        categories[category].append(item['name'])

# Create two list for x-axis and y-axis. 
# Append categories into list x and amount of products in y.
x, y = [], []
for category in categories:
    x.append(category)
    y.append(len(categories[category]))

    
# Create bar
fig = go.Figure()
fig.add_trace(go.Bar(
    x = x,
    y = y
))

#You don't need to generate offline and online bar, 
# it was made to show opportunities of both libraries (plotly and dash)
# If you need only offline bar - comment all below fig.show()
fig.show()
app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)