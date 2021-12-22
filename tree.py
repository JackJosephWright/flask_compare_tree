class Tree:
    def __init__(self, name, link = None, W = 0, L = 0):
        self.name = name
        self.link = link
        self.W = W
        self.L = L
    def get_WL(self):
        print("W:{}, L:{}".format(self.W,self.L))
    def update_WL(self, win):
        if win==True:
            self.W+=1
            
        else:
            self.L+=1
