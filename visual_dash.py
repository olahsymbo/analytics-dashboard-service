#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import inspect
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
            'background': '#9KDBFF',             #'#9KDBFF'
            'div_bg': 'e2ecfb',
            'text': '#000000'
         }

divBorder = {
             'border': '0.8px outset grey',
             'border-radius': '5px'
            }
     
app.layout = html.Div(style={'backgroundColor': colors['background'], 
                             "margin": "auto"}, children=[
        
#    html.Div([
#        html.H1(
#            children='Firebase Data',
#            style={'textAlign': "center", "margin": "10px", "padding": "0px", 
#                   "font-family":"Courier New, monospace", "fontColor":"#F5E5E5"}),
#            ],
#            style={'backgroundColor':'#10166c'},            
#            ),
    html.Br(), 
    
    html.Div([
            dcc.DatePickerRange(
                id='my-date-picker-range',
                min_date_allowed=dt(2018, 10, 31),
                max_date_allowed=dt(2021, 12, 31),
                initial_visible_month=dt(2019, 8, 1),
                end_date=None),
    html.Div(id='output-container-date-picker-range')]),
    
    html.Br(),
    html.Br(),
    
############################################################################### 

    
    html.Div([  
        dbc.Row([
#### Country Details
                dbc.Col(html.Div([ 
                    dcc.Graph(
                    id='Country Details',
                    figure={
                        'data': [go.Bar(x=Index_country_df.geo_country, 
                                    y=Index_country_df.user_id,
                                    )],
                                'layout': { 
                                    'plot_bgcolor': colors['div_bg'],
                                    'paper_bgcolor': colors['div_bg'], 
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
                                    'tickangle':'45'
                                    },
                                }
                            },
                        ),
                    ],style={'backgroundColor':colors['div_bg'], 
                         'border':divBorder['border'],
                         'border-radius':divBorder['border-radius']
                         }),
                ),
    
#### City Details
        dbc.Col(html.Div([ 
            dcc.Graph(
            id='City Details',
            figure={
                'data': [go.Bar(x=Index_city_df.geo_city, 
                                y=Index_city_df.user_id, 
                                )],
                        'layout': { 
                            'plot_bgcolor': colors['div_bg'],
                            'paper_bgcolor': colors['div_bg'], 
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
                                'tickangle':'45'
                                },
                        }
                    },
                ),
            ],style={'backgroundColor':colors['div_bg'], 
                     'border':divBorder['border'],
                     'border-radius':divBorder['border-radius']
                     }),
            ), 
    
            ]),
        ]),
        html.Br(),
        html.Br(),

############################################################################### 
    
    html.Div([  
        dbc.Row([
            
#### OS Details
                dbc.Col(html.Div([ 
                    dcc.Graph(
                    id='OS',
                    figure={
                        'data': [go.Pie(labels=Index_OS_df.platform, 
                                        values=Index_OS_df.user_id)],
                                'layout': { 
                                    'plot_bgcolor': colors['div_bg'],
                                    'paper_bgcolor': colors['div_bg'], 
                                    'title': "OS",
                                    'font': {
                                        'color': colors['text']
                                            } 
                                        }
                                    },
                            ),   
                        ],style={'backgroundColor':colors['div_bg'], 
                         'border':divBorder['border'],
                         'border-radius':divBorder['border-radius']
                         }),
                    ),
    
#### Brand Name Details
                dbc.Col(html.Div([ 
                    dcc.Graph(
                    id='Brand Name',
                    figure={
                        'data': [go.Pie(labels=Index_brand_df.brand_name, 
                                        values=Index_brand_df.user_id)],
                                'layout': { 
                                    'plot_bgcolor': colors['div_bg'],
                                    'paper_bgcolor': colors['div_bg'],  
                                    'title': "Brand Name",
                                    'font': {
                                        'color': colors['text']
                                            } 
                                        }
                                    },
                            ),   
                        ],style={'backgroundColor':colors['div_bg'], 
                         'border':divBorder['border'],
                         'border-radius':divBorder['border-radius']
                         }),
                    ),
    
                ]),
            ]),
            html.Br(),
            html.Br(),


############################################################################### 
            
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
                                    'margin':go.layout.Margin(l=150, r=0, b=40,
                                                              t=100, pad=5),
                                    'plot_bgcolor': colors['div_bg'],
                                    'paper_bgcolor': colors['div_bg'],
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
                ],style={'backgroundColor':colors['div_bg'], 
                         'border':divBorder['border'],
                         'border-radius':divBorder['border-radius']
                         }),
                ), 
    
#### Users Details
                dbc.Col(html.Div([ 
                    dcc.Graph(
                    id='Users Details',
                    figure={
                        'data': [go.Bar(x=Index_User_df.event_name, 
                                        y=Index_User_df.user_id,
                                    orientation='h')],
                                'layout': {  
                                    'margin':go.layout.Margin(l=150, r=0, b=40,
                                                              t=100, pad=5),
                                    'plot_bgcolor': colors['div_bg'],
                                    'paper_bgcolor': colors['div_bg'], 
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
                ],style={'backgroundColor':colors['div_bg'], 
                         'border':divBorder['border'],
                         'border-radius':divBorder['border-radius']
                         }),
                ),
    

            ]),
        ]),
        html.Br(),
        html.Br(),
    
############################################################################### 
    
    html.Div([  
        dbc.Row([
#### Event Time for Users
                dbc.Col(html.Div([ 
                    dcc.Graph(
                    id='Event Time for Users',
                    figure={
                        'data': [go.Bar(y=Index_event_time_df.user_id, 
                                        x=Index_event_time_df.event_diff,
                                    orientation='h')],
                                'layout': { 
                                    'margin':go.layout.Margin(l=150, r=0, b=50,
                                                              t=100, pad=5),
                                    'plot_bgcolor': colors['div_bg'],
                                    'paper_bgcolor': colors['div_bg'], 
                                    'title': "Event Time for Users",
                                    'font': {
                                        'color': colors['text']
                                    }, 
                                'yaxis': {
                                        'automargin': False, 
                                        'title': "User ID"
                                      },
                                 'xaxis': {
                                        'automargin': 'true', 
                                        'title': "Time"
                                      },
                                }
                            },
                        ),   
                        ],style={'backgroundColor':colors['div_bg'], 
                         'border':divBorder['border'],
                         'border-radius':divBorder['border-radius']
                         }),
                    ),
                                    
#### Event Traffic Details
                dbc.Col(html.Div([ 
                    dcc.Graph(
                    id='Event Traffic per day',
                    figure={
                        'data': [go.Scatter(x=Index_event_date_df.event_date, 
                                            y=Index_event_date_df.counts)],
                                'layout': { 
#                                    'margin':go.layout.Margin(l=150, r=0, b=50, t=100, pad=5),
                                    'plot_bgcolor': colors['div_bg'],
                                    'paper_bgcolor': colors['div_bg'], 
                                    'title': "Daily Event Traffic",
                                    'font': {
                                        'color': colors['text']
                                            },
                                    'yaxis': {
                                        'automargin': 'true', 
                                        'title': "Counts",
                                        'tickmode': 'linear',
                                        'nticks': Index_event_date_df.counts.max() + 1000,
                                        'tick0': 0,
                                        'dtick': (Index_event_date_df.counts.max() - Index_event_date_df.counts.min())//2
                                      },
                                    'xaxis': {
                                        'automargin': 'true', 
                                        'title': "Days",
                                        'tickformat': '%Y%m%d', 
                                        'nticks': Index_event_date_df.event_date.max(),
                                        'tick0': Index_event_date_df.counts.min()
                                            },
                                         }
                                        
                                    },
                            ),   
                        ],style={'backgroundColor':colors['div_bg'], 
                         'border':divBorder['border'],
                         'border-radius':divBorder['border-radius']
                         }),
                    ),
    
                ]),
            ]),
            
        html.Br(),
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


#from google.cloud import bigquery
##from bq_helper import BigQueryHelper
#from google.oauth2 import service_account
#from datetime import date, timedelta
#previous_date = date.today() - timedelta(days=5)
#app_path = inspect.getfile(inspect.currentframe())
#dash_dir = os.path.realpath(os.path.dirname(app_path))
#     
    
#@app.callback(
#        dash.dependencies.Output('','value'),
#        [dash.dependencies.Input('','start_date'),
#        dash.dependencies.Input('','end_date')])
#    
#def date_data():
#    
#    credentials = service_account.Credentials.from_service_account_file(
#            os.path.join(dash_dir, "config/clane-8d862-fa96872fe9cb.json"))
#    
#    project_id = "clane-8d862"
#    client = bigquery.Client(credentials= credentials, project=project_id)
#    
#    start = previous_date.strftime("%Y%m%d")
#    end = date.today().strftime("%Y%m%d")
#    
#    
#    QUERY = """
#    SELECT * FROM  `clane-8d862.analytics_183730768.events_*` 
#    where REPLACE(_TABLE_SUFFIX, "_", "-")
#          BETWEEN {0} AND {1}
#          """.format('"%s"' % start, '"%s"' % end)
#        
#    query_job = client.query(QUERY)
#    
#    results = query_job.result()  # Waits for job to complete.
#    print("firebase data loaded")
#    
#    datan = list(query_job.result(timeout=30))
#     
#    df = pd.DataFrame(data=[list(x.values()) for x in datan], 
#                            columns=list(datan[0].keys()))
#    
#    return df, results
        
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
