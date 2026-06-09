import dash
from dash import html, dcc

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Sample Dashboard'),
    dcc.Graph(
        id='sample-graph',
        figure={
            'data': [{
                'x': [1, 2, 3, 4],
                'y': [10, 15, 13, 17],
                'type': 'line',
                'name': 'Sample Data'
            }],
            'layout': {
                'title': 'Sample Line Chart'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)