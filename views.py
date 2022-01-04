from flask import current_app, render_template, request
from random import randint , shuffle , sample
from flask.helpers import url_for
from werkzeug.utils import redirect
import threading
import pandas as pd
import numpy as np

def gen_random_pics(db):
    n_pics = len(db.trees)
    r_list = sample(range(1,n_pics+1),2)
                
                
    return r_list
                


def home_page():
    db = current_app.config['db']

def index():
    if request.method =='POST':
        db = current_app.config['db']
        #print('random indexes:',db.last_accessed)
        #print('db.last_accessed:{}'.format(db.last_accessed))
        db.update_tree(db.last_accessed,request.form['complex'])
        
        r_list = gen_random_pics(db)
        #print('r list is filled with:',str(r_list))
        db.last_accessed=r_list
        #print('checking if db_last accessed is updated:{}'.format(db.last_accessed))
        links = db.get_trees(r_list)

        
        return render_template('index.html',images=r_list, img_list=links)
        
    else:
        print('index method is get')
        db = current_app.config['db']
        r_list = gen_random_pics(db)
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
    df=pd.DataFrame(data)
    return render_template('results.html', tables = [df.sort_values(by=['W'],ascending=False).to_html(classes='data')])