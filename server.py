from flask import Flask,  render_template, request, session
import os
import random
import sys

from database import Database
from tree import Tree
import views
import sqlite3
import pandas as pd
import numpy as np

def create_app():
    
    app=Flask(__name__)
    app.config.from_object('settings')
    app.add_url_rule('/', methods = ['GET','POST'], view_func = views.index)
    app.add_url_rule('/submit_db/', methods = ['GET','POST'], view_func=views.results)
    db_first = Database()
    
    db_first.load_trees('static/images')
    
    app.config['db']=db_first
    Session(app)
    
    print('app created')
    print('db.last_accessed:{}'.format(db_first.last_accessed))
    
    
    return app


app = create_app()


if __name__ == "__main__":
    app.run()