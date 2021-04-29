import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

cloudinary.config(
    cloud_name=os.environ.get('CLOUD_NAME'),
    api_key=os.environ.get('API_KEY'),
    api_secret=os.environ.get('API_SECRET')
)

mongo = PyMongo(app)


# main home page
@app.route("/")
@app.route("/view_cocktails")
def view_cocktails():
    cocktails = list(mongo.db.cocktails.find())
    return render_template("cocktails.html", cocktails=cocktails)


# landing page
@app.route("/index")
def index():
    cocktails = list(mongo.db.cocktails.find())
    return render_template("index.html", cocktails=cocktails)


# about page
@app.route("/about")
def about():
    cocktails = list(mongo.db.cocktails.find())
    return render_template("about.html", cocktails=cocktails)


# search functionality
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    cocktails = list(mongo.db.cocktails.find({"$text": {"$search": query}}))
    return render_template("cocktails.html", cocktails=cocktails)


# register user functionality
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists. Please choose another username.")
            return redirect(url_for('register'))

        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        # prevents user from creating account if passwords do not match
        if password != confirm_password:
            flash("Please ensure that your passwords match.")
            return redirect(url_for("register"))
        if password == confirm_password:
            register = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password").lower())
                    }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for('profile', username=session["user"]))
    return render_template("register.html")


# login functionality
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get(
                    "password").lower()):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(
                        url_for('profile', username=session["user"]))
            else:
                # incorrect password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# user profile
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grabs the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


# logs user out of profile
@app.route("/logout")
def logout():
    # remove user from session cookies to allow for logout
    flash("You have successfully logged out!")
    session.pop("user")
    return redirect(url_for("login"))


# functionality to add new cocktail to db
@app.route("/add_cocktail", methods=["GET", "POST"])
def add_cocktail():
    if request.method == "POST":
        cocktail = {
            "category_name": request.form.get("category_name"),
            "cocktail_name": request.form.get("cocktail_name"),
            "cocktail_description": request.form.get("cocktail_description"),
            "cocktail_ingredients": request.form.get("cocktail_ingredients"),
            "cocktail_instructions": request.form.get("cocktail_instructions"),
            "cocktail_serving": request.form.get("cocktail_serving"),
            "created_by": session["user"],
            "cocktail_img": request.form.get("cocktail_img")
        }
        mongo.db.cocktails.insert_one(cocktail)
        flash("Cocktail Successfully Added")
        return redirect(url_for('view_cocktails'))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_cocktail.html", categories=categories)


#functionality to edit cocktails in db
@app.route("/edit_cocktail/<cocktail_id>", methods=["GET", "POST"])
def edit_cocktail(cocktail_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "cocktail_name": request.form.get("cocktail_name"),
            "cocktail_description": request.form.get("cocktail_description"),
            "cocktail_ingredients": request.form.get("cocktail_ingredients"),
            "cocktail_instructions": request.form.get("cocktail_instructions"),
            "cocktail_serving": request.form.get("cocktail_serving"),
            "created_by": session["user"],
            "cocktail_img": request.form.get("cocktail_img")
        }
        mongo.db.cocktails.update({"_id": ObjectId(cocktail_id)}, submit)
        flash("Cocktail Successfully Added")

    cocktail = mongo.db.cocktails.find_one({"_id": ObjectId(cocktail_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_cocktail.html", cocktail=cocktail, categories=categories)


# allows users to delete their submitted cocktails
@app.route("/delete_cocktail/<cocktail_id>")
def delete_cocktail(cocktail_id):
    mongo.db.cocktails.remove({"_id": ObjectId(cocktail_id)})
    flash("Cocktail Successfully Deleted")
    return redirect(url_for("view_cocktails"))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))

    if session["user"] == "admin".lower():
        return render_template("categories.html", categories=categories)
    else:
        return redirect(url_for("view_cocktails"))


# functionality to add categories to db
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    # restricts access of category crud functionality to admin only
    if session["user"] == "admin".lower():
        if request.method == "POST":
            category = {
                "category_name": request.form.get("category_name")
            }
            mongo.db.categories.insert_one(category)
            flash("New Category Added")
            return redirect(url_for('get_categories'))

        return render_template("add_category.html")
    else:
        return redirect(url_for("view_cocktails"))


# functionality to edit categories in db
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# allows user to delete categories
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
