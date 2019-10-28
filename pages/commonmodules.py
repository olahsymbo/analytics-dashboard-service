#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import inspect
app_path = inspect.getfile(inspect.currentframe())
dash_dir = os.path.realpath(os.path.dirname(app_path))
dir_path = os.path.dirname(dash_dir)

import dash_core_components as dcc
import dash_html_components as html
import base64  

encoded_image = base64.b64encode(open(os.path.join(dir_path, "img/clane.png"), 'rb').read())

def get_header():
    header = html.Div([ 
        
        html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
                style={'textAlign': "left", 
                   'height' : '25%',
                   'width' : '12%',  
                   'padding-top' : 0,
                   'padding-right' : 0, 
                   "line-height":"1",
                   "margin-bottom": "0.85rem",
                   "margin-left": "1.25rem",
                   "margin-top": "0.75rem",
                   "fontColor":"#515151" 
                   }
                ), 
        html.H6('ANALYTICS',
                style={ 
                  "font-weight": "bold",
                   "margin-top": "2.45rem",
                   "margin-left": "0.25rem",
                   'padding-right' : 0, 
                   "line-height":"1",
                   "fontColor":"#B65151" 
                   }),
        html.Br(),
        html.Br()

    ], className="row gs-header gs-text-header")
    return header

def get_menu():
#    tab_style={
#        'margin':5
#        }
    
    menu = html.Div([ 
        
        dcc.Link('Firebase   ', href='/visual_dash', className="p-2 text-dark"),
        dcc.Link('News   ', href='/news', className="p-2 text-dark"),
#        dcc.Link('Interactions   ', href='/visual_interactions', className="p-2 text-dark"), 

    ], className="d-flex flex-column flex-md-row align-items-center p-1 px-md-4 mb-3 bg-white border-bottom ")
    return menu    
