#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import visual_dash, visual_interactions, commonmodules

from app import app


layout = html.Div([
    commonmodules.get_header(),
    commonmodules.get_menu(),
    html.Br(),
    html.H3('Welcome to Clane Dashboard'),
])