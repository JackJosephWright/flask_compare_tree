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


def gen_random_pics(db):
    
    r_list = sample(range(1,db.n_pics+1),2)
                
                
    return r_list
                


def home_page():
    db = current_app.config['db']

def index():
    if request.method =='POST':
        db = current_app.config['db']
        print('INSIDE INDEX() VALUE OF db.last_accessed:',db.last_accessed)
        #print('random indexes:',db.last_accessed)
        #print('db.last_accessed:{}'.format(db.last_accessed))
        db.update_tree(db.last_accessed,request.form['complex'])
        
        r_list = gen_random_pics(db)
        #print('r list is filled with:',str(r_list))
        while(db.last_accessed!=r_list):
            db.last_accessed=r_list
        #print('checking if db_last accessed is updated:{}'.format(db.last_accessed))
        links = db.get_trees(r_list)

        
        return render_template('index.html',images=r_list, img_list=links)
        
    else:
        
        
        db = current_app.config['db']
        r_list = gen_random_pics(db)
        while(db.last_accessed!=r_list):
            db.last_accessed=r_list
        links = db.get_trees(r_list)

        
        return render_template('index.html',images=r_list, img_list=links)

def results():
    columns = list(('name', 'W','L'))
    data = []

    print(columns)
    
    db = current_app.config['db']
    for k,v in db.trees.items():
            name=v.name
            link=v.link
            W=v.W
            L=v.L
            print('name:{} link:{} W:{} L{}'.format(name, link, W, L))
            values = [name, W, L]
            zipped = zip(columns, values)
            a_dictionary = dict(zipped)
            print(a_dictionary)
            data.append(a_dictionary)
    scores_table=pd.DataFrame(data).set_index('name')
    print(scores_table)
    
    
    #check if table exists
    # #engine = create_engine('sqlite:///tc.db') #access the DB engine
    # #if not engine.dialect.has_table(engine, scores_table): #if table doesnt exist, create
    #     #sqlite_connection = engine.connect()
    #     #sqlite_table = 'scores_table'
    #     #scores_table.to_sql(sqlite_table,sqlite_connection, if_exists='fail')
    #     #sqlite_connection.close()
    #     print('inside engine.dialect.hastable check')
    # else:
    #     dat = sqlite3.connect('tc.db')
    #     query = dat.execute("SELECT * FROM scores_table")
    #     cols = [column[0] for column in query.description]
    #     old_scores = pd.DataFrame.from_records(data=query.fetchall(), columns = cols)
    engine = create_engine('sqlite:///tc.db', echo=False)
    sqlite_connection = engine.connect()
    insp = inspect(engine)
    sqlite_table='scores_table'
    if (insp.has_table('scores_table')==True):
        print('there is a scores table')
        old_scores=pd.read_sql_table('scores_table',sqlite_connection).set_index('name')
        print(old_scores)
    else:
        scores_table.to_sql(sqlite_table,sqlite_connection,if_exists='fail')
    df_total = old_scores.add(scores_table, fill_value=0)
    



    

    #getting sqlite3 table into program
    dat = sqlite3.connect('tc.db')
    query = dat.execute("SELECT * FROM tree_info")
    cols = [column[0] for column in query.description]
    tree_info = pd.DataFrame.from_records(data = query.fetchall(), columns = cols).set_index('tree_name')
    table_list = [scores_table.sort_values(by=['W'],ascending=False).to_html(classes='data'), df_total.sort_values(by=['W'],ascending=False).to_html(classes='data'),tree_info.to_html(classes='data')]
    return render_template('results.html', tables = table_list)