#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import inspect
app_path = inspect.getfile(inspect.currentframe())
dash_dir = os.path.realpath(os.path.dirname(app_path))

import dash_core_components as dcc
import dash_html_components as html
import base64 
from dash.dependencies import Input, Output

encoded_image = base64.b64encode(open(os.path.join("/Users/o.arigbabu/Clane-Code/clane-services-dashboard", "img/clane.png"), 'rb').read())

def get_header():
    header = html.Div([

#        html.Div([
#            html.H1(
#                'Clane DashBoard')
#        ], className="twelve columns padded"), 
        
        html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
                style={'textAlign': "left", 
                   'height' : '25%',
                   'width' : '12%',  
                   'padding-top' : 0,
                   'padding-right' : 0, 
                   "line-height":"1",
                   "margin-bottom": "0.85rem",
                   "margin-left": "1.01rem",
                   "margin-top": "0.75rem",
                   "fontColor":"#515151" 
                   }
                ), 
        html.Br(),
        html.Br()

    ], className="row gs-header gs-text-header")
    return header

def get_menu():
    menu = html.Div([

        dcc.Link('Home   ', href='/', className="p-2 text-dark"),
        dcc.Link('Firebase   ', href='/visual_dash', className="p-2 text-dark"),
        dcc.Link('Interactions   ', href='/visual_interactions', className="p-2 text-dark"), 

    ], className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm")
    return menu    
