# 레시피 전체 조회, 등록, 삭제, 수정
from flask import Blueprint, Flask, render_template, request, jsonify
app = Flask(__name__)
from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.er12y5s.mongodb.net/?retryWrites=true&w=majority')
# client = MongoClient('mongodb+srv://sparta:test@cluster0.cirioky.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

import requests
from bs4 import BeautifulSoup
from bson.objectid import ObjectId

blue_recipe = Blueprint("recipe", __name__, url_prefix="/recipe")

# 메인
@blue_recipe.route('/')
def home():
   
#    all_recipes = list(db.recipes.find({}))
#    for i in all_recipes:
#       print(i['_id'])

   return render_template('main.html')

# 없어도 될 것 같아요
@blue_recipe.route('/list', methods=['GET'])
def test_get():
   
   all_recipes = []
   recipes = list(db.recipes.find({}))
   for recipe in recipes:
      recipe['_id'] = str(recipe['_id'])
      all_recipes.append(recipe)

   return jsonify({'result':all_recipes})

# 레시피 등록 get
@blue_recipe.route('/update', methods=['GET'])
def test_update():
   return render_template('update.html')

# 레시피 등록 post
@blue_recipe.route("/update", methods=["POST"])
def recipe_post():
    url_receive = request.form['url_give']
    name_receive = request.form['name_give']
    recipe_receive = request.form['recipe_give']

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    ogimage = soup.select_one('meta[property="og:image"]')['content']

    doc = {
        'image':ogimage,
        'name':name_receive,
        'recipe':recipe_receive
    }

    db.recipes.insert_one(doc)

    return jsonify({'msg':'저장완료!'})

# 레시피 삭제 delete
@blue_recipe.route('/delete', methods=['DELETE'])
def recipe_delete():
   
   # name_receive = request.json['button_delete']
   # db.recipes.delete_one({'name':name_receive})
   id_receive = request.form['id']
   under_id_receive = request.form['under_id']
   print(id_receive)
   print(under_id_receive)
#    db.recipes.delete_one({'_id':ObjectId(under_id_receive)})

   return jsonify({'msg':'삭제완료!'})

#레시피 수정 put
@blue_recipe.route('/put', methods=['PUT'])
def recipe_put():
   name_receive = request.json['button_modify']
   image_receive = request.json['image_give']
   recipe_receive = request.json['recipe_give']

   print(name_receive, image_receive, recipe_receive)
   # db.recipes.update_one({'name':name_receive},{'$set':{'name':name_receive}})
   # db.recipes.update_one({'name':name_receive},{'$set':{'image':image_receive}})
   # db.recipes.update_one({'name':name_receive},{'$set':{'recipe':recipe_receive}})
   # print(name_receive, image_receive, recipe_receive)
   return jsonify({'msg':'수정완료!'})





# @blue_recipe.route("/1")
# def detail():
#     id = db.movies.find_one({'_id':ObjectId('64228cd1651170aa61050baa')})
#     reviews = list(db.review.find({'recipe_id':'1'}))
#     print(reviews)
#     return render_template('recipe.html', id=id, reviews=reviews)

# 레시피 상세 페이지
@blue_recipe.route("/<under_id>")
def detail(under_id):
    id = db.recipes.find_one({'_id':ObjectId(under_id)})
    reviews = list(db.review.find({'recipe_id':under_id}))
    print(reviews)
    return render_template('recipe.html', id=id, reviews=reviews)