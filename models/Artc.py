import inspect
import os
app_path = inspect.getfile(inspect.currentframe())
module_dir = os.path.realpath(os.path.dirname(app_path))
import sys
sys.path.insert(0, module_dir)
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy  

connectt = os.environ.get('connection')

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = connection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


article_category = db.Table('article_category',
    db.Column('article_id', db.Integer, db. ForeignKey('articles.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'))               
)


class Articles(db.Model):
    __tablename__ = 'news_art'

    id = db.Column('id', db.Integer, primary_key=True) 
    title = db.Column('title', db.String())
    author = db.Column('author', db.String())
    content = db.Column('content', db.Text)
    published_date = db.Column('published_date', db.DateTime)
    created_at = db.Column('created_at', db.DateTime)
    updated_at = db.Column('updated_at', db.DateTime)
    deleted_at = db.Column('deleted_at', db.DateTime)
    additional_data = db.Column('additional_data', db.Integer)

    art_category = db.relationship('Category',
                                   secondary=article_category,
                                   backref= db.backref('news', lazy='dynamic'))


class Category(db.Model):
    __tablename__ = 'category'
    
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String())


class Interactions(db.Model):
    __tablename__ = 'interact'

    id = db.Column('id', db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.String())
    news_art_id = db.Column('news_art_id', db.Integer)
    interaction_id = db.Column('interaction_id', db.Integer)
    created_at = db.Column('created_at', db.DateTime)
    updated_at = db.Column('updated_at', db.DateTime)
