#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import inspect
from datetime import datetime as dt
from datetime import date
import base64
import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go  
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
from google.cloud import bigquery
#from bq_helper import BigQueryHelper
from google.oauth2 import service_account
from datetime import date, timedelta
previous_date = date.today() - timedelta(days=5)
app_path = inspect.getfile(inspect.currentframe())
dash_dir = os.path.realpath(os.path.dirname(app_path))


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


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUMEN])

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

app.layout = html.Div(style={'backgroundColor': colors['background'], 
                             "margin": "auto"}, children=[
        
    html.Div([
        dbc.Row([ 
        
        dbc.Col(
        html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
                style={'textAlign': "left", 
                   'height' : '65%',
                   'width' : '25%',  
                   'padding-top' : 0,
                   'padding-right' : 0, 
                   "line-height":"1",
                   "margin-bottom": "0.75rem",
                   "margin-left": "0.35rem",
                   "margin-top": "0.75rem",
                   "fontColor":"#515151" 
                   }
                ),
            ),
        
        dbc.Col(
        html.H6(
            children='Firebase Data',
            style={'textAlign': "right", 
                   "margin": "12px", 
                   "padding": "0px", 
                   "font-family":"Helvetica Neue, Helvetica, Arial", 
                   "font-size":"2rem", 
                   "fontWeight": "bold", 
                   "line-height":"1",
                   "margin-bottom": "0.75rem",
                   "margin-top": "0.75rem",
                   "fontColor":"#515151" 
                   }
                ),
            ),
            
            ]),
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
                start_date=dt(2019, 8, 29),
                end_date=dt(2019, 8, 30)),
    html.Div(id='output-container-date-picker-range')]),
    
    html.Br(),
    html.Br(),
    
############################################################################### 

    
    html.Div([  
        dbc.Row([
#### Country Details
    
                dbc.Col(html.Div([ 
                    dcc.Loading(
                    dcc.Graph(
                    id='Country-Details')
                    ),
                    ],style={'backgroundColor':colors['div_bg'], 
                         'border':divBorder['border'],
                         'border-radius':divBorder['border-radius']
                         }),
                    ),

#### City Details
        dbc.Col(html.Div([ 
                    dcc.Loading(
                    dcc.Graph(
                    id='City-Details')
                    ),
                    ],style={'backgroundColor':colors['div_bg'], 
                         'border':divBorder['border'],
                         'border-radius':divBorder['border-radius']
                         }),
                    ),
            ]),
        ]),

        html.Br(), 
    
    html.Div([  
        dbc.Row([
#### OS Details
    
                dbc.Col(html.Div([ 
                    dcc.Loading(
                    dcc.Graph(
                    id='OS-Details')
                    ),
                    ],style={'backgroundColor':colors['div_bg'], 
                         'border':divBorder['border'],
                         'border-radius':divBorder['border-radius']
                         }),
                    ),

#### Brand Details
        dbc.Col(html.Div([ 
                    dcc.Loading(
                    dcc.Graph(
                    id='Brand-Details')
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

    ], 
    className = "container")
 
    
@app.callback(
        dash.dependencies.Output('Country-Details','figure'),
        [dash.dependencies.Input('my-date-picker-range', 'start_date'),
        dash.dependencies.Input('my-date-picker-range', 'end_date')])
    
def country_data(start_date, end_date):
    
    credentials = service_account.Credentials.from_service_account_file(
            os.path.join(dash_dir, "config/clane-8d862-fa96872fe9cb.json"))
    
    project_id = "clane-8d862"
    client = bigquery.Client(credentials= credentials, project=project_id)
    
    start = dt.strptime(start_date[:10], '%Y-%m-%d').strftime("%Y%m%d")
    
    end = dt.strptime(end_date[:10], '%Y-%m-%d').strftime("%Y%m%d")
    
    QUERY = """
    SELECT * FROM  `clane-8d862.analytics_183730768.events_*` 
    where REPLACE(_TABLE_SUFFIX, "_", "-")
          BETWEEN {0} AND {1}
          """.format('"%s"' % start, '"%s"' % end)
        
    query_job = client.query(QUERY)
    
    results = query_job.result()  # Waits for job to complete.
    print("firebase data loaded")
    
    datan = list(query_job.result(timeout=30))
     
    df = pd.DataFrame(data=[list(x.values()) for x in datan], 
                            columns=list(datan[0].keys()))
    
    data = df
    app_dmat = []
    for row in range(len(data)):
        
        user_id = data.loc[row]['user_pseudo_id']
        geo_country = data.loc[row]['geo']['country']
        
        app_dmat.append([user_id, geo_country])
    
    colums = ['user_id',  'geo_country' ]
     
    
    app_dmat_df = pd.DataFrame(app_dmat, columns = colums)  
    enc_dmat = app_dmat_df
       
    
    Enc_country = enc_dmat.groupby('geo_country')['user_id'].count() \
                                                .sort_values(ascending=False) 
    country_df = pd.DataFrame(Enc_country) 
    Index_country_df = country_df.reset_index()
    
    data = plotly.graph_objs.Bar(
            x=Index_country_df.geo_country,
            y=Index_country_df.user_id,
            name='Countries' 
            )
    
    return {'data': [data],'layout' : go.Layout(xaxis=dict(automargin = True, tickangle=45),
                                                yaxis=dict(title = 'Counts')
                                                )}

    
    
@app.callback(
        dash.dependencies.Output('City-Details','figure'),
        [dash.dependencies.Input('my-date-picker-range', 'start_date'),
        dash.dependencies.Input('my-date-picker-range', 'end_date')])
    
def city_data(start_date, end_date):
    
    credentials = service_account.Credentials.from_service_account_file(
            os.path.join(dash_dir, "config/clane-8d862-fa96872fe9cb.json"))
    
    project_id = "clane-8d862"
    client = bigquery.Client(credentials= credentials, project=project_id)
    
    start = dt.strptime(start_date[:10], '%Y-%m-%d').strftime("%Y%m%d")
    
    end = dt.strptime(end_date[:10], '%Y-%m-%d').strftime("%Y%m%d")
    
    QUERY = """
    SELECT * FROM  `clane-8d862.analytics_183730768.events_*` 
    where REPLACE(_TABLE_SUFFIX, "_", "-")
          BETWEEN {0} AND {1}
          """.format('"%s"' % start, '"%s"' % end)
        
    query_job = client.query(QUERY)
    
    results = query_job.result()  # Waits for job to complete.
    
    datan = list(query_job.result(timeout=30))
     
    df = pd.DataFrame(data=[list(x.values()) for x in datan], 
                            columns=list(datan[0].keys()))
    
    data = df
    app_dmat = []
    for row in range(len(data)):
        
        user_id = data.loc[row]['user_pseudo_id']
        geo_city = data.loc[row]['geo']['city']
        
        app_dmat.append([user_id, geo_city])
    
    colums = ['user_id',  'geo_city' ]
     
    
    app_dmat_df = pd.DataFrame(app_dmat, columns = colums)  
    enc_dmat = app_dmat_df
       
    
    Enc_city = enc_dmat.groupby('geo_city')['user_id'].count() \
                                                .sort_values(ascending=False) 
    city_df = pd.DataFrame(Enc_city) 
    Index_city_df = city_df.reset_index()
    
    data = plotly.graph_objs.Bar(
            x=Index_city_df.geo_city,
            y=Index_city_df.user_id,
            name='Cities' 
            )
    
    return {'data': [data],'layout' : go.Layout(xaxis=dict(automargin = True, tickangle=45),
                                                yaxis=dict(title = 'Counts')
                                                )}
    
    
    
@app.callback(
        dash.dependencies.Output('OS-Details','figure'),
        [dash.dependencies.Input('my-date-picker-range', 'start_date'),
        dash.dependencies.Input('my-date-picker-range', 'end_date')])
    
def os_data(start_date, end_date):
    
    credentials = service_account.Credentials.from_service_account_file(
            os.path.join(dash_dir, "config/clane-8d862-fa96872fe9cb.json"))
    
    project_id = "clane-8d862"
    client = bigquery.Client(credentials= credentials, project=project_id)
    
    start = dt.strptime(start_date[:10], '%Y-%m-%d').strftime("%Y%m%d")
    
    end = dt.strptime(end_date[:10], '%Y-%m-%d').strftime("%Y%m%d")
    
    QUERY = """
    SELECT * FROM  `clane-8d862.analytics_183730768.events_*` 
    where REPLACE(_TABLE_SUFFIX, "_", "-")
          BETWEEN {0} AND {1}
          """.format('"%s"' % start, '"%s"' % end)
        
    query_job = client.query(QUERY)
    
    results = query_job.result()  # Waits for job to complete.
    
    datan = list(query_job.result(timeout=30))
     
    df = pd.DataFrame(data=[list(x.values()) for x in datan], 
                            columns=list(datan[0].keys()))
    
    data = df
    app_dmat = []
    for row in range(len(data)):
        
        user_id = data.loc[row]['user_pseudo_id']
        platform = data.loc[row]['platform']
        
        app_dmat.append([user_id, platform])
    
    colums = ['user_id',  'platform' ]
     
    
    app_dmat_df = pd.DataFrame(app_dmat, columns = colums)  
    enc_dmat = app_dmat_df
       
    
    Enc_OS = enc_dmat.groupby('platform')['user_id'].count() 
    OS_df = pd.DataFrame(Enc_OS) 
    Index_OS_df = OS_df.reset_index() 
    
    data = plotly.graph_objs.Pie(labels=Index_OS_df.platform, 
                                 values=Index_OS_df.user_id, 
            name='OS' 
            )
    
    return {'data': [data],'layout' : go.Layout(xaxis=dict(automargin = True),
                                                yaxis=dict(title = 'Counts')
                                                )}
    
@app.callback(
    dash.dependencies.Output('Brand-Details','figure'),
    [dash.dependencies.Input('my-date-picker-range', 'start_date'),
    dash.dependencies.Input('my-date-picker-range', 'end_date')])
    
def brand_data(start_date, end_date):
    
    credentials = service_account.Credentials.from_service_account_file(
            os.path.join(dash_dir, "config/clane-8d862-fa96872fe9cb.json"))
    
    project_id = "clane-8d862"
    client = bigquery.Client(credentials= credentials, project=project_id)
    
    start = dt.strptime(start_date[:10], '%Y-%m-%d').strftime("%Y%m%d")
    
    end = dt.strptime(end_date[:10], '%Y-%m-%d').strftime("%Y%m%d")
    
    QUERY = """
    SELECT * FROM  `clane-8d862.analytics_183730768.events_*` 
    where REPLACE(_TABLE_SUFFIX, "_", "-")
          BETWEEN {0} AND {1}
          """.format('"%s"' % start, '"%s"' % end)
        
    query_job = client.query(QUERY)
    
    results = query_job.result()  # Waits for job to complete.
    
    datan = list(query_job.result(timeout=30))
     
    df = pd.DataFrame(data=[list(x.values()) for x in datan], 
                            columns=list(datan[0].keys()))
    
    data = df
    app_dmat = []
    for row in range(len(data)):
        
        user_id = data.loc[row]['user_pseudo_id']
        brand_name = data.loc[row]['device']['mobile_brand_name']
        
        app_dmat.append([user_id, brand_name])
    
    colums = ['user_id',  'brand_name' ]
     
    
    app_dmat_df = pd.DataFrame(app_dmat, columns = colums)  
    enc_dmat = app_dmat_df
       
    
    Enc_brand = enc_dmat.groupby('brand_name')['user_id'].count() 
    brand_df = pd.DataFrame(Enc_brand) 
    Index_brand_df = brand_df.reset_index() 
    
    data = plotly.graph_objs.Pie(labels=Index_brand_df.brand_name, 
                                 values=Index_brand_df.user_id, 
            name='Phone Brand' 
            )
    
    return {'data': [data],'layout' : go.Layout(xaxis=dict(automargin = True, tickangle=45),
                                                yaxis=dict(title = 'Counts')
                                                )}
if __name__ == '__main__':
    app.run_server(debug=True)
    