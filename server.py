from flask import Flask,  render_template, request, current_app
import os
import random
import sys

from sql_db_class import Database
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
    db.init_user_db()
   
    
    return app


app = create_app()


if __name__ == "__main__":
    
    app.run()