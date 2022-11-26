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

    def select_category_and_food(self):
        result = {}
        with self.get_db_connection() as conn:
            cur = conn.cursor()
            cur.execute(select_categorys_and_food)
            rows = cur.fetchall()
            for row in rows:
                try:
                    result[row[0]].append(row[1])
                except:
                    result[row[0]] = [row[1]]
        return result

    def select_category_and_hisfood(self,category):
        result = {f"{category}":[]}
        with self.get_db_connection() as conn:
            cur = conn.cursor()
            cur.execute(select_category_and_his_food, category)
            
            rows = cur.fetchall()
            for row in rows:
                result[category].append(row[1])
            return result

    def select_food_info(self):
        result = {}
        with self.get_db_connection() as conn:
            cur = conn.cursor()
            cur.execute(select_food_info)
            rows = cur.fetchall()
            for row in rows:
                result[row[0]] = {"protein":row[1],"fats":row[2],"carbohydrates":row[3],"kilocolories":row[4]}
        return result
    
    def select_food_disc(self):
        result = {}
        with self.get_db_connection() as conn:
            cur = conn.cursor()
            cur.execute(select_food_disc)
            rows = cur.fetchall()
            for row in rows:
                result[row[0]] = {"disc":row[1]}
        return result
    
    def select_food_full_info(self):
        result = {}
        with self.get_db_connection() as conn:
            cur = conn.cursor()
            cur.execute(select_food_full_info)
            rows = cur.fetchall()
            for row in rows:
                # row[0] - NameFood
                result[row[1]]={"idfood":row[0],
                                "Description":row[2],
                                "cookingMethod":row[3],
                                "foodValue":row[4],
                                "price":row[5],
                                "protein":row[6],
                                "fats":row[7],
                                "carbohydrates":row[8],
                                "kilocolories":row[9],
                                "CategoryFood":row[10],
                                }
        return result
        
