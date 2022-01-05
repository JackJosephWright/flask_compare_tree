from tree import Tree
import os

class Database:
    def __init__(self):
        self.trees = {}
        self._last_tree_key = 0
        self.last_accessed = []
        self.n_pics = 0
    def load_trees(self, image_location='static\images'):
        
        for filename in os.listdir(image_location):
            if filename.endswith('jpg') or filename.endswith('.png'):
                print(filename)
                self._last_tree_key +=1
                tree=Tree(filename,link=os.path.join(image_location,filename))
                self.trees[self._last_tree_key] = tree
            
            self.n_pics = len(self.trees)
        
    def print_trees(self):
        for k,v in self.trees.items():
            name=v.name
            link=v.link
            W=v.W
            L=v.L
            
            
        
    def get_trees(self,index_list):
        
        #self.last_accessed=index_list
        image_address = []
        
        
        for index in index_list:
            link = self.trees[index].link
            image_address.append(link)
        return image_address

    def update_tree(self, index_list,win):
        
        print(index_list)
        

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
        

