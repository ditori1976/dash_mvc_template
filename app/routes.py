from dash.dependencies import Input, Output
from app.app import app
from app.pages.home import layout as home_layout
from app.pages.admin import layout as admin_layout
from app.pages.table import layout as table_layout


@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def render_page_content(pathname):
    if pathname in (['/', '/home']):
        return home_layout
    elif pathname == '/admin':
        return admin_layout
    elif pathname == '/table':
        return table_layout
