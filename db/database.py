from db.command import * 
import os
import sqlite3

class Database:

    def __init__(self,database_name):
        self.database_name = database_name
    
    def get_db_connection(self):
        conn = sqlite3.connect(self.database_name)
        conn.row_factory = sqlite3.Row
        return conn

    def create_db(self):
        with self.get_db_connection() as conn:
            conn.execute(create_category)
            conn.execute(create_eats)
    
    def init_db(self):
        if not os.path.exists(self.database_name):
            self.create_db()
            with self.get_db_connection() as conn:
                conn.commit()

    def select_category(self):
        result = []
        with self.get_db_connection() as conn:
            cur = conn.cursor()
            cur.execute(select_category)
            rows = cur.fetchall()
            for row in rows:
                result.append(row[0])
            return result

    # def add_categoty(self,name):
    #     with self.get_db_connection() as conn:
    #         cur = conn.cursor()
    #         # parameters = name
    #         cur.execute(insert_category,name)
    #         conn.commit()


    def add_food(self,Name,Price,Description,idCategory):
        with self.get_db_connection() as conn:
            cur = conn.cursor()
            parameters = (Name,Price,Description,idCategory)
            cur.execute(insert_eats,parameters)

    def get_colons(self):
        with self.get_db_connection() as conn:
            cur = conn.execute("select * from category")
            row = cur.fetchone()
            names = row.keys()
            return names
