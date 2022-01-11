from tree import Tree
import os
import re
from random import randint , shuffle , sample
import pandas as pd

class Database:
    def __init__(self):
        self.trees = {}
        self.last_accessed = []
        self.n_pics = 0
    def load_trees(self, image_location ='static\images'):
        
        for filename in os.listdir(image_location):
            if filename.endswith('jpg') or filename.endswith('.png'):
                pic_number = int(re.search('\d', filename).group())
                tree = Tree(filename, link =  os.path.join(image_location, filename))
                self.trees[pic_number] = tree
    def get_trees(self, index_list):
        
        image_address = []
        index_list = self.last_accessed

        for index in index_list:
            link = self.trees[index].link
            image_address.append(link)
        return image_address
    def update_tree(self, win):
        
        index_list=self.last_accessed
        print('index_list inside update tree:{}'.format(index_list))
        if win =='TRUE':
            
            winner = self.trees[index_list[0]] 
            winner.update_WL(True)
            print('winner:'+str(index_list[0]))
            winner.get_WL()
            self.trees[index_list[0]]=winner
            loser = self.trees[index_list[1]]
            loser.update_WL(False)
            print('loser:'+str(index_list[1]))
            loser.get_WL()
            self.trees[index_list[1]]=loser
                 
        else:
            winner = self.trees[index_list[1]] 
            winner.update_WL(True)
            print('winner:'+str(index_list[1]))
            winner.get_WL()
            self.trees[index_list[1]]=winner
            loser = self.trees[index_list[0]]
            loser.update_WL(False)
            print('loser:'+str(index_list[0]))
            loser.get_WL()
            self.trees[index_list[0]]=loser
    def set_new_pair(self):
        self.last_accessed=sample(range(1,8),2)
        print('updating last accessed:{}'.format(self.last_accessed))
        link_list = self.get_trees(self.last_accessed)
        return(link_list, self.last_accessed)
    def return_scores(self):
        columns = list(('name','W','L'))
        data = []
        for k,v in self.trees.items():
            name = v.name
            W = v.W
            L = v.L
            values = [name,W,L]
            zipped = zip(columns, values)
            d = dict(zipped)
            data.append(d)
        return (pd.DataFrame(data).set_index('name'))