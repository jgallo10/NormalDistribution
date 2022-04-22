
import dash 
import datetime
import pandas_datareader.data as dat
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

stock = 'AMZN'

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2018, 2, 8)

df = dat.DataReader(stock, 'yahoo', start, end)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
# df = df.drop("Symbol", axis=1)

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Amazon Stock Graph'),



    html.Div(children='''
        Getting Amazon stock data from yahoo
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df.Close, 'type': 'line', 'name': 'SF'},
            ],
            'layout': {
                'title': stock
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)