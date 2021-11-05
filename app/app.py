# %%
from pathlib import Path
# import networkx as nx

from dash import Dash
from friss.network.layout import layout

app = Dash()

app.layout = layout
