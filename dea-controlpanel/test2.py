import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import boto3
import pandas as pd
from boto3.dynamodb.conditions import Key, Attr

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('OrchestrationJobStatus')

response = table.scan()
items = response['Items']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash (Boogedy)'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    # dash_table.DataTable(
    #     id='table',
    #     columns=[{"name": i, "id": i} for i in df.columns],
    #     data=df.to_dict('records'),
    #     sort_action='native',
    #     filter_action='native',
    # ),
    dash_table.DataTable(
        id='table',
        columns=[{"name": k, "id": k} for k in items[0].keys()],
        data=items,
        sort_action='native',
        filter_action='native',
    ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)