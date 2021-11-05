from dash.dependencies import Output, Input
from dash.dash_table import DataTable

from app.app import app
from app.pages.table.data import load_db


@app.callback(
    Output('table', 'children'),
    Input('button', 'n_clicks')
)
def create_table(table):
    df = load_db()

    return DataTable(
        id='data_table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
    )
