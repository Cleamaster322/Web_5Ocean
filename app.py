from flask import Flask, render_template,redirect,session,request,url_for
from db.database import Database

menu = [{"name":"Крабы","url":"crabs"},
        {"name":"Холодные напитки","url":"cold-drinks"},
        {"name":"Салаты","url":"salads"},
        ]

app = Flask(__name__)

app.config['SECRET_KEY'] = "dasfdsfhgskdjfsdkjlgfsdlkfhd"

DATABASE = "db/5_Ocean.db"

db = Database(DATABASE)
db.init_db()
# count = db.get_colons()
# print(count)
# db.add_food("dasd",3020,"dsad",1)
@app.route("/")
@app.route("/main", methods = ["POST","GET"])
def index():
    categorys = db.select_all_categorys_Foods()
    if request.method == "POST":
        print(request.form)
        # db.add_food(request.form["food_name"],request.form["Price"],request.form["Description"],request.form["idCategory"])
    return render_template('index.html',categorys = categorys, lenght = len(categorys))

@app.route("/categorys")
def categorys():
    categorys = db.select_all_categorys_Foods()
    return render_template('categorys.html',categorys = categorys)
    
@app.route("/categorysandfood")
def categorysandfood():
    categorysandfood = db.select_category_and_food()
    return render_template('categorysandfood.html',categ = categorysandfood)

@app.route("/menu/<category>")
def menu(category):
    categorysAll = db.select_all_categorys_Foods()
    foodInfoAll = db.select_food_full_info()
    return  render_template("menu.html",categoryName = category,categorysAll=categorysAll,foodInfoAll=foodInfoAll)

@app.route("/desc")
def desc():
    return render_template("desc.html")

@app.route("/reserve")
def reserve():
    return render_template("reserve.html")

@app.route("/admins", methods = ["POST", "GET"])
def admins():
    if request.method == "POST":
        # print(request.form)
        category = db.select_one_category(request.form["categoryName"].lower())
        if category == -1:
            db.insert_category(request.form["categoryName"].lower())
    return render_template("admins.html", menu = menu)

# if __name__ =="__main__":
#     app.run(debug = True)