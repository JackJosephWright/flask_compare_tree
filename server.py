from flask import Flask,  render_template, request
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
    db = Database()
    
    db.load_trees('static/images')
    db.print_trees()
    app.config['db']=db
    
    
    return app


app = create_app()


if __name__ == "__main__":
    app.run()