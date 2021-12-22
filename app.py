from flask import Flask,  render_template, request
import os
import random
import sys

from database import Database
from tree import Tree
import views

def create_app():
    
    app=Flask(__name__)
    app.config.from_object('settings')
    app.add_url_rule('/', methods = ['GET','POST'], view_func = views.index)
    #app.add_url_rule('/submit', methods = ['POST'], view_func=views.submit)
    db = Database()
    
    db.load_trees('static\images')
    db.print_trees()
    app.config['db']=db
    
    
    return app



if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port)