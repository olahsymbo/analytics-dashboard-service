#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import inspect
import os 
import json
from google.cloud import bigquery
#from bq_helper import BigQueryHelper
from google.oauth2 import service_account

from datetime import date, timedelta
previous_date = date.today() - timedelta(days=1)


app_path = inspect.getfile(inspect.currentframe())
dash_dir = os.path.realpath(os.path.dirname(app_path))
 

credentials = service_account.Credentials.from_service_account_file(
        os.path.join(dash_dir, "config/clane-8d862-fa96872fe9cb.json"))

project_id = "clane-8d862"
client = bigquery.Client(credentials= credentials, project=project_id)

start = previous_date.strftime("%Y%m%d")
end = date.today().strftime("%Y%m%d")


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