from flask import current_app, render_template, request
from random import randint , shuffle , sample
from flask.helpers import url_for

from werkzeug.utils import redirect

def gen_random_pics(db):
    n_pics = len(db.trees)
    r_list = sample(range(1,n_pics),2)
                
                
    return r_list
                


def home_page():
    db = current_app.config['db']

def index():
    if request.method =='POST':
        print('index method is post')
        db = current_app.config['db']
        
        print('random indexes:',db.last_accessed)
        print('db.last_accessed:{}'.format(db.last_accessed))
        db.update_tree(db.last_accessed,request.form['complex'])
        
        r_list = gen_random_pics(db)
        db.last_accessed=r_list
        links = db.get_trees(r_list)

        
        return render_template('index.html',images=r_list, img_list=links)
        
    else:
        print('index method is get')
        db = current_app.config['db']
        r_list = gen_random_pics(db)
        db.last_accessed=r_list
        links = db.get_trees(r_list)

        
        return render_template('index.html',images=r_list, img_list=links)
        
