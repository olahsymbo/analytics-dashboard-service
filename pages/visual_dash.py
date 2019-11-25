#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import inspect
app_path = inspect.getfile(inspect.currentframe())
dash_dir = os.path.realpath(os.path.dirname(app_path))

from datetime import datetime as dt, timedelta
import base64
import pandas as pd
import numpy as np 
import dash 
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go   
from dash_app import app
from dashboard_firebase import *
from pages import commonmodules
import logging
#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR) 

client = db_config(dash_dir)
 
colors = {
            'background': '#f5f6f7',             #'#9KDBFF'
            'div_bg': '#9KDBFF',    ##e2ecfb
            'text': '#000000'
         }

divBorder = {
             'border': '1px outset white',
             'border-radius': '5px'
            }

def myconverter(o):
 if isinstance(o, dt):
    return o.__str__()

encoded_image = base64.b64encode(open(os.path.join(dash_dir, "img/clane.png"), 'rb').read())

layout = html.Div(style={'backgroundColor': colors['background'], 
                             "margin": "auto"}, children=[
        
            html.Div([
        
                    commonmodules.get_header(),
                    commonmodules.get_menu(),
                    ],
                    style={'backgroundColor':'#fcfcfc'},            
                    ), 
            html.Br(),
            
            html.Div([
                    dcc.DatePickerRange(
                        id='my-date-picker-range',
                        min_date_allowed=dt(2018, 10, 31),
                        max_date_allowed=dt(2021, 12, 31),
                        initial_visible_month=dt(2019, 8, 1),
                        start_date=dt.today() - timedelta(days=8),
                        end_date=dt.today() - timedelta(days=1)),
            html.Div(id='output-container-date-picker-range'),
            dcc.Loading(
            html.Div(id='Intermediate-Details', style={'display': 'none'}), type="circle"),   
            html.Div(id='Intermediate-Details1', style={'display': 'none'}),   
            html.Div(id='Intermediate-Details2', style={'display': 'none'}),  
            ]),
             
            html.Br(),

######################################################################  

            html.Div([    
                    
                    html.Div([ 
                            
                        #### User/Event Details  
                        html.Br(),
                        
                        html.Div(
                                [ 
                                html.P("App Users"),
                                html.H2(id = "Unique-Users",
                                        className = "info_text",
                                        style={'textAlign' : 'center', 
                                               'opacity': 7}
                                   ), 
                                ], style={'textAlign': 'center', 
                                          'fontSize': 15,  
                                          'font-family': 'Helvetica Neue, Helvetica, Arial'
                                        }
                            ),
                                        
                        html.Br(),
                        
                        html.Div(
                                [ 
                                html.P("Total Events"),
                                html.H2(id = "Total-Event-Details",
                                        className = "info_text" ,
                                        style={'textAlign' : 'center', 
                                               'opacity': 7
                                               }
                                        ), 
                                ], style={'textAlign': 'center',  
                                      'fontSize': 15,
                                      'font-family': 'Helvetica Neue, Helvetica, Arial' 
                                      }
                                ),
                         
                        html.Br(),
                        
                        html.Div(
                                [ 
                                html.P("Churn Rate"),
                                html.H2(id = "Churn-Number-Details",
                                        className = "info_text",
                                        style={'textAlign' : 'center', 
                                               'opacity': 7,
                                              }
                                        ), 
                                ], style={'textAlign': 'center', 
                                      'fontSize': 15, 
                                      'font-family': 'Helvetica Neue, Helvetica, Arial'
                                      }
                                ),
                        html.Br(),
                             ],style={'backgroundColor':'ffffff',
                             'border':divBorder['border'],
                             'border-radius':divBorder['border-radius'],
                             'display' : 'inline-block', 
                             'boxSizing' : 'border-box',
                             'float':'left',
                             'width' : '25%',
                             'box-shadow' : '2px 2px 2px lightgrey',
                             'position':'relative'
                             }),

                    #### Traffic Details        
                    html.Div([ 
                    dcc.Loading(
                    dcc.Graph(id='Traffic-Details')
                                ),
                            ],style={'backgroundColor':colors['div_bg'], 
                             'border':divBorder['border'],
                             'border-radius':divBorder['border-radius'],
                             'display' : 'inline-block', 
                             'boxSizing' : 'border-box',
                             'float':'right', 
                             'width' : '73%',
                             'box-shadow' : '2px 2px 2px lightgrey',
                             'position': 'relative'
                             }
                            ),
                    
                            ], style={'paddingBottom': '5', "overflow": "auto"}
                        ),
    
                    html.Br(), 
    
                    html.Div([  
                    #### Country Details 
                    html.Div([ 
                    dcc.Loading(
                    dcc.Graph(id='Country-Details')
                            ),
                            ],style={'backgroundColor':colors['div_bg'], 
                             'border':divBorder['border'],
                             'border-radius':divBorder['border-radius'], 
                             'display' : 'inline-block', 
                             'boxSizing' : 'border-box',
                             'float':'left',
                             'width' : '60%',
                             'box-shadow': '2px 2px 2px lightgrey',
                             'position': 'relative'
                             }),  

                    #### OS Details 
                    html.Div([ 
                    dcc.Loading(
                    dcc.Graph(id='OS-Details')
                                ),
                            ],style={'backgroundColor':colors['div_bg'], 
                                 'border':divBorder['border'],
                                 'border-radius':divBorder['border-radius'], 
                                 'display' : 'inline-block', 
                                 'boxSizing' : 'border-box',
                                 'float':'right',
                                 'width' : '38%',
                                 'box-shadow' : '2px 2px 2px lightgrey',
                                 'position': 'relative'
                                 }
                            ), 
                                ],
                                style={'paddingBottom' : '5', "overflow": "auto"}
                            ),

                    html.Br(),  
        
                    html.Div([   

                    #### Event Details 
                    html.Div([ 
                    dcc.Loading(
                    dcc.Graph(
                    id='Event-Details')
                    ),
                    ],style={'backgroundColor':colors['div_bg'], 
                         'border':divBorder['border'],
                         'border-radius':divBorder['border-radius'], 
                         'display' : 'inline-block', 
                         'boxSizing' : 'border-box',
                         'float':'left',
                         'width' : '60%',
                         'box-shadow' : '2px 2px 2px lightgrey',
                         'position': 'relative'
                         }), 
        
                    #### Mobile Brand
                    html.Div([ 
                    dcc.Loading(
                    dcc.Graph(id='Brand-Details')
                            ),
                            ],style={'backgroundColor':colors['div_bg'], 
                             'border':divBorder['border'],
                             'border-radius':divBorder['border-radius'], 
                             'display' : 'inline-block', 
                             'boxSizing' : 'border-box',
                             'float':'right',
                             'width' : '38%',
                             'box-shadow' : '2px 2px 2px lightgrey',
                             'position': 'relative'
                             }),
         
                            ],  
                            style={'paddingBottom' : '5', "overflow": "auto"}
                            ),
         
                    html.Br(),   
                    html.Br(), 
                                                        ], 
                                className = "container"
                )


############### DB Loader 
@app.callback(
        dash.dependencies.Output('Intermediate-Details','children'),
        [dash.dependencies.Input('my-date-picker-range', 'start_date'),
        dash.dependencies.Input('my-date-picker-range', 'end_date')])
    
def db_data(start_date, end_date):
    
    start = dt.strptime(start_date[:10], '%Y-%m-%d').strftime("%Y%m%d")
    
    end = dt.strptime(end_date[:10], '%Y-%m-%d').strftime("%Y%m%d")
    
    QUERY = """
    SELECT * FROM  `clane-8d862.analytics_183730768.events_*` 
    where REPLACE(_TABLE_SUFFIX, "_", "-")
          BETWEEN {0} AND {1}
          """.format('"%s"' % start, '"%s"' % end)
        
    query_job = client.query(QUERY)
#    print("firebase data loaded")
    
    datan = list(query_job.result(timeout=100))
     
    df = pd.DataFrame(data=[list(x.values()) for x in datan], columns=list(datan[0].keys()))
    datann = df
    
    return datann.to_json() 


############### Unique Users
@app.callback(
        dash.dependencies.Output('Unique-Users','children'),
        [dash.dependencies.Input('Intermediate-Details', 'n_intervals') ])
    
def user_data(datann):
    if datann is None:
        raise dash.exceptions.PreventUpdate
        
    datann = pd.read_json(datann)
    app_dmat = [] 
    for row in range(len(datann)):
        
        user_id = datann.loc[row]['user_pseudo_id'] 
        
        app_dmat.append([user_id])
    
    colums = ['user_id']
     
    
    app_dmat_df = pd.DataFrame(app_dmat, columns = colums)  
    enc_dmat = app_dmat_df
        
    Enc_users = enc_dmat['user_id'].nunique()
    
    return Enc_users 

############### Total Events
@app.callback(
        dash.dependencies.Output('Total-Event-Details','children'),
        [dash.dependencies.Input('Intermediate-Details', 'n_intervals') ])
    
def total_event_data(datann):
    if datann is None:
        raise dash.exceptions.PreventUpdate
        
    datann = pd.read_json(datann) 
    
    return datann.shape[0]

############### Churn Rate
@app.callback(
        dash.dependencies.Output('Churn-Number-Details','children'),
        [dash.dependencies.Input('Intermediate-Details', 'n_intervals') ])
    
def churn_number_data(datann):
    if datann is None:
        raise dash.exceptions.PreventUpdate
        
    datann = pd.read_json(datann) 
    
    app_dmat = [] 
    for row in range(len(datann)):
        
        user_id = datann.loc[row]['user_pseudo_id']
        event_date = datann.loc[row]['event_date']
        event_name = datann.loc[row]['event_name']
        
        app_dmat.append([user_id, event_date, event_name])
    
    colums = ['user_id',  'event_date', 'event_name']
    
    app_dmat_df = pd.DataFrame(app_dmat, columns = colums)  
    
    Enc_users = app_dmat_df['user_id'].nunique()
    
    app_remove = app_dmat_df[app_dmat_df['event_name'] == 'app_remove']
     
    churn_rate = ((app_remove.shape[0])/Enc_users)*100
    
    return '{0}%'.format((round(churn_rate,2))) 
 
############### Country Details
@app.callback(
        dash.dependencies.Output('Country-Details','figure'),
        [dash.dependencies.Input('Intermediate-Details', 'n_intervals') ])
    
def country_data(datann):
    
    if datann is None:
        raise dash.exceptions.PreventUpdate
        
    datann = pd.read_json(datann)
    app_dmat = [] 
    for row in range(len(datann)):
        
        user_id = datann.loc[row]['user_pseudo_id']
        geo_country = datann.loc[row]['geo']['country']
        
        app_dmat.append([user_id, geo_country])
    
    colums = ['user_id',  'geo_country' ]
     
    
    app_dmat_df = pd.DataFrame(app_dmat, columns = colums)  
    enc_dmat = app_dmat_df
       
    
    Enc_country = enc_dmat.groupby('geo_country')['user_id'].nunique().sort_values(ascending=False) 
    country_df = pd.DataFrame(Enc_country) 
    Index_country_df = country_df.reset_index()
    
    data = plotly.graph_objs.Bar(
            x=Index_country_df.geo_country,
            y=Index_country_df.user_id,
            name='Countries' 
            )
    
    return {'data': [data],
            'layout' : go.Layout(title=dict(
                                            text="<b>Countries</b>",
                                            ), 
                                            font=dict(size=10),
                                            height = 350,
                                            xaxis=dict(automargin = True, 
                                                       tickangle=45),
                                            yaxis=dict(title = 'Counts')
                                            )
            }
    
################ OS Details
@app.callback(
        dash.dependencies.Output('OS-Details','figure'),
        [dash.dependencies.Input('Intermediate-Details', 'children') ])
    
def os_data(datann):
    datann = pd.read_json(datann)
    app_dmat = [] 
    for row in range(len(datann)):
        
        user_id = datann.loc[row]['user_pseudo_id']
        platform = datann.loc[row]['platform']
        
        app_dmat.append([user_id, platform])
    
    colums = ['user_id',  'platform' ]
     
    
    app_dmat_df = pd.DataFrame(app_dmat, columns = colums)  
    enc_dmat = app_dmat_df
       
    
    Enc_OS = enc_dmat.groupby('platform')['user_id'].count() 
    OS_df = pd.DataFrame(Enc_OS) 
    Index_OS_df = OS_df.reset_index() 
    
    data = plotly.graph_objs.Pie(labels=Index_OS_df.platform, values=Index_OS_df.user_id, name='OS')
    
    return {'data': [data],
            'layout' : go.Layout(title=dict(
                                            text="<b>OS</b>",
                                            ), 
                                            font=dict( size=10),
                                            height = 350,
                                            xaxis=dict(automargin = True),
                                            yaxis=dict(title = 'Counts')
                                            )
            }
    
############ Event details    
@app.callback(
    dash.dependencies.Output('Event-Details','figure'),
        [dash.dependencies.Input('Intermediate-Details', 'children') ])
    
def event_data(datann):
    datann = pd.read_json(datann)
    app_dmat = [] 
    for row in range(len(datann)):
        
        user_id = datann.loc[row]['user_pseudo_id']
        event_name = datann.loc[row]['event_name']
        
        app_dmat.append([user_id, event_name])
    
    colums = ['user_id',  'event_name' ]
     
    
    app_dmat_df = pd.DataFrame(app_dmat, columns = colums)  
    enc_dmat = app_dmat_df
       
    
    Enc_events = enc_dmat.groupby('event_name')['user_id'].count().sort_values(ascending=True)
    Event_df = pd.DataFrame(Enc_events) 
    Index_Event_df = Event_df.reset_index()
    
    data = plotly.graph_objs.Bar(
            y=Index_Event_df.event_name,
            x=Index_Event_df.user_id,
            orientation='h',
            name='Events' 
            )
    
    return {'data': [data],
            'layout' : go.Layout(title=dict(
                                            text="<b>Events Usage</b>",
                                            ),
                                            font=dict(size=10),
                                            height = 350,
                                            margin = dict(l=200, r=50, b=50,
                                                          t=100, pad=5),
                                            xaxis=dict(automargin = True,
                                                        title = 'Counts'),
                                            yaxis=dict(
                                            tickfont=dict(size=10))
                                            )
            }


############ Brand Details
@app.callback(
    dash.dependencies.Output('Brand-Details','figure'),
    [dash.dependencies.Input('Intermediate-Details', 'children') ])
    
def brand_data(datann):
    datann = pd.read_json(datann) 
    app_dmat = []
    for row in range(len(datann)):
        
        user_id = datann.loc[row]['user_pseudo_id']
        brand_name = datann.loc[row]['device']['mobile_brand_name']
        
        app_dmat.append([user_id, brand_name])
    
    colums = ['user_id',  'brand_name' ]
     
    
    app_dmat_df = pd.DataFrame(app_dmat, columns = colums)  
    enc_dmat = app_dmat_df
       
    
    Enc_brand = enc_dmat.groupby('brand_name')['user_id'].count() 
    brand_df = pd.DataFrame(Enc_brand) 
    Index_brand_df = brand_df.reset_index() 
    
    data = plotly.graph_objs.Pie(labels=Index_brand_df.brand_name, values=Index_brand_df.user_id, 
                                                                             name='Phone Brand')
    
    return {'data': [data],
            'layout' : go.Layout(title=dict(
                                           text="<b>Mobile Brands</b>",
                                            ),
                                            height = 350,
                                            font=dict(size=10),
                                            xaxis=dict(automargin = True, 
                                                       tickangle=45),
                                            yaxis=dict(title = 'Counts')
                                            )
            }


############### Daily Traffic    
@app.callback(
        dash.dependencies.Output('Traffic-Details','figure'),
        [dash.dependencies.Input('Intermediate-Details', 'children') ])
    
def traffic_data(datann):
    datann = pd.read_json(datann)
    app_dmat = [] 
    for row in range(len(datann)):
        
        user_id = datann.loc[row]['user_pseudo_id']
        event_date = datann.loc[row]['event_date']
        
        app_dmat.append([user_id, event_date])
    
    colums = ['user_id',  'event_date' ]
     
    
    app_dmat_df = pd.DataFrame(app_dmat, columns = colums)  
    app_dmat_df['event_date'] =  pd.to_datetime(app_dmat_df['event_date'], 
               format='%Y%m%d')
    
    app_dmat_df['event_date'] = app_dmat_df['event_date'].dt.date
    enc_dmat = app_dmat_df
       
    
    Enc_event_date = enc_dmat.groupby('event_date').size() 
    event_date_df= pd.DataFrame(Enc_event_date) 
    Index_event_date_df = event_date_df.reset_index()
    Index_event_date_df.columns = ['event_date', 'counts']
    
    data = plotly.graph_objs.Scatter(x=Index_event_date_df.event_date, y=Index_event_date_df.counts)
    
    xmin, xmax = np.min(Index_event_date_df.event_date.to_numpy()), \
                        np.max(Index_event_date_df.event_date.to_numpy())
    
    return {'data': [data],
            'layout' : go.Layout(
                                title=dict(
                                text="<b>Daily Traffic</b>",
                                        ),
                                margin = dict(l=70, r=40, b=70,
                                                          t=50, pad=5),
                                height = 320,
                                font=dict( size=10), 
                                yaxis=dict(title = 'Counts',
                                           showgrid = False
                                           ),
                                xaxis=dict(automargin = True,  
                                title = 'Date',  
                                tickvals=[xmin, xmax]
                                    ),
                                    ),
            }   