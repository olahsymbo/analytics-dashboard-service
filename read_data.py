#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 21:38:52 2019

@author: o.arigbabu
"""

import pandas as pd
import numpy as np
from dashboard_firebase import *

def read_data(data):
    app_dmat = []
    for row in range(len(data)):
        
        user_id = data.loc[row]['user_pseudo_id']
        user_first_touch = data.loc[row]['user_first_touch_timestamp']
        
        device = data.loc[row]['device']['category']
        brand_name = data.loc[row]['device']['mobile_brand_name']
        platform = data.loc[row]['platform']
         
        
        
        geo_city = data.loc[row]['geo']['city']
        geo_country = data.loc[row]['geo']['country']
        geo_continent = data.loc[row]['geo']['continent']
        
        event_name = data.loc[row]['event_name']
        event_date = data.loc[row]['event_date']
        event_previous_time = data.loc[row]['event_previous_timestamp']
        event_time = data.loc[row]['event_timestamp']
        event_bundle_sequence_id = data.loc[row]['event_bundle_sequence_id']
        event_diff = np.subtract(int(event_time),int(user_first_touch))
    #    engagement_time = data[row]['event_params']['engagement_time_msec']
        
        app_dmat.append([user_id, user_first_touch, device, 
                        brand_name, platform, geo_city, geo_country, 
                        geo_continent, event_name, event_date, 
                        event_previous_time, event_time, event_bundle_sequence_id, event_diff])
    
    colums = ['user_id', 'user_first_touch', 'device', 
                        'brand_name', 'platform', 'geo_city', 'geo_country', 
                        'geo_continent', 'event_name', 'event_date', 
                        'event_previous_time', 'event_time', 'event_bundle_sequence_id', 'event_diff']
     
    
    app_dmat_df = pd.DataFrame(app_dmat, columns = colums)
    
    enc_dmat = app_dmat_df
    
    return enc_dmat
    
    #print(len(enc_dmat['user_id'].unique()))
    
data = df 

enc_dmat = read_data(data)
    
Enc_events = enc_dmat.groupby('event_name')['user_id'].count().sort_values(ascending=True)
Event_df = pd.DataFrame(Enc_events) 
Index_Event_df = Event_df.reset_index()

Enc_users = enc_dmat.groupby('user_id')['event_name'].count().sort_values(ascending=True)
User_df = pd.DataFrame(Enc_users) 
Index_User_df = User_df.reset_index()

Enc_country = enc_dmat.groupby('geo_country')['user_id'].count().sort_values(ascending=False) 
country_df = pd.DataFrame(Enc_country) 
Index_country_df = country_df.reset_index()

Enc_city = enc_dmat.groupby('geo_city')['user_id'].count().sort_values(ascending=False) 
city_df = pd.DataFrame(Enc_city) 
Index_city_df = city_df.reset_index()

Enc_OS = enc_dmat.groupby('platform')['user_id'].count() 
OS_df = pd.DataFrame(Enc_OS) 
Index_OS_df = OS_df.reset_index() 

Enc_brand = enc_dmat.groupby('brand_name')['user_id'].count() 
brand_df = pd.DataFrame(Enc_brand) 
Index_brand_df = brand_df.reset_index() 

Enc_event_time = enc_dmat.groupby('user_id')['event_diff'].sum().sort_values(ascending=True) 
Enc_event_time.sort_values(ascending=False).head(40) 
event_time_df= pd.DataFrame(Enc_event_time) 
Index_event_time_df = event_time_df.reset_index()

Enc_event_date = enc_dmat.groupby('event_date')['user_id'].count() 
event_date_df= pd.DataFrame(Enc_event_date) 
Index_event_date_df = event_date_df.reset_index()


if __name__ == 'main':
    read_data()
    