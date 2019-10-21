#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
import dash_html_components as html 
from pages import commonmodules 
 
layout = html.Div([
    commonmodules.get_header(),
    commonmodules.get_menu(),
    html.Br(),
    html.H3('Welcome to Clane Dashboard'),
])