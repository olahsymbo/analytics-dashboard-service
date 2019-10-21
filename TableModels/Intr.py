#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:14:50 2019

@author: o.arigbabu
"""

import inspect
import os
app_path = inspect.getfile(inspect.currentframe())
module_dir = os.path.realpath(os.path.dirname(app_path))
import sys
sys.path.insert(0, module_dir)
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy  
from configura import * 

# Retrieve set environment variables
#connectt1 = os.environ.get('connection_1')
#connectt2 = os.environ.get('connection_2')
#
#app = Flask(__name__)
#app.config['DEBUG'] = True
#app.config['SQLALCHEMY_DATABASE_URI'] = connectt1
#app.config['SQLALCHEMY_BINDS'] = {
#    'news': connectt1,
#    'users': connectt2
#}
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#db = SQLAlchemy(app)

connectt = os.environ.get('connection')

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = connectt
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Interactions(db.Model):
    __tablename__ = 'interactions'

    id = db.Column('id', db.Integer, primary_key=True) 
    user_id = db.Column('user_id', db.String())
    article_id = db.Column('article_id', db.Integer)
    interaction_type_id = db.Column('interaction_type_id', db.Integer)
    created_at = db.Column('created_at', db.DateTime)
    updated_at = db.Column('updated_at', db.DateTime)

#class AppUsers(db.Model):
#    __tablename__ = 'appusers'
#    __bind_key__ = 'users'
#
#    id = db.Column('id', db.Integer, primary_key=True) 
#    phone = db.Column('phone', db.String())
#    created_at = db.Column('created_at', db.DateTime)
#    updated_at = db.Column('updated_at', db.DateTime)