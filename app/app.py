from dash import Dash
from app.layout import layout

app = Dash(
    __name__,
    suppress_callback_exceptions=True)

app.layout = layout
