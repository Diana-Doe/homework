import dash
import json
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dataADT import DataADT

# Create object of class DataADT and read data from 
# json file.
d = DataADT()
with open('modules/data.json', 'r', encoding='utf-8') as ff:
    data = json.load(ff)

# Convert data into ADT.
d.insert(data)

categories = d.category_count()
categor, dev1 = [], []
for i in categories:
    categor.append(i)
    dev1.append(categories[i]) 

categories_avail = d.category_count_avail()
dev2 = []
for i in categories_avail:
    dev2.append(categories_avail[i]) 

# Create Categories-Devices graph. 
# Create two bars with available devices and all devices.
fig = go.Figure(data=[
    go.Bar(name='Available', x=categor, y=dev2),
    go.Bar(name='All', x=categor, y=dev1, marker_color='lightslategrey')
])

# Change the bar title and name of y axis.
fig.update_layout(barmode='group', 
        title='Categories-Devices',
        yaxis=dict(
        title='Number of devices',
        showgrid=False,
        showline=True,
        linecolor='rgb(100, 100, 100)',
        tickfont_color='rgb(100, 100, 100)'
    ),
    paper_bgcolor='white',
    plot_bgcolor='white' )

fig.show()

date = d.date_count()
dates, devices1 = [], []
for i in date:
    dates.append(i)
    devices1.append(date[i])

date2 = d.date_count_avail()
devices2 = []
for i in date2:
    devices2.append(date2[i])

# Create Dates-Devices graph.
line = go.Figure()
line.add_trace(go.Scatter(x=dates, y=devices1, name='All'))
line.add_trace(go.Scatter(x=dates, y=devices2, name='Available', line=dict(color='firebrick')))
line.update_layout(
    title='Dates-Devices',
    xaxis=dict(
        showgrid=False,
        showline=True,
        linecolor='rgb(100, 100, 100)',
        tickfont_color='rgb(100, 100, 100)'
    ),
    yaxis=dict(
        showline=True,
        linecolor='rgb(100, 100, 100)',
        tickfont_color='rgb(100, 100, 100)',
        title='Number of devices'
    ),
    paper_bgcolor='white',
    plot_bgcolor='white'
)
line.show()

date_cust = d.date_customers()
dates_cust, cust = [], []
for i in date_cust:
    dates_cust.append(i)
    cust.append(date_cust[i])

# Create Dates-Customers graph.
line2 = go.Figure()
line2.add_trace(go.Scatter(x=dates_cust, y=cust))
line2.update_layout(
    title='Dates-Customers',
    xaxis=dict(
        showgrid=False,
        showline=True,
        linecolor='rgb(100, 100, 100)',
        tickfont_color='rgb(100, 100, 100)'
    ),
    yaxis=dict(
        showline=True,
        linecolor='rgb(100, 100, 100)',
        tickfont_color='rgb(100, 100, 100)',
        title='Number of customers'
    ),
    paper_bgcolor='white',
    plot_bgcolor='white'
)

line2.show()


# app = dash.Dash(external_stylesheets=[dbc.themes.LUX])
# app.title = 'SmartHome'

# app.layout = dbc.Tabs([dbc.Tab(dcc.Graph(figure=fig), label="Categories")])

# app.run_server(debug=True, use_reloader=False)

prices, rates, names, categorise_p_r, customers = [], [], [], [], []
for item in d.list:
    if item['date'] == d.newest:
        price, rate = item['price'], item['rate']
        if price != 'Pending' and rate != 0:
            prices.append(price)
            rate = (rate * 5) / 100
            rates.append(rate)
            names.append(item['name'])
            categorise_p_r.append(item['category'])
            customers.append(item['customers'])

# Create Price-Rate graph.
pr_rt = go.Figure()
pr_rt.add_trace(go.Scatter(
    x=prices,
    y=rates,
    text=names,
    mode="markers",
    marker=dict(
        color=rates
    )
))

pr_rt.update_layout(
    title='Price-Rate',
    xaxis=dict(
        showgrid=False,
        showline=True,
        linecolor='rgb(100, 100, 100)',
        tickfont_color='rgb(100, 100, 100)',
        title='Price($)',
        range=[0, 12000]
    ),
    yaxis=dict(
        showline=True,
        linecolor='rgb(100, 100, 100)',
        tickfont_color='rgb(100, 100, 100)',
        title='Rate(stars)'
    ),
    paper_bgcolor='white',
    plot_bgcolor='white'
)

pr_rt.show()

diction = {}
for i in range(len(categorise_p_r)):
    rate, price = rates[i], prices[i]
    for cat in categorise_p_r[i]:
        if cat in diction:
            diction[cat][0] += rate
            diction[cat][1] += price
            diction[cat][2] += 1
        else:
            diction[cat] = [rate, price, 1]

categor_bubble, rate_bubble, price_bubble, size_bubble, color_bubble = [], [], [], [], []
for i, j in diction.items():
    categor_bubble.append('Category:{}<br>Devices:{}'.format(i, j[2]))
    rate_bubble.append(j[0]/j[2])
    price_bubble.append(j[1]/j[2])
    size_bubble.append(j[2])

# Create Category-Price-Rate graph.
bubble = go.Figure()
bubble.add_trace(go.Scatter(
    x=price_bubble,
    y=rate_bubble,
    text=categor_bubble,
    mode="markers",
    marker=dict(
        color=size_bubble,
        size=size_bubble)
))

bubble.update_layout(
    title='Category-Price-Rate',
    xaxis=dict(
        showgrid=False,
        showline=True,
        linecolor='rgb(100, 100, 100)',
        tickfont_color='rgb(100, 100, 100)',
        title='Price($)'
    ),
    yaxis=dict(
        showline=True,
        linecolor='rgb(100, 100, 100)',
        tickfont_color='rgb(100, 100, 100)',
        title='Rate(stars)'
    ),
    paper_bgcolor='white',
    plot_bgcolor='white'
)

bubble.show()

# Create Price-customers graph.
dot_cust = go.Figure()
dot_cust.add_trace(go.Scatter(
        x=prices,
        y=customers,
        text=names,
        mode="markers",
        marker=dict(
            color=prices
    )
))

dot_cust.update_layout(
    title='Price-customers',
    xaxis=dict(
        showgrid=False,
        showline=True,
        linecolor='rgb(100, 100, 100)',
        tickfont_color='rgb(100, 100, 100)',
        title='Price($)',
        range=[0, 6000]
    ),
    yaxis=dict(
        showline=True,
        linecolor='rgb(100, 100, 100)',
        tickfont_color='rgb(100, 100, 100)',
        title='Customers',
        range=[0,350]
    ),
    paper_bgcolor='white',
    plot_bgcolor='white'
)

dot_cust.show()

# Create Rate-Customers graph.
dot_rate = go.Figure()
dot_rate.add_trace(go.Scatter(
        x=customers,
        y=rates,
        text=names,
        mode="markers",
        marker=dict(
            color=prices
    )
))

dot_rate.update_layout(
    title='Rate-Customers',
    xaxis=dict(
        showgrid=False,
        showline=True,
        linecolor='rgb(100, 100, 100)',
        tickfont_color='rgb(100, 100, 100)',
        title='Customers',
        range=[0,350]
    ),
    yaxis=dict(
        showline=True,
        linecolor='rgb(100, 100, 100)',
        tickfont_color='rgb(100, 100, 100)',
        title='Rate(stars)'
    ),
    paper_bgcolor='white',
    plot_bgcolor='white'
)

dot_rate.show()
