#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 09:28:36 2019

@author: o.arigbabu
"""

import numpy as np
import pandas as pd
import json
from google.cloud import bigquery
#from bq_helper import BigQueryHelper
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file('/Users/o.arigbabu/Clane-Code/firebasedb/clane-8d862-fa96872fe9cb.json')
project_id = "clane-8d862"
client = bigquery.Client(credentials= credentials, project=project_id)

query_job = client.query("SELECT * FROM `clane-8d862.analytics_183730768.events_20190818` ")

#QUERY = """
#        SELECT location, city, country, value, timestamp
#        FROM `bigquery-public-data.openaq.global_air_quality`
#        WHERE pollutant = "pm10" AND timestamp > "2017-04-01"
#        ORDER BY value DESC
#        LIMIT 1000
#        """
        
results = query_job.result()  # Waits for job to complete.

print(results)

datan = list(query_job.result(timeout=30))
 

df = pd.DataFrame(data=[list(x.values()) for x in datan], columns=list(datan[0].keys()))


 
 
















#from firebase import Firebase
#import firebase_admin
#from firebase_admin import credentials
#import pyrebase
#
#
##cred = credentials.Certificate('/Users/o.arigbabu/Clane-Code/firebasedb/google-services.json')
##firebase_admin.initialize_app(cred, {
##    'databaseURL' : 'https://clane-8d862.firebaseio.com'
##})
#
## AIzaSyDJuMSGBPwwTx8Zd3MQUx8Oy4HwnEu90Yc
#
#config = {
#  "apiKey": "fa96872fe9cbec0487686e419b6e41abbcebf2af", 
#  "authDomain": "clane-8d862.firebaseapp.com",
#  "databaseURL": "https://clane-8d862.firebaseio.com",
#  "storageBucket": "clane-8d862.appspot.com",
#  "serviceAccount": "/Users/o.arigbabu/Clane-Code/firebasedb/clane-8d862-fa96872fe9cb.json"
#}
#
#firebase = pyrebase.initialize_app(config)
#
#auth = firebase.auth()
# 
#user = auth.sign_in_with_email_and_password("dev.clane@gmail.com", "pressureandsuccess")
#
#db = firebase.database()


 
