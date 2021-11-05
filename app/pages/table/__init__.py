from dash import html

layout = html.Div([
    html.Button('Submit', id='button', n_clicks=0),
    html.Div(id='table')
])
