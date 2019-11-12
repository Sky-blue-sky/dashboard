import dash
from dash.dependencies import Input, Output, State
import dash_table
import dash_html_components as html
import pandas as pd

data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}
df_1 = pd.DataFrame(data)

app = dash.Dash(__name__)

app.layout = app.layout = html.Div([
    dash_table.DataTable(
        id='table-one',
        columns=[
            {"name": i, "id": i, 'editable':False} for i in df_1.columns  
        ],
        data=df_1.to_dict("rows")),
        
    html.Hr(),
    html.Div(id='changed-cell'),
    html.Div(id='selected-letter'),  # intermediate variable, will have style={'display': 'none'}
    html.Button(id='save-button', n_clicks=0, children='Save'),
    ])

@app.callback(Output('changed-cell', 'children'),
              [Input('table-one', 'active_cell'),
               Input('table-one', 'data')])
def get_active_letter(active_cell, data):
    if active_cell:
        
        return active_cell["row"]

@app.callback(Output('selected-letter', 'children'),
              [Input('save-button', 'n_clicks')],
              [State('table-one', 'active_cell'),
               State('table-one', 'data')])
def get_active_digit(n_clicks, active_cell, data):
    if active_cell and data:
        return active_cell['row']

if __name__ == '__main__':
    app.run_server(debug=True)