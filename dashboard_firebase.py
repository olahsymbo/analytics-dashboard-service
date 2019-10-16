#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import inspect
import os  
from google.cloud import bigquery
#from bq_helper import BigQueryHelper
from google.oauth2 import service_account

import inspect
app_path = inspect.getfile(inspect.currentframe())
dash_dir = os.path.realpath(os.path.dirname(app_path))

def db_config(dash_dir):
    credentials = service_account.Credentials.from_service_account_file(
            os.path.join(dash_dir, "config/clane-8d862-fa96872fe9cb.json"))
    
    project_id = "clane-8d862"
    client = bigquery.Client(credentials= credentials, project=project_id)
    return client
    