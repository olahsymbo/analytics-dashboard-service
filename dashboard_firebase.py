import os
import inspect
app_path = inspect.getfile(inspect.currentframe())
dash_dir = os.path.realpath(os.path.dirname(app_path))

from google.cloud import bigquery
from bq_helper import BigQueryHelper
from google.oauth2 import service_account

def db_config(dash_dir):
    credentials = service_account.Credentials.from_service_account_file(
            os.path.join(dash_dir, "config/project-8b812-fa96872fe9cb.json"))
    
    project_id = "project-8b812"
    client = bigquery.Client(credentials=credentials, project=project_id)
    return client
