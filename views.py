from flask import current_app, render_template, request
from random import randint , shuffle , sample
from flask.helpers import url_for
from sqlalchemy.sql.schema import MetaData
from werkzeug.utils import redirect
import threading
import pandas as pd
import numpy as np
from database import Database
from sqlalchemy import create_engine, inspect
import sqlite3


def index():
    


    var_exists = 'db' in locals() or 'db' in globals()
    if var_exists:
        print('db object already exists')
        pass
    else:
        print('db object does not exist')
        db = current_app.config['db']
    if request.method =='POST':
        db.update_tree(request.form['complex'])
        links, img_number = db.set_new_pair()
        return render_template('index.html',images=img_number, img_list = links)
    
    else:
        links, img_number = db.set_new_pair()
        return render_template('index.html',images=img_number, img_list=links)
def results():
    db = current_app.config['db']
    scores_table = db.return_scores()

    #connect to sqlite

    engine = create_engine('sqlite:///tc.db', echo=False)
    sqlite_connection = engine.connect()
    insp = inspect(engine)
    sqlite_table='scores_table'
    if (insp.has_table('scores_table')==True):
        old_scores=pd.read_sql_table('scores_table',sqlite_connection).set_index('name')
        df_total = old_scores.add(scores_table, fill_value=0)
        df_total.to_sql(sqlite_table,sqlite_connection,if_exists='replace')
    else:
        scores_table.to_sql(sqlite_table,sqlite_connection,if_exists='fail')
        df_total=scores_table
    
    
    
    
    #getting sqlite3 table into program
    dat = sqlite3.connect('tc.db')
    query = dat.execute("SELECT * FROM tree_info")
    cols = [column[0] for column in query.description]
    tree_info = pd.DataFrame.from_records(data = query.fetchall(), columns = cols).set_index('tree_name')
    table_list = [scores_table.sort_values(by=['W'],ascending=False).to_html(classes='data'), df_total.sort_values(by=['W'],ascending=False).to_html(classes='data'),tree_info.to_html(classes='data')]
    return render_template('results.html', tables = table_list)


    
