#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 09:37:53 2019

@author: o.arigbabu
"""

from datetime import datetime as dt
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go 
from read_data import *
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

colors = {
            'background': '#9KDBFF',
            'text': '#000000'
         }
     
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    
    html.Div([
        html.H1(
            children='Firebase Data',
            style={'textAlign': "center", "margin": "30px", "padding": "10px", "width": "50%", "margin-left": "auto",
                    "margin-right": "auto", "font-family":"Courier New, monospace", "fontColor":"#7f7f7f"
            }),
            ],
            style={'backgroundColor':'#aeb0f5',
                  },
            
            ),

    html.Div([
    dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=dt(2018, 10, 31),
        max_date_allowed=dt(2021, 12, 31),
        initial_visible_month=dt(2019, 8, 1),
        end_date=None
                        ),
    html.Div(id='output-container-date-picker-range')
            ]),

    
#######################
###################### First Row 
#######################
    
    html.Div([  
        dbc.Row([
                dbc.Col(html.Div([ 
                    dcc.Graph(
                    id='Event Details',
                    figure={
                        'data': [go.Bar(x=Index_Event_df.user_id, 
                                    y=Index_Event_df.event_name,
                                    orientation='h')],
                                'layout': {  
                                    'margin':go.layout.Margin(
                                                        l=150,
                                                        r=0,
                                                        b=40,
                                                        t=100,
                                                        pad=5
                                                    ),
#                                    'margin':dict(
#                                                'l':50,
#                                                'r':50,
#                                                'b':100,
#                                                't':100,
#                                                'pad':4
#                                            ),
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'title': "Event Details",
                                    'font': {
                                        'color': colors['text']
                                    }, 
                                'yaxis': { 
                                        'automargin': False,  
                                        'title': 'Events'
                                      },
                                'xaxis': {
                                    'automargin': 'true', 
                                    'title': 'Counts'
                                    },
                                }
                            },
                        ),
                ]),
                ), 
    
##################### Users Details
                dbc.Col(html.Div([ 
                    dcc.Graph(
                    id='Users Details',
                    figure={
                        'data': [go.Bar(x=Index_User_df.event_name, 
                                        y=Index_User_df.user_id,
                                    orientation='h')],
                                'layout': {  
                                    'margin':go.layout.Margin(
                                                        l=150,
                                                        r=0,
                                                        b=40,
                                                        t=100,
                                                        pad=5
                                                    ),
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'], 
                                    'title': "Top Users",
                                    'font': {
                                        'color': colors['text']
                                    }, 
                                'yaxis': {
                                        'automargin': False,  
                                         'title': 'User ID'
                                      },
                                'xaxis': {
                                    'automargin': 'true', 
                                    'title': 'Counts'
                                    },
                                }
                            },
                        ),
                ]), 
                ),
    

        ]),
    ]),
    html.Br(),
    html.Br(),
    
#######################
###################### Second Row  
#######################
    
    html.Div([  
        dbc.Row([
##################### Country Details
                dbc.Col(html.Div([ 
                    dcc.Graph(
                    id='Country Details',
                    figure={
                        'data': [go.Bar(x=Index_country_df.geo_country, 
                                    y=Index_country_df.user_id,
                                    )],
                                'layout': { 
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'], 
                                    'title': "Countries",
                                    'font': {
                                        'color': colors['text']
                                    },
                                    'yaxis': {
                                        'automargin': 'true', 
                                        'title': "Counts"
                                      },
                                    'xaxis': {
                                    'automargin': 'true', 
                                    },
                                }
                            },
                        ),
                    ]), 
                ),
    
##################### City Details
        dbc.Col(html.Div([ 
            dcc.Graph(
            id='City Details',
            figure={
                'data': [go.Bar(x=Index_city_df.geo_city, 
                                y=Index_city_df.user_id, 
                                )],
                        'layout': { 
                            'plot_bgcolor': colors['background'],
                            'paper_bgcolor': colors['background'], 
                            'title': "Cities",
                            'font': {
                                'color': colors['text']
                            }, 
                        'yaxis': {
                                'automargin': 'true', 
                                'title': "Counts"
                              },
                        'xaxis': {
                                'automargin': 'true', 
                                },
                        }
                    },
                ),
        ]), 
        ), 
    
        ]),
    ]),
    html.Br(),
    html.Br(),

#######################
####################### Third Row
#######################
    
    html.Div([  
        dbc.Row([
            
                ##################### OS Details
                dbc.Col(html.Div([ 
                    dcc.Graph(
                    id='OS',
                    figure={
                        'data': [go.Pie(labels=Index_OS_df.platform, values=Index_OS_df.user_id)],
                                'layout': { 
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'], 
                                    'title': "OS",
                                    'font': {
                                        'color': colors['text']
                                            } 
                                        }
                                    },
                            ),   
                        ]),
                    ),
    
                ##################### Brand Name Details
                dbc.Col(html.Div([ 
                    dcc.Graph(
                    id='Brand Name',
                    figure={
                        'data': [go.Pie(labels=Index_brand_df.brand_name, values=Index_brand_df.user_id)],
                                'layout': { 
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'], 
                                    'title': "Brand Name",
                                    'font': {
                                        'color': colors['text']
                                            } 
                                        }
                                    },
                            ),   
                        ]),
                    ),
    
                ]),
            ]),
            html.Br(),
            html.Br(),

    
#######################
####################### Fourth Row
#######################
    
    html.Div([  
        dbc.Row([
    
##################### Event Time for Users
                dbc.Col(html.Div([ 
                    dcc.Graph(
                    id='Event Time for Users',
                    figure={
                        'data': [go.Bar(y=Index_event_time_df.user_id, 
                                        x=Index_event_time_df.event_diff,
                                    orientation='h')],
                                'layout': { 
                                    'margin':go.layout.Margin(
                                                        l=150,
                                                        r=0,
                                                        b=40,
                                                        t=100,
                                                        pad=5
                                                    ),
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'], 
                                    'title': "Event Time for Users",
                                    'font': {
                                        'color': colors['text']
                                    }, 
                                'yaxis': {
                                        'automargin': True, 
                                        'title': "User ID"
                                      },
                                 'xaxis': {
                                        'automargin': True, 
                                        'title': "Time"
                                      },
                                }
                            },
                        ),   
                        ]),
                    ),
    
        
                ##################### Event Traffic Details
                dbc.Col(html.Div([ 
                    dcc.Graph(
                    id='Event Traffic per day',
                    figure={
                        'data': [go.Scatter(x=Index_event_date_df.event_date, 
                                            y=Index_event_date_df.user_id)],
                                'layout': { 
                                    'margin':go.layout.Margin(
                                                        l=150,
                                                        r=0,
                                                        b=40,
                                                        t=100,
                                                        pad=5
                                                    ),
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'title': "Daily Event Traffic",
                                    'font': {
                                        'color': colors['text']
                                            },
                                    'yaxis': {
                                        'automargin': 'true', 
                                        'title': "Counts"
                                      },
                                 'xaxis': {
                                        'automargin': 'true', 
                                        'title': "Days"
                                            },
                                         }
                                        
                                    },
                            ),   
                        ]),
                    ),
    
                ]),
            ]),
            
    html.Br(),
    html.Br(),

    ], 
    className = "container")

@app.callback(
    dash.dependencies.Output('output-container-date-picker-range', 'children'),
    [dash.dependencies.Input('my-date-picker-range', 'start_date'),
     dash.dependencies.Input('my-date-picker-range', 'end_date')])

def update_output(start_date, end_date):
    string_prefix = 'You have selected: '
    if start_date is not None:
        start_date = dt.strptime(start_date, '%Y-%m-%d')
        start_date_string = start_date.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'Start Date: ' + start_date_string + ' | '
    if end_date is not None:
        end_date = dt.strptime(end_date, '%Y-%m-%d')
        end_date_string = end_date.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'End Date: ' + end_date_string
    if len(string_prefix) == len('You have selected: '):
        return 'Select a date to see it displayed here'
    else:
        return string_prefix
        
if __name__ == '__main__':
    app.run_server(debug=True)
    
    

#from datetime import timedelta, date
#
#def daterange(date1, date2):
#    for n in range(int ((date2 - date1).days)+1):
#        yield date1 + timedelta(n)
#
#start_dt = date(2015, 12, 20)
#end_dt = date(2016, 1, 11)
#for dt in daterange(start_dt, end_dt):
#    print(dt.strftime("%Y-%m-%d"))
