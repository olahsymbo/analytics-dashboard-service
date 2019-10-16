#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import inspect
app_path = inspect.getfile(inspect.currentframe())
dash_dir = os.path.realpath(os.path.dirname(app_path))

from datetime import datetime as dt  
import pandas as pd 
from dashboard_firebase import *
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

client = db_config(dash_dir)

class queryLoader:
    
    def firebase_db(self, start_date, end_date):        
    
        start = dt.strptime(start_date[:10], '%Y-%m-%d').strftime("%Y%m%d")
        
        end = dt.strptime(end_date[:10], '%Y-%m-%d').strftime("%Y%m%d")
        
        QUERY = """
        SELECT * FROM  `clane-8d862.analytics_183730768.events_*` 
        where REPLACE(_TABLE_SUFFIX, "_", "-")
              BETWEEN {0} AND {1}
              """.format('"%s"' % start, '"%s"' % end)
            
        query_job = client.query(QUERY)
        print("firebase data loaded")
        
        datan = list(query_job.result(timeout=100))
         
        self.df = pd.DataFrame(data=[list(x.values()) for x in datan], 
                                columns=list(datan[0].keys()))
        datann = self.df
        
        return datann.to_json()
        