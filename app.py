from flask import Flask, render_template,redirect,session
from db.database import Database

menu = [{"name":"Крабы","url":"crabs"},
        {"name":"Холодные напитки","url":"cold-drinks"},
        {"name":"Салаты","url":"salads"},
        ]

app = Flask(__name__)

DATABASE = "db/5_Ocean.db"

db = Database(DATABASE)
db.init_db()

# count = db.get_colons()
# print(count)
db.add_food("dasd",3020,"dsad",1)

@app.route("/")
def index():
    return render_template('base.html', menu = menu)

@app.route("/crabs")
def crabs():
    return render_template("crabs.html", menu = menu)

if __name__ =="__main__":
    app.run(debug = True)
