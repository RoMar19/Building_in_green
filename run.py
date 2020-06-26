import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
# MONGO_URI import for workspace
from os import path
if path.exists("env.py"):
    import env

# Start application 

app = Flask(__name__)
app.config["MONGODB_NAME"] = os.environ.get("MONGODB_NAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

coll = mongo.db

# Shows Home page

@app.route('/')
def index():
    categories = mongo.db.categories.find()
    return render_template("index.html", page_title="Home", categories=categories)
    



# Shows all houses in the gallery(DB) by category selection. (READ)
@app.route('/gallery/<selected_category>')
def gallery(selected_category):
    if selected_category == "all":
        houses = mongo.db.houses.find()
    else: 
        houses = mongo.db.houses.find(
            { "category_name": selected_category }
        )
    return render_template("gallery.html",
                          houses=houses,
                          page_title=selected_category.capitalize() + "Green Buildings")

# Shows details of the selected house the Gallery.
@app.route('/house_detail/<house_id>')
def house_detail(house_id):
    house = mongo.db.houses.find_one({"_id": ObjectId(house_id)})
    return render_template("house_detail.html",
                          house=house,
                          page_title="Green building Info.")                          
                     

# Shows form page to add new houses of the users to the Gallery of the Comunity(DB).
@app.route('/add_house')
def add_house():
    categories = mongo.db.categories.find()
    category_name = [category for category in categories]
    return render_template("add_house.html",
                            categories=category_name,
                            page_title="Add Your Own Green Building")

# Inserts/add new houses to the DB after fill in Form add_house. (CREATE)
@app.route('/insert_house', methods=["POST"])
def insert_house():
    houses = mongo.db.houses

    form_data = request.form.to_dict()
    house_details = houses.insert_one(
    {
    "category_name": form_data["category_name"],
    "user_name": form_data["user_name"],
    "location": form_data["location"],
    "year": form_data["description"],
    "house_name": form_data["house_name"],
    "image": form_data["image"],
    "description": form_data["description"]
    }
    )

    return redirect(url_for("house_detail",
                            house_id=house_details.inserted_id))                        



# Edit_house page, providing data from formfield values. (EDIT)
@app.route('/edit_house/<house_id>')
def edit_house(house_id):
    house = mongo.db.houses.find_one({"_id": ObjectId(house_id)})
    categories = mongo.db.categories.find()
    return render_template("edit_house.html",
                            house=house,
                            categories=categories,
                            page_title="Edit Green Building")


# Updates house info. in the DB after changes of the user. (UPDATE)
@app.route('/update_house/<house_id>', methods=["POST"])
def update_house(house_id):
    houses = mongo.db.houses

    form_data = request.form.to_dict()

    houses.update({"_id": ObjectId(house_id)},
                {
                "category": form_data["category_name"],
                "user_name": form_data["user_name"],
                "location": form_data["location"],
                "year": form_data["description"],
                "house_name": form_data["house_name"],
                "image": form_data["image"],
                "description": form_data["description"]
                }
                )

    return redirect(url_for("house_detail",
                            house_id=house_id))


# Deletes selected house from DB with alert. (DELETE)
@app.route('/delete_house/<house_id>')
def delete_house(house_id):
    mongo.db.houses.remove({"_id": ObjectId(house_id)})
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP", "0.0.0.0"),
            port=int(os.environ.get("PORT", 5000)),
            debug=False)