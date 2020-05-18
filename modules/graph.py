'''Module for creating graphs and site'''
import dash
import json
import plotly.graph_objects as go
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dataADT import DataADT

#################################################################################################
#Graphs

# Create object of class DataADT and read data from 
# json file.
d = DataADT()
with open('modules/data.json', 'r', encoding='utf-8') as ff:
    data = json.load(ff)

#Convert data into ADT.
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
        yaxis=dict(
        title='Number of devices',
        showgrid=False,
        showline=True,
        linecolor='rgb(100, 100, 100)',
        tickfont_color='rgb(100, 100, 100)'
    ),
    paper_bgcolor='white',
    plot_bgcolor='white' )


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


date_cust = d.date_customers()
dates_cust, cust = [], []
for i in date_cust:
    dates_cust.append(i)
    cust.append(date_cust[i])

# Create Dates-Customers graph.
line2 = go.Figure()
line2.add_trace(go.Scatter(x=dates_cust, y=cust))
line2.update_layout(
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

####################################################################################################
#   Site

HOME_LOGO = "https://www.nicepng.com/png/full/420-4209725_smart-homes-wifi-sign.png"

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
nav_item1 = dbc.NavItem(
    dbc.NavLink("GitHub", href='https://github.com/Diana-Doe/homework')
)
nav_item2 = dbc.NavItem(dbc.NavLink("Database", href='https://www.smarthomedb.com/products'))
nav_item = dbc.NavItem(dbc.NavLink("Dash Udemy Course", href="https://www.udemy.com/course/plotly-dash/?referralCode=16FC11D8981E0863E557"))
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=HOME_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("SmartHome", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    [nav_item1,
                     nav_item2
                     ], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-5",
)

####################
#   Body

SliderApp1 = html.Div([
    html.H1('Date-Devices graph'),
    dcc.Graph(figure=line, id='slide1')
])

SliderApp2 = html.Div([
    html.H1('Category-Devices bar'),
    dcc.Graph(figure=fig, id='slide2')
])

SliderApp3 = html.Div([
    html.H1('Date-Customers graph'),
    dcc.Graph(figure=line2, id='slide3')
])

SliderApp4 = html.Div([
    html.H1('Price-rate graph'),
    dcc.Graph(figure=pr_rt, id='slide4')
])
SliderApp5 = html.Div([
    html.H1('Categories bubble'),
    dcc.Graph(figure=bubble, id='slide5')
])
SliderApp6 = html.Div([
    html.H1('Price-customers graph'),
    dcc.Graph(figure=dot_cust, id='slide6')
])
SliderApp7 = html.Div([
    html.H1('Rate-customers graph'),
    dcc.Graph(figure=dot_rate, id='slide7')
])

cardOne = dbc.Card(
    [
        dbc.CardImg(src="https://i.pcmag.com/imagery/articles/0100gZDnjpDgR5KqbpXcvMX-7.fit_scale.size_2698x1517.v1569490902.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Date-Devices", className="card-title"),
                html.P(
                    "This is simple linear trendline. \
                    It shows change the number of available devices and all devices.",
                    className="card-text",
                    style={'height': '99.2px'}
                ),
                dbc.Button("Open graph", id="open",  color='primary', style={'margin': 'auto', 'width': '100%'}),
                dbc.Modal(
                    [
                        dbc.ModalHeader("SmartHome"),
                        dbc.ModalBody(SliderApp1),
                        dbc.ModalFooter(
                            dbc.Button("Close", id="close", className="ml-auto")
                        ),
                    ],
                    id="modal",
                    size='xl'
                ),
            ]
        ),
    ],
    style={"width": "18rem", 'height': '396px'},
)
cardTwo = dbc.Card(
    [
        dbc.CardImg(src="https://cumgeek.com/wp-content/uploads/2017/08/Smart-Home-graphic-scaled.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Caregories", className="card-title"),
                html.P(
                    "This is simple bar that represents categories.",
                    className="card-text",
                ),
                dbc.Button("Open graph", id="opentwo", color='primary', style={'margin': 'auto', 'width': '100%'}),
                dbc.Modal(
                    [
                        dbc.ModalHeader("SmartHome"),
                        dbc.ModalBody(SliderApp2),
                        dbc.ModalFooter(
                            dbc.Button("Close", id="closetwo", className="ml-auto")
                        ),
                    ],
                    id="modaltwo",
                    size='xl'
                ),
            ]
        ),
    ],
    style={"width": "18rem", 'height': '396px'},
)
cardThree = dbc.Card(
    [
        dbc.CardImg(src="https://ichip.ru/blobimgs/uploads/2019/03/smart-home-3395994_960_720.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Date-Customers", className="card-title"),
                html.P(
                    "This is simple linear trendline. It shows growth of customers.",
                    className="card-text",
                    style={'height': '74.95px'}
                ),
                dbc.Button("Open graph", id="openthree", color='primary', style={'margin': 'auto', 'width': '100%'}),
                dbc.Modal(
                    [
                        dbc.ModalHeader("SmartHome"),
                        dbc.ModalBody(SliderApp3),
                        dbc.ModalFooter(
                            dbc.Button("Close", id="closethree", className="ml-auto")
                        ),
                    ],
                    id="modalthree",
                    size='xl'
                ),
            ]
        ),
    ],
    style={"width": "18rem", 'height': '396px'},
)
cardFour = dbc.Card(
    [
        dbc.CardImg(src="https://www.eletimes.com/wp-content/uploads/2017/02/The-internet-of-things.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Rate-Price", className="card-title"),
                html.P(
                    "This is simple dot graph. It shows dependence of the price on a rating.",
                    className="card-text",
                    style={'height': '99.39px'}
                ),
                dbc.Button("Open graph", id="openfour", color='primary', style={'margin': 'auto', 'width': '100%'}),
                dbc.Modal(
                    [
                        dbc.ModalHeader("SmartHome"),
                        dbc.ModalBody(SliderApp4),
                        dbc.ModalFooter(
                            dbc.Button("Close", id="closefour", className="ml-auto")
                        ),
                    ],
                    id="modalfour",
                    size='xl'
                ),
            ]
        ),
    ],
    style={"width": "18rem", 'height': '396px'},
)
cardFive = dbc.Card(
    [
        dbc.CardImg(src="https://www.techfunnel.com/wp-content/uploads/2019/10/7-Free-Marketing-Automation-Tools-for-SMBs.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Category-Price-Rate", className="card-title"),
                html.P(
                    "This is simple bubble graph. It shows dependence of categories on rate and price.",
                    className="card-text",
                    style={'height': '94.75px'}
                ),
                dbc.Button("Open graph", id="openfive", color='primary', style={'margin': 'auto', 'width': '100%'}),
                dbc.Modal(
                    [
                        dbc.ModalHeader("SmartHome"),
                        dbc.ModalBody(SliderApp5),
                        dbc.ModalFooter(
                            dbc.Button("Close", id="closefive", className="ml-auto")
                        ),
                    ],
                    id="modalfive",
                    size='xl'
                ),
            ]
        ),
    ],
    style={"width": "18rem", 'height': '396px'},
)
cardSix = dbc.Card(
    [
        dbc.CardImg(src="https://cdn.makeuseof.com/wp-content/uploads/2017/10/Smart-Home-Break-Even-Featured-670x335.jpg?x97327", top=True),
        dbc.CardBody(
            [
                html.H4("Price-Customers", className="card-title"),
                html.P(
                    "This is simple dot graph. It shows dependence of customers on price.",
                    className="card-text",
                    style={'height': '117.25px'}
                ),
                dbc.Button("Open graph", id="opensix", color='primary', style={'margin': 'auto', 'width': '100%'}),
                dbc.Modal(
                    [
                        dbc.ModalHeader("SmartHome"),
                        dbc.ModalBody(SliderApp6),
                        dbc.ModalFooter(
                            dbc.Button("Close", id="closesix", className="ml-auto")
                        ),
                    ],
                    id="modalsix",
                    size='xl'
                ),
            ]
        ),
    ],
    style={"width": "18rem", 'height': '396px'},
)
cardSeven = dbc.Card(
    [
        dbc.CardImg(src="https://images.idgesg.net/images/article/2018/06/ring-alarm-lifestyle-100761146-large.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Rate-Customers", className="card-title"),
                html.P(
                    "This is simple dot graph. It shows dependence of customers on rate.",
                    className="card-text",
                    style={'height': '69.59px'}
                ),
                dbc.Button("Open graph", id="openseven", color='primary', style={'margin': 'auto', 'width': '100%'}),
                dbc.Modal(
                    [
                        dbc.ModalHeader("SmartHome"),
                        dbc.ModalBody(SliderApp7),
                        dbc.ModalFooter(
                            dbc.Button("Close", id="closeseven", className="ml-auto")
                        ),
                    ],
                    id="modalseven",
                    size='xl'
                ),
            ]
        ),
    ],
    style={"width": "18rem", 'height': '396px'},
)

row = html.Div(
    [
        dbc.Row(html.P('')),
        dbc.Row(
            [
                dbc.Col(html.Div(cardOne)),
                dbc.Col(html.Div(cardTwo)),
                dbc.Col(html.Div(cardThree)),
            ],
            style={'margin': 'auto', 'width': '78vw'}
),
        dbc.Row(html.P('')),
        dbc.Row(
            [
                dbc.Col(html.Div(cardFour)),
                dbc.Col(html.Div(cardFive)),
                dbc.Col(html.Div(cardSix))
            ],
            style={'margin': 'auto', 'width': '78vw'}
),
        dbc.Row(html.P('')),
        dbc.Row(
            [
                dbc.Col(html.Div(cardSeven))
            ],
            style={'margin': 'auto', 'width': '26vw'}
),
    ]
)

"""Layout"""

app.layout = html.Div(
    [navbar, row]
)

#module One
@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
#Module Two
@app.callback(
    Output("modaltwo", "is_open"),
    [Input("opentwo", "n_clicks"), Input("closetwo", "n_clicks")],
    [State("modaltwo", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

#Module Three
@app.callback(
    Output("modalthree", "is_open"),
    [Input("openthree", "n_clicks"), Input("closethree", "n_clicks")],
    [State("modalthree", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

#Module Four
@app.callback(
    Output("modalfour", "is_open"),
    [Input("openfour", "n_clicks"), Input("closefour", "n_clicks")],
    [State("modalfour", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

#Module Five
@app.callback(
    Output("modalfive", "is_open"),
    [Input("openfive", "n_clicks"), Input("closefive", "n_clicks")],
    [State("modalfive", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

#Module Six
@app.callback(
    Output("modalsix", "is_open"),
    [Input("opensix", "n_clicks"), Input("closesix", "n_clicks")],
    [State("modalsix", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

#Module Seven
@app.callback(
    Output("modalseven", "is_open"),
    [Input("openseven", "n_clicks"), Input("closeseven", "n_clicks")],
    [State("modalseven", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open



# For all sliders
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


# the same function (toggle_navbar_collapse) is used in all three callbacks
for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)



if __name__ == "__main__":
    app.run_server()