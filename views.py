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
    
    
    db = current_app.config['db']
    r_list = gen_random_pics(db)
    links = db.get_trees(r_list)

      
    return render_template('index.html',images=r_list, img_list=links)
    
def submit():
    if request.method =='POST':
        db = current_app.config['db']
        print(db.last_accessed)
        print(request.form['complex'])
        r_list = gen_random_pics(db)
        links = db.get_trees(r_list)

        return render_template('index.html',images=r_list, img_list=links)