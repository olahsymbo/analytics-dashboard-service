#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import inspect
app_path = inspect.getfile(inspect.currentframe())
dash_dir = os.path.realpath(os.path.dirname(app_path))
 
import dash
import dash_bootstrap_components as dbc 
from dashboard_firebase import *
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'] 

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
app.config.suppress_callback_exceptions = True
     