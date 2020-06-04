import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# Start application 

app = Flask(__name__)

app.config["MONGODB_NAME"] = 'green_buildings'
app.config["MONGODB_URI"] = 'mongodb+srv://RoMar19:CodeStudent@cluster0-oourq.mongodb.net/green_buildings?retryWrites=true&w=majority'

mongo = PyMongo(app)

# Shows Home page

@app.route('/')
def index():
    return render_template("index.html", page_title="Home")

# Shows all houses of DB
@app.route('/all_gallery')
def all_gallery():
    houses = mongo.db.houses.find()
    return render_template ('all_gallery.html', houses=houses)

# Shows all houses in the gallery(DB) by category selection
@app.route('/gallery/<select_category>')
def gallery(select_category):
    selected_gallery = mongo.db.houses.find()
    return render_template('gallery.html', 
                          houses=selected_gallery,
                          select_category=select_category,
                          page_title=select_category + "Green Buildings")

# Shows details of the selected house with butons to Edit or Delete 
@app.route('/house_detail/<house_id>')
def house_detail(house_id):
    house_details = mongo.db.houses.find_one({"_id": ObjectId(house_id)})
    return render_template('house_detail.html',
                          houses=house_details,
                          page_title="Green building Info.")                          
                     

# Shows form page to add new houses of the users to the Gallery of the Comunity(DB) 
@app.route('/add_house')
def add_house():
    house_categories = mongo.db.categories.find()
    return render_template('add_house.html', 
                        categories=house_categories,
                        page_title="Add Your Own Green Building")

# Inserts new houses to the DB after fill in Form add_house and press button
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



# Edit_house page, providing data from formfield values
@app.route('/edit_house/<house_id>')
def edit_house(house_id):
    house_details = mongo.db.houses.find_one({"_id": ObjectId(house_id)})
    house_categories = mongo.db.categories.find()
    return render_template('edit_house.html',
                            houses=house_details,
                            categories= house_categories,
                            page_title="Edit")


# Updates house info. in the DB after changes of the user
@app.route('/update_house/<house_id>', methods=["POST"])
def update_house(house_id):
    houses = mongo.db.houses

    form_data = request.form.to_dict()

    houses.update({"_id": ObjectId(house_id)},
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

    return redirect(url_for('house_detail',
                            house_id=house_id))


# Deletes selected house from DB with alert
@app.route('/delete_house/<house_id>')
def delete_house(house_id):
    mongo.db.houses.remove({"_id": ObjectId(house_id)})
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP", "0.0.0.0"),
            port=int(os.environ.get("PORT", "5000")),
            debug=True)