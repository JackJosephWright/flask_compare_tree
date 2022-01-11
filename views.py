from os import name
from flask import current_app, render_template, request, g
from random import randint , shuffle , sample
from flask.helpers import url_for
from sqlalchemy.sql.schema import MetaData
from werkzeug.utils import redirect
import threading
import pandas as pd
import numpy as np
#from database import Database
from sqlalchemy import create_engine, inspect
import sqlite3
from sql_db_class import Database


def index():
    db = Database()
    

    
        
    if request.method =='POST':
        
        db.update_tree(request.form['complex'])
        db.new_random()
        links = db.get_links()
        img_number = db.last_accessed()
        return render_template('index.html',images=img_number, img_list = links)
    
    else:
        
        links = db.get_links()
        img_number = db.last_accessed()
        return render_template('index.html',images=img_number, img_list=links)
def results():
    db = Database()
    user_db = db.get_current_user()
    scores_table = db.get_scores_table()
    tree_info = db.get_tree_info()
    output = pd.concat([user_db, scores_table]).groupby(['pic_number','link']).sum(['W','L']).reset_index()
    output = output.set_index('pic_number')
    
    print(output)
    #getting sqlite3 table into program
    #dat = sqlite3.connect('tc.db')
    #query = dat.execute("SELECT * FROM tree_info")
    #cols = [column[0] for column in query.description]
    #tree_info = pd.DataFrame.from_records(data = query.fetchall(), columns = cols).set_index('tree_name')
    table_list = [output.sort_values(by=['W'],ascending=False).to_html(classes='data'), user_db.sort_values(by=['W'],ascending=False).to_html(classes='data'),tree_info.to_html(classes='data')]
    db.set_scores_table(output)
    db.init_user_db()
    return render_template('results.html', tables = table_list)


    
