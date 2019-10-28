#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
import dash_html_components as html 
from pages import commonmodules 
import pandas as pd
import numpy as np
from app import app
from datetime import datetime as dt 
import plotly
import plotly.graph_objs as go  
import dash
import dash_table
import dash_core_components as dcc
from TableModels.Artc import Articles 
from TableModels.Intr import Interactions 
import json
 
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
                    start_date=dt(2019, 8, 28),
                    end_date=dt(2019, 8, 30)),
        html.Div(id='output-container-date-picker-range'),
        dcc.Loading(
        html.Div(id='Intermediate-Details', style={'display': 'none'}), 
                                                            type="circle"),   
        html.Div(id='Intermediate-Details1', style={'display': 'none'}),   
        html.Div(id='Intermediate-Details2', style={'display': 'none'}),  
        ]),
          
    html.Br(),
    
    html.Div([     
            html.Div([
#### unique liked articles
             html.Br(),
                        html.Div(
                                [ 
                                html.P("Rated Articles"),
                                html.H2(id = "Liked-Article",
                                        className = "info_text",
                                        style={'textAlign' : 'center', 
                                               'opacity': 1}
                                   ), 
                                ], style={'textAlign': 'center', 
                                          'fontSize': 15,  
                                          'font-family': 'Helvetica Neue, \
                                                      Helvetica, Arial'
                                        }
                            ),  

#### unique liked articles
             html.Br(),
                        html.Div(
                                [ 
                                html.P("Unique Users"),
                                html.H2(id = "Raters",
                                        className = "info_text",
                                        style={'textAlign' : 'center', 
                                               'opacity': 1}
                                   ), 
                                ], style={'textAlign': 'center', 
                                          'fontSize': 15,  
                                          'font-family': 'Helvetica Neue, \
                                                      Helvetica, Arial'
                                        }
                            ),  
            
#### unique liked articles
             html.Br(),
                        html.Div(
                                [ 
                                html.P("Total Interactions"),
                                html.H2(id = "Interactions-types",
                                        className = "info_text",
                                        style={'textAlign' : 'center', 
                                               'opacity': 1}
                                   ), 
                                ], style={'textAlign': 'center', 
                                          'fontSize': 15,  
                                          'font-family': 'Helvetica Neue, \
                                                      Helvetica, Arial'
                                        }
                            ),  
                    ], style={
                     'float':'left',
                     'width':'25%',
                     'backgroundColor':'ffffff',
                     'border':divBorder['border'],
                     'border-radius':divBorder['border-radius'],
                     'display' : 'inline-block', 
                     'boxSizing' : 'border-box', 
                     'box-shadow' : '2px 2px 2px lightgrey',
                     'position':'relative' 
                    }),

#### Traffic Details        
                    html.Div([ 
                    dcc.Loading(
                    dcc.Graph(
                    id='Interactions-Traffic')
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
                         }),
                    
            ], style={'paddingBottom': '5', "overflow": "auto"}),
    html.Br(),
    html.Div([     
        
        html.Div([   
    
    #### User-Interactions Details 
                html.Div([ 
                dcc.Loading(
                dcc.Graph(
                id='User-Interactions')
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
            
    #### Total Interactions Details
                html.Div([ 
                dcc.Loading(
                dcc.Graph(
                id='Total-Interactions')
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
                style={'paddingBottom' : '5', "overflow": "auto"}),
        
            html.Br(),
            
        html.Div(id= 'Article-Interactions'), 
        
        html.Br()
            ]),
], className = "container")


############### DB Loader Articles
@app.callback(
        dash.dependencies.Output('Intermediate-Details2','children'),
        [dash.dependencies.Input('my-date-picker-range', 'start_date'),
        dash.dependencies.Input('my-date-picker-range', 'end_date')])
    
def db_articles(start_date, end_date):
 
    ArticleSet = Articles.query.filter(Articles.status_id == 7).all()
    
    article_table = []
    for Article in ArticleSet:
        cont = [Article.id, Article.title, Article.content, Article.updated_at]
        article_table.append(cont)
            
    article_table_df = pd.DataFrame(article_table, 
                           columns=['id','title',
                                    'content', 'updated_at'])
 
    
    return json.dumps(article_table, default = myconverter)

############### DB Loader Interactions
@app.callback(
        dash.dependencies.Output('Intermediate-Details1','children'),
        [dash.dependencies.Input('my-date-picker-range', 'start_date'),
        dash.dependencies.Input('my-date-picker-range', 'end_date')])
    
def db_interactions(start_date, end_date):
    
    start = dt.strptime(start_date[:10], '%Y-%m-%d').strftime("%Y%m%d")
    
    end = dt.strptime(end_date[:10], '%Y-%m-%d').strftime("%Y%m%d")
    
    Interactions_df = Interactions.query.filter(Interactions.updated_at <= end,
                                               Interactions.updated_at >= 
                                                                   start).all()
    interactions_table = []        
    for intr in Interactions_df:
        cont = [intr.id, intr.user_id, intr.article_id, 
                intr.interaction_type_id,intr.updated_at]
        interactions_table.append(cont)
            
    
    interactions_table_df = pd.DataFrame(interactions_table, 
                           columns=['id','user_id',
                                    'article_id', 'interaction_type_id', 
                                                                'updated_at'])
    
    return json.dumps(interactions_table, default = myconverter)


############### Unique rated Articles
@app.callback(
        dash.dependencies.Output('Liked-Article','children'),
        [dash.dependencies.Input('Intermediate-Details1', 'children')])
    
def rated_articles(interactions_table):
    interactions = pd.DataFrame(eval(str(interactions_table)),
                                columns=['id','user_id', 'article_id', 
                                         'interaction_type_id', 'updated_at'])
    
    unique_articles = interactions['article_id'].nunique() 
    
    
    return unique_articles


############### Unique Raters
@app.callback(
        dash.dependencies.Output('Raters','children'),
        [dash.dependencies.Input('Intermediate-Details1', 'children')])
    
def article_raters(interactions_table):
    interactions = pd.DataFrame(eval(str(interactions_table)),
                                columns=['id','user_id', 'article_id', 
                                         'interaction_type_id', 'updated_at'])
    
    unique_users = interactions['user_id'].nunique() 
    
    
    return unique_users


############### Interactions types  
@app.callback(
        dash.dependencies.Output('Interactions-types','children'),
        [dash.dependencies.Input('Intermediate-Details1', 'children')])
    
def interaction_types(interactions_table):
    interactions = pd.DataFrame(eval(str(interactions_table)),
                                columns=['id','user_id', 'article_id', 
                                         'interaction_type_id', 'updated_at'])
    
    unique_users = interactions['interaction_type_id'].nunique() 
    
    
    return unique_users

############### User_id Interactions
@app.callback(
        dash.dependencies.Output('User-Interactions','figure'),
        [dash.dependencies.Input('Intermediate-Details1', 'children') ])
    
def user_interactions_data(interactions_table): 
    interactions = pd.DataFrame(eval(str(interactions_table)), 
                                            columns=['id','user_id',
                                    'article_id', 'interaction_type_id', 
                                                            'updated_at'])
    
    interactions_df = interactions.groupby('user_id')[
                                            'interaction_type_id'].count().head(10) 
    
    intr_df = pd.DataFrame(interactions_df) 
    Index_intr_df = intr_df.reset_index()  
    
    data = plotly.graph_objs.Bar(
            y=Index_intr_df.user_id,
            x=Index_intr_df.interaction_type_id, 
            orientation='h',            
            name='User_Interactions' 
            )
    
    return {'data': [data],
            'layout' : go.Layout(title=dict(
                                            text="<b> Top Users (Interactions) </b>",
                                            ), 
                                            font=dict(size=10),
                                            height = 350,
                                            margin = dict(l=180, r=50, b=50,
                                                          t=100, pad=5), 
                                            xaxis=dict(automargin = True, 
                                                       tickangle=45),
#                                            yaxis=dict(title = 'Counts')
                                            )}


############### Interactions Details
@app.callback(
        dash.dependencies.Output('Total-Interactions','figure'),
        [dash.dependencies.Input('Intermediate-Details1', 'children') ])
    
def total_interactions_data(interactions_table):
#    interactions = pd.read_json(eval(str(interactions_table)))
    interactions = pd.DataFrame(eval(str(interactions_table)), 
                                            columns=['id','user_id',
                                    'article_id', 'interaction_type_id', 
                                                            'updated_at'])
    
    interactions_df = interactions.groupby('interaction_type_id')[
                                                        'user_id'].count() 
    
    intr_df = pd.DataFrame(interactions_df) 
    Index_intr_df = intr_df.reset_index() 
    Index_intr_df['interaction_type_id'] = Index_intr_df[
                                    'interaction_type_id'].map({1: 'Likes', 2: 
                                                    'Bookmarks', 3: 'Share'})
    
    data = plotly.graph_objs.Bar(
            x=Index_intr_df.interaction_type_id,
            y=Index_intr_df.user_id, 
            name='Interactions' 
            )
    
    return {'data': [data],
            'layout' : go.Layout(title=dict(
                                            text="<b>Articles Interactions</b>",
                                            ), 
                                            font=dict(size=10),
                                            height = 350,
                                            xaxis=dict(automargin = True, 
                                                       tickangle=45),
                                            yaxis=dict(title = 'Counts')
                                            )}


############### Top liked Articles
@app.callback(
        dash.dependencies.Output('Article-Interactions', 'children'),
        [dash.dependencies.Input('Intermediate-Details1', 'children'),
        dash.dependencies.Input('Intermediate-Details2', 'children')])
    
def articles_interactions_data(interactions_table, article_table): 
    
    interactions = pd.DataFrame(eval(str(interactions_table)), 
                                            columns=['id','user_id',
                                    'article_id', 'interaction_type_id', 
                                                            'updated_at'])
    
    interactions_df = interactions.groupby('article_id')[
                                            'interaction_type_id'] \
                                            .count() \
                                            .sort_values(ascending=False) \
                                            .head(10) 
    
    intr_df = pd.DataFrame(interactions_df) 
    Index_intr_df = intr_df.reset_index()  
    user_df = interactions.loc[interactions['article_id'].isin(Index_intr_df['article_id'])] 
    
    articles = pd.DataFrame(eval(str(article_table)), 
                                            columns=['id','title',
                                    'content', 'updated_at'])
    
    article_df = articles.loc[articles['id'].isin(Index_intr_df['article_id'])]   
    article_df = pd.DataFrame(article_df.drop(['content', 'updated_at'], 1))  
    article_df = article_df.join(user_df['user_id'])
    
    return html.Div([
			dash_table.DataTable(
				id='table',
				columns=[{"name": i, "id": i} for i in article_df.columns],
				data=article_df.to_dict("rows"),
				style_cell={'width': 'auto',  
				'height': 'auto', 
                'fontSize': 12,
				'textAlign': 'left'})
			])
                                         

############### Daily Traffic    
@app.callback(
        dash.dependencies.Output('Interactions-Traffic','figure'), 
        [dash.dependencies.Input('Intermediate-Details1', 'children')])
    
def interaction_traffic(interactions_table):
    
    app_dmat_df = pd.DataFrame(eval(str(interactions_table)), 
                                            columns=['id','user_id',
                                    'article_id', 'interaction_type_id', 
                                                            'updated_at'])
    
    app_dmat_df['updated_at'] =  pd.to_datetime(app_dmat_df['updated_at'], 
               format='%Y-%m-%d')
    
    app_dmat_df['updated_at'] = app_dmat_df['updated_at'].dt.date
    enc_dmat = app_dmat_df
       
    
    Enc_event_date = enc_dmat.groupby('updated_at').size() 
    event_date_df= pd.DataFrame(Enc_event_date) 
    Index_event_date_df = event_date_df.reset_index()
    Index_event_date_df.columns = ['updated_at', 'counts']
    
    data = plotly.graph_objs.Scatter(x=Index_event_date_df.updated_at, 
                                     y=Index_event_date_df.counts)
    
    xmin, xmax = np.min(Index_event_date_df.updated_at.to_numpy()), \
                        np.max(Index_event_date_df.updated_at.to_numpy())
    
    return {'data': [data],
            'layout' : go.Layout(
                                title=dict(
                                text="<b>Daily Traffic</b>",
                                        ),
                                margin = dict(l=70, r=40, b=70,
                                                          t=50, pad=5),
                                height = 300,
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
