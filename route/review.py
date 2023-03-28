from flask import Blueprint, Flask, render_template, request, jsonify
app = Flask(__name__)
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient('mongodb+srv://sparta:test@cluster0.cirioky.mongodb.net/?retryWrites=true&w=majority')
# client = MongoClient('mongodb+srv://sparta:test@cluster0.er12y5s.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

blue_review = Blueprint("review", __name__, url_prefix="/review")

@blue_review.route("/")
def home():
    return render_template('review.html')

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

@blue_review.route("/", methods=["PUT"])
def update():
    # recipe_id_receive = request.form['recipe_id']
    id_receive = request.form['id']
    under_id_receive = request.form['under_id']
    review_receive = request.form['review']
    
    doc = {
        'review':review_receive
        }
    db.review.update_one({'_id':ObjectId(under_id_receive)}, {'$set': doc})
    
    return jsonify({'msg':'수정완료!'})

@blue_review.route("/", methods=["DELETE"])
def review_delete():
    id_receive = request.form['id_give'] ## 댓글의 id
    under_id_receive = request.form['under_id_give']
    # session_id = 
    print(id_receive)
    print(session_id)
    if id_receive == session_id:
        db.review.delete_one({'_id':ObjectId(under_id_receive)})
        return jsonify({'msg':'삭제완료!'})
    else:
        return jsonify({'msg':'본인의 댓글만 삭제 가능합니다!'})
    