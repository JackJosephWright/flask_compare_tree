from tree import Tree
import os
import re
from random import randint, shuffle, sample
import pandas as pd
from sqlalchemy import create_engine, inspect
import sqlite3


class Database:
    def __init__(self):
        self.sqlite_address = 'sqlite:///tc.db'
        self.image_location='static\images'
        
    def conn(self):

        engine = create_engine(self.sqlite_address, echo=False)
        sqlite_connection = engine.connect()
        return [engine, sqlite_connection, inspect(engine)]
    def init_user_db(self):
        user_db = pd.DataFrame(columns = ['pic_number','link','W','L'])
        for filename in os.listdir(self.image_location):
            if filename.endswith('jpg') or filename.endswith('.png'):
                pic_number = int(re.search('[0-9]+', filename).group())
                link = os.path.join(self.image_location, filename)
                tree = [pic_number,link,0,0]
                df_length = len(user_db)
                user_db.loc[df_length]=tree
        user_db = user_db.sort_values(by=['pic_number']).set_index(['pic_number'])
        engine, sqlite_connection, insp = self.conn()
        sqlite_table = 'user_table'
        if (insp.has_table(sqlite_table)==True):
            user_db.to_sql(sqlite_table,sqlite_connection,if_exists = 'replace',index_label='pic_number')
        else:
            user_db.to_sql(sqlite_table, sqlite_connection, if_exists = 'fail',index_label='pic_number')
        sqlite_connection.close()

    def last_accessed(self):
        engine , sqlite_connection, insp = self.conn()

        sqlite_table = 'rand_table'
        if (insp.has_table('rand_table') == True):
            #get the last accessed
            last_accessed = list(pd.read_sql_table('rand_table',sqlite_connection)['0'])
            return last_accessed
        sqlite_connection.close()
    def update_tree(self,win):
        engine , sqlite_connection, insp = self.conn()
        user_db = pd.read_sql_table('user_table', sqlite_connection, index_col='pic_number').reset_index(drop=True)
        index_list = self.last_accessed()
        #print(user_db)
        #print(index_list)
        if win =='TRUE':
             user_db.loc[index_list[0],'W']=user_db.loc[index_list[0],'W']+1
             user_db.loc[index_list[1],'L']=user_db.loc[index_list[1],'L']+1
        else:
            user_db.loc[index_list[0],'L']=user_db.loc[index_list[0],'L']+1
            user_db.loc[index_list[1],'W']=user_db.loc[index_list[1],'W']+1
        user_db.to_sql('user_table',sqlite_connection,if_exists = 'replace', index_label='pic_number')
        sqlite_connection.close()
    def get_links(self):
        index_list = self.last_accessed()
        engine , sqlite_connection, insp = self.conn()
        user_db = pd.read_sql_table('user_table', sqlite_connection)#.reset_index(drop=True)
        index_list = self.last_accessed()
        link1 = user_db.loc[user_db['pic_number']==index_list[0],'link'].item()
        link2 = user_db.loc[user_db['pic_number'] == index_list[1],'link'].item()

        return [link1, link2]
    def new_random(self):
        engine , sqlite_connection, insp = self.conn()
        sqlite_table = 'rand_table'
        rand_table=sample(range(0,22),2)
        pd.Series(rand_table).to_sql(sqlite_table,sqlite_connection,if_exists = 'replace', index=False)
        sqlite_connection.close()
    def get_current_user(self):
        engine , sqlite_connection, insp = self.conn()
        user_db = pd.read_sql_table('user_table', sqlite_connection)#.reset_index(drop=True)
        sqlite_connection.close()
        return user_db
    def get_scores_table(self):
        engine , sqlite_connection, insp = self.conn()
        sqlite_table = 'scores_table'
        if (insp.has_table(sqlite_table)==True):
            scores_table = pd.read_sql_table(sqlite_table, sqlite_connection)
        else:
            scores_table = pd.DataFrame(columns = ['pic_number','link','W','L'])
            for filename in os.listdir(self.image_location):
                if filename.endswith('jpg') or filename.endswith('.png'):
                    pic_number = int(re.search('[0-9]+', filename).group())
                    link = os.path.join(self.image_location, filename)
                    tree = [pic_number,link,0,0]
                    df_length = len(scores_table)
                    scores_table.loc[df_length]=tree
            scores_table = scores_table.sort_values(by=['pic_number']).set_index(['pic_number'])
            scores_table.to_sql(sqlite_table, sqlite_connection, if_exists = 'fail',index_label='pic_number')
        sqlite_connection.close()
        return scores_table
    def set_scores_table(self, data):
        print(data)
        engine , sqlite_connection, insp = self.conn()
        sqlite_table = 'scores_table'
        data.to_sql(sqlite_table, sqlite_connection, if_exists = 'replace', index_label = 'pic_number')
    def get_tree_info(self):
        engine , sqlite_connection, insp = self.conn()
        sqlite_table = 'tree_info'
        tree_info = pd.read_sql_table(sqlite_table, sqlite_connection)
        sqlite_connection.close()
        return tree_info
    def drop_scores_table(self):
        engine, sqlite_connection, insp = a.conn()
        connection = engine.raw_connection()
        cursor = connection.cursor()
        command = 'DROP TABLE IF EXISTS scores_table'
        cursor.execute(command)
        connection.commit()
        cursor.close()

if __name__ == "__main__":
    
    a=Database()
    a.init_user_db()
    