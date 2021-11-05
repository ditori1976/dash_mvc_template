from dash.dependencies import Input, Output
from friss.network.app import app
from friss.network.pages.network import layout as network_layout


@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def render_page_content(pathname):
    if pathname == '/':
        return network_layout
    elif pathname == '/home':
        return 'home'
