from tree import Tree
import os

class Database:
    def __init__(self):
        self.trees = {}
        self._last_tree_key = 0
        self.last_accessed = []
    def load_trees(self, image_location='static\images'):
        
        for filename in os.listdir(image_location):
            if filename.endswith('jpg') or filename.endswith('.png'):
                self._last_tree_key +=1
                tree=Tree(filename,link=os.path.join(image_location,filename))
                self.trees[self._last_tree_key] = tree
        
    def print_trees(self):
        for k,v in self.trees.items():
            name=v.name
            link=v.link
            W=v.W
            L=v.L
            
        
    def get_trees(self,index_list):
        
        self.last_accessed=index_list
        image_address = []
        
        
        for index in index_list:
            link = self.trees[index].link
            image_address.append(link)
        return image_address
        
            
            

