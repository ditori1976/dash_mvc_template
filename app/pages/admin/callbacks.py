# from dash.dependencies import Input, Output, State

# @app.callback(
#     Output('net', 'data'),
#     [Input('label', 'value')])
# def myfun(x):
#     data = {'nodes': [{'id': 1, 'label': x, 'color': '#00ffff'},
#                       {'id': 2, 'label': 'Node 2'},
#                       {'id': 4, 'label': 'Node 4'},
#                       {'id': 5, 'label': 'Node 5'},
#                       {'id': 6, 'label': 'Node 6'}],
#             'edges': [{'id': '1-3', 'from': 1, 'to': 3},
#                       {'id': '1-2', 'from': 1, 'to': 2}]
#             }
#     return data


# @app.callback(
#     Output('net', 'options'),
#     [Input('color', 'value')])
# def myfun(x):
#     return {'nodes': {'color': x}}
