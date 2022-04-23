#Done by Jason and Khizar
import dash
import pandas_datareader.data as dat
import datetime
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div(children=[


    html.Div(children='''
        Please enter a valid stock symbol.
    '''),

    dcc.Input(id='input', value ='', type='text'),

    html.Div(id='output-graph')
])

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)

def update_graph(input_data):
    start = datetime.datetime(2020, 1, 1)
    end = datetime.datetime.now()
    df = dat.DataReader(input_data, 'yahoo', start, end)
    df.reset_index(inplace=True)
    df.set_index("Date", inplace=True)
    # df = df.drop("Symbol", axis=1)    #unknown error

    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df.Close, 'type': 'line', 'name': input_data},
            ],
            'layout': {
                'title': input_data
            }
        }
    )

if __name__ == '__main__':
    app.run_server(debug=True)