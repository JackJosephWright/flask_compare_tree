from flask import current_app, render_template, request
from random import randint , shuffle , sample

def home_page():
    db = current_app.config['db']

def index():
    
    if request.method =='GET':
        db = current_app.config['db']
        n_pics = len(db.trees)
        r_list = sample(range(1,n_pics),2)
        
        
        links = db.get_trees(r_list)
        
        

        
        return render_template('index.html',images=r_list, img_list=links)

def submit():
    print('inside submit function')
    if request.method =='POST':
        winner = request.form['complex']
        #print(winner)


        
