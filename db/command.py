create_category = """CREATE TABLE IF NOT EXISTS Category(
    id INTEGER PRIMARY KEY,
    food_name TEXT UNIQUE)"""

create_eats = """CREATE TABLE IF NOT EXISTS Eats (
    ID INTEGER NOT NULL PRIMARY KEY,
    Name TEXT NOT NULL,
    Price INTEGER NOT NULL,
    Description TEXT NOT NULL,
    idCategory TEXT REFERENCES Category (id) )"""

insert_category = """INSERT INTO category (nameCat) VALUES (?)"""

insert_eats = """INSERT INTO eats (Name,Price,Description,idCategory) VALUES(?,?,?,?)"""

select_all_categorys_Foods = """SELECT Name FROM SubCategory WHERE categoryid = 1"""

select_category = """SELECT NameCat From Category WHERE nameCat = ?"""

select_categorys_and_food = """SELECT category.NameCat,eats.NameFood  FROM Category LEFT JOIN
Eats ON Eats.idCategory = Category.id
order by category.id"""

select_category_and_his_food = """SELECT category.NameCat,eats.NameFood  FROM Category JOIN Eats ON Eats.idCategory = Category.id WHERE category.NameCat = ? """

select_food_info = """SELECT Eats.NameFood,Eats.proteins,Eats.fats,Eats.carbohydrates,Eats.kilocolories FROM Eats"""

select_food_disc = """SELECT Eats.NameFood, Eats.Description FROM Eats"""


select_food_full_info = """SELECT   Eats.ID,
                                    Eats.NameFood,
                                    Eats.Description,
                                    Eats.CookingMethod,
                                    Eats.FoodValue,
                                    Eats.Price,
                                    Eats.proteins,
                                    Eats.fats,
                                    Eats.carbohydrates,
                                    Eats.kilocolories,
                                    Eats.imgPath,
SubCategory.Name FROM Eats LEFT join SubCategory on eats.idSubCategory = SubCategory.id """

select_category_bar = """SELECT NameCat FROM Category WHERE NameCat != 'блюда' """

select_subCategory_bar = """SELECT Name FROM SubCategory where SubCategory.CategoryId = (SELECT id FROM Category WHERE NameCat = ?)"""

select_full_bar = """SELECT Drinks.id,
                            Drinks.Name,
                            Drinks.Volume, 
                            Drinks.Price, 
                            Drinks.protein, 
                            Drinks.fats, 
                            Drinks.Carbohydrates, 
                            Drinks.kilocalories, 
                            Drinks.structure, 
                            SubCategory.Name as NameSubCat, 
                            Category.NameCat 
FROM Drinks LEFT JOIN SubCategory ON Drinks.idSubCategory = SubCategory.id LEFT JOIN Category ON Subcategory.CategoryId = category.id Where NameCat = ? """

# create_main = """CREATE TABLE IF NOT EXISTS Main(
#    id INTEGER PRIMARY KEY,
#    login TEXT,
#    mail TEXT,
#    password TEXT,
#    avatar BOLD DEFAULT NULL)"""