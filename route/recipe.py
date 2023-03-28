# 레시피 전체 조회, 등록, 삭제, 수정
from flask import Blueprint, render_template, request, jsonify

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.er12y5s.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

blue_recipe = Blueprint("recipe", __name__, url_prefix="/recipe")

# 메인
@blue_recipe.route('/')
def home():
   return render_template('main.html')

# 없어도 될 것 같아요
@blue_recipe.route('/list', methods=['GET'])
def test_get():
   all_recipes = list(db.recipes.find({},{'_id':False}))
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
   name_receive = request.json['button_delete']
   db.recipes.delete_one({'name':name_receive})
   return jsonify({'msg':'삭제완료!'})
