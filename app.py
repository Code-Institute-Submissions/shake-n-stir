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


@app.route("/")
@app.route("/view_cocktails")
def view_cocktails():
    cocktails = mongo.db.cocktails.find()
    return render_template("cocktails.html", cocktails=cocktails)


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
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grabs the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies to allow for logout
    flash("You have successfully logged out!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_cocktail", methods=["GET", "POST"])
def add_cocktail():
    if request.method == "POST":
        photo = request.files['cocktail_img']
        photo_upload = cloudinary.uploader.upload(
            photo, upload_preset="yxesuzpw")
        cocktail = {
            "category_name": request.form.get("category_name"),
            "cocktail_name": request.form.get("cocktail_name"),
            "cocktail_description": request.form.get("cocktail_description"),
            "cocktail_ingredients": request.form.get("cocktail_ingredients"),
            "cocktail_instructions": request.form.get("cocktail_instructions"),
            "cocktail_serving": request.form.get("cocktail_serving"),
            "created_by": session["user"],
            "cocktail_img": photo_upload['secure_url']
        }
        mongo.db.cocktails.insert_one(cocktail)
        flash("Cocktail Successfully Added")
        return redirect(url_for('view_cocktails'))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_cocktail.html", categories=categories)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
