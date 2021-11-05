from dash import html, dcc
import visdcc
from friss.network.pages.network.data import nodes, edges

# TODO: check out cryospace?
layout = html.Div([
    visdcc.Network(id='net',
                   data={'nodes': nodes, 'edges': edges},
                   options=dict(height='800', width='100%')),
    # dcc.Input(id='label',
    #           placeholder='Enter a label ...',
    #           type='text',
    #           value=''),
    # html.Br(), html.Br(),
    # dcc.RadioItems(id='color',
    #                options=[{'label': 'Red', 'value': '#ff0000'},
    #                         {'label': 'Green', 'value': '#00ff00'},
    #                         {'label': 'Blue', 'value': '#0000ff'}],
    #                value='Red')
])
