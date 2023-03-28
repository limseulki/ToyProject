from flask import Blueprint, Flask, render_template, request, jsonify
app = Flask(__name__)
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient('mongodb+srv://sparta:test@cluster0.cirioky.mongodb.net/?retryWrites=true&w=majority')
# client = MongoClient('mongodb+srv://sparta:test@cluster0.er12y5s.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

blue_recipe = Blueprint("main", __name__, url_prefix="/")

# @blue_recipe.route("/")
# def home():
#     all_recipes = []
#     recipes = list(db.bucket.find({}))
#     for recipe in recipes:
#         recipe['_id'] = str(recipe['_id'])
#         all_recipes.append(recipe)
#     return render_template('main.html', all_recipes=all_recipes)


# @blue_recipe.route("/")
# def recipe():
#     all_recipes = list(db.bucket.find({}))
#     print(all_recipes)
#     num = 1
#     return render_template('recipe.html', num=num)

@blue_recipe.route("/recipe/1")
def detail():
    id = db.movies.find_one({'_id':ObjectId('64228cd1651170aa61050baa')})
    reviews = list(db.review.find({'recipe_id':'1'}))
    print(reviews)
    return render_template('recipe.html', id=id, reviews=reviews)