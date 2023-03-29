from flask import Blueprint, Flask, render_template, request, jsonify, redirect
app = Flask(__name__)
import requests, jwt
from bs4 import BeautifulSoup
from pymongo import MongoClient
from bson.objectid import ObjectId
# client = MongoClient('mongodb+srv://sparta:test@cluster0.cirioky.mongodb.net/?retryWrites=true&w=majority')
client = MongoClient('mongodb+srv://sparta:test@cluster0.er12y5s.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta
SECRET_KEY = 'recipe'

blue_review = Blueprint("review", __name__, url_prefix="/review")

@blue_review.route("/")
def home():
    return render_template('review.html')

# 리뷰 등록
@blue_review.route("/", methods=["POST"])
def add():
    recipe_id_receive = request.form['recipe_id']
    id_receive = request.form['id']
    review_receive = request.form['review']
    
    doc = {
        'recipe_id':recipe_id_receive,
        'id':id_receive,
        'review':review_receive
        }
    db.review.insert_one(doc)
    
    return jsonify({'msg':'저장완료!'})

# 리뷰 수정
@blue_review.route("/", methods=["PUT"])
def update():
    under_id_receive = request.form['under_id']
    id_receive = request.form['id']
    review_receive = request.form['review']

    # token_receive = request.cookies.get('mytoken')
    # try:
    #      payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
    #      print("------------------------"+payload)
    # except jwt.ExpiredSignatureError:
    #     return redirect("http://localhost:5000/recipe")
    # except jwt.exceptions.DecodeError:
    #     return redirect("http://localhost:5000/recipe")

    # if id_receive == session_id:
    #     doc = {
    #         'review':review_receive
    #     }
    #     db.review.update_one({'_id':ObjectId(under_id_receive)}, {'$set': doc})
    #     return jsonify({'msg':'수정완료!'})
    # else:
    #     return jsonify({'msg':'본인의 댓글만 수정 가능합니다!'})

    # token_receive = request.cookies.get('mytoken')
    # print(token_receive)
    # try:
    #     payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
    #     user_info = db.user.find_one({"id": payload['id']})
    #     doc = {
    #         'review':review_receive
    #     }
    #     db.review.update_one({'_id':ObjectId(under_id_receive)}, {'$set': doc})
    #     return jsonify({'msg':'수정완료!'})
    # except jwt.ExpiredSignatureError:
    #     print("로그인 시간 만료")
    #     return redirect("/user/signin")
    # except jwt.exceptions.DecodeError:
    #     print("로그인 정보 잘못됨")
    #     return redirect("/user/signin")

    doc = {
            'review':review_receive
    }
    db.review.update_one({'_id':ObjectId(under_id_receive)}, {'$set': doc})
    return jsonify({'msg':'수정완료!'})
    

# 리뷰 삭제
@blue_review.route("/", methods=["DELETE"])
def review_delete():
    id_receive = request.form['id_give'] ## 댓글의 id
    under_id_receive = request.form['under_id_give']

    # print(session_id)
    # if id_receive == session_id:
    #     db.review.delete_one({'_id':ObjectId(under_id_receive)})
    #     return jsonify({'msg':'삭제완료!'})
    # else:
    #     return jsonify({'msg':'본인의 댓글만 삭제 가능합니다!'})
    
    db.review.delete_one({'_id':ObjectId(under_id_receive)})
    return jsonify({'msg':'삭제완료!'})
    