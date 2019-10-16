#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import inspect
app_path = inspect.getfile(inspect.currentframe())
dash_dir = os.path.realpath(os.path.dirname(app_path))

from datetime import datetime as dt 
import base64 
import dash
import dash_core_components as dcc
import dash_html_components as html 
from app import app
from pages import home, visual_dash, visual_interactions 
import dash_bootstrap_components as dbc 
from dashboard_firebase import *
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
#client = db_config(dash_dir)
#
#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUMEN])
#app.config.suppress_callback_exceptions = True

colors = {
            'background': '#f5f6f7',             #'#9KDBFF'
            'div_bg': '#9KDBFF',    ##e2ecfb
            'text': '#000000'
         }

divBorder = {
             'border': '1px outset white',
             'border-radius': '5px'
            }

encoded_image = base64.b64encode(open(os.path.join(dash_dir, "img/clane.png"), 'rb').read())

app.layout = html.Div([
    # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False), 
    html.Div(id='page-content')
])

#app.layout = html.Div(style={'backgroundColor': colors['background'], 
#                             "margin": "auto", "overflow": "auto"}, children=[
#        
#    html.Div([
#        dbc.Row([ 
#        
#        dbc.Col(
#        html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
#                style={'textAlign': "left", 
#                   'height' : '65%',
#                   'width' : '25%',  
#                   'padding-top' : 0,
#                   'padding-right' : 0, 
#                   "line-height":"1",
#                   "margin-bottom": "0.75rem",
#                   "margin-left": "0.45rem",
#                   "margin-top": "0.75rem",
#                   "fontColor":"#515151" 
#                   }
#                ),
#            ),
#        
#        dbc.Col(  
#            dcc.Location(id='url', refresh=False), 
#            html.Br(),
#            dcc.Link('Firebase', href='/visual_dash'), 
#            html.Br(),
#            dcc.Link('Interactions', href='/visual_interactions'),
#            html.Div(id='page-content')
##            html.Nav(className = "nav nav-pills", children=[
##            html.A('Firebase DB', className="nav-item nav-link active btn", 
##                   href= os.path.join(dash_dir, '/visual_dash')),
##            html.A('Interactions', className="nav-item nav-link btn", 
##                   href= os.path.join(dash_dir, '/visual_interactions'))
##                    ],
##            style={'textAlign': "right", 
##                   "margin": "1px", 
##                   "float":"right",
##                   "padding": "0px", 
##                   "font-family":"Helvetica Neue, Helvetica, Arial", 
##                   "font-size":"2rem", 
##                   "fontWeight": "bold", 
##                   "line-height":"1",
##                   "margin-bottom": "0.75rem",
##                   "margin-top": "0.80rem",
##                   "fontColor":"#515151" 
##                   }
##            ),
#            ),
#            
#            ]),
#            ],
#            style={'backgroundColor':'#fcfcfc'},            
#            ),
#    html.Br(), 
#    
#    html.Div([
#            dcc.DatePickerRange(
#                id='my-date-picker-range',
#                min_date_allowed=dt(2018, 10, 31),
#                max_date_allowed=dt(2021, 12, 31),
#                initial_visible_month=dt(2019, 8, 1),
#                start_date=dt(2019, 8, 28),
#                end_date=dt(2019, 8, 30)),
#    html.Div(id='output-container-date-picker-range'),
#    dcc.Loading(
#    html.Div(id='Intermediate-Details', style={'display': 'none'}), type="circle"),    
#    ]),
#    
#    html.Br(),
#    html.Br(),
#    
#])
    
    
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
         return home.layout
    elif pathname == '/visual_dash':
         return visual_dash.layout
    elif pathname == '/visual_interactions':
         return visual_interactions.layout
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)