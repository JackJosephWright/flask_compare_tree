from flask import Flask,  render_template, request
import os
import random

app=Flask(__name__)
d= dict()
current_images=()
def get_pics(max_length):
    p1=random.randint(1,max_length)
    p2=random.randint(1,max_length)
    return[p1,p2]
def all_equal(lst):
    return lst[:-1] == lst[1:]
@app.route('/', methods =['GET','POST'])
def index():
    pics = os.listdir('static/images')
    pics = ['images/'+file for file in pics]
    neq_index=get_pics(len(pics))
    current_images=neq_index
    while all_equal(neq_index):
        neq_index=get_pics(len(pics))
    p_list = [pics[i-1] for i in neq_index] 
    
    return render_template('index.html',images=p_list)
@app.route('/addRegion', methods=['POST'])
def addRegion():
    print(request.form['complex'])
    