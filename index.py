import os
import inspect
app_path = inspect.getfile(inspect.currentframe())
dash_dir = os.path.realpath(os.path.dirname(app_path))
 
import base64 
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash_app import app
from pages import news, visual_dash
from dashboard_firebase import *
import logging

colors = {
            'background': '#f5f6f7',
            'div_bg': '#9KDBFF',
            'text': '#000000'
         }

divBorder = {
             'border': '1px outset white',
             'border-radius': '5px'
            }

encoded_image = base64.b64encode(open(os.path.join(dash_dir, "img/image.png"), 'rb').read())

app.layout = html.Div([
    # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False), 
    html.Div(id='page-content')
])


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/visual_dash':
         return visual_dash.layout    
    elif pathname == '/news':
         return news.layout
    elif pathname == '/':
         return news.layout
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True, port=8090)