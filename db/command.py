create_category = """CREATE TABLE IF NOT EXISTS Category(
    id INTEGER PRIMARY KEY,
    food_name TEXT UNIQUE)"""

create_eats = """CREATE TABLE IF NOT EXISTS Eats (
    ID INTEGER NOT NULL PRIMARY KEY,
    Name TEXT NOT NULL,
    Price INTEGER NOT NULL,
    Description TEXT NOT NULL,
    idCategory TEXT REFERENCES Category (id) )"""

insert_category = """INSERT INTO category (name) VALUES (?)"""

insert_eats = """INSERT INTO eats (Name,Price,Description,idCategory) VALUES(?,?,?,?)"""


# create_main = """CREATE TABLE IF NOT EXISTS Main(
#    id INTEGER PRIMARY KEY,
#    login TEXT,
#    mail TEXT,
#    password TEXT,
#    avatar BOLD DEFAULT NULL)"""