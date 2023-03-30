from flask import Blueprint, Flask, render_template, request, jsonify, redirect
app = Flask(__name__)
import requests, jwt
from bs4 import BeautifulSoup
from pymongo import MongoClient
from bson.objectid import ObjectId
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
    token_receive = request.cookies.get('mytoken')
    if token_receive is not None: # token 값이 있다면 (로그인 상태라면)
        recipe_id_receive = request.form['recipe_id']
        id_receive = request.form['id']
        review_receive = request.form['review']
    
        doc = {
            'recipe_id':recipe_id_receive,
            'id':id_receive,
            'review':review_receive
            }
        db.review.insert_one(doc)
        
        return jsonify({'msg':'저장 완료!', 'login':'true'})
    else: # token 값이 없다면 (로그아웃 상태라면)
        return jsonify({'msg':'먼저 로그인을 해주세요!', 'login':'false'})

# 리뷰 수정
@blue_review.route("/", methods=["PUT"])
def update():
    under_id_receive = request.form['under_id']
    id_receive = request.form['id']
    review_receive = request.form['review']

    token_receive = request.cookies.get('mytoken')
    try:
        if token_receive is not None: # token 값이 있다면 (로그인 상태라면)
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
            user_id = payload['id']
            if id_receive == user_id: # 로그인 사용자와 해당 리뷰를 남긴 사용자가 같으면
                doc = {
                    'review':review_receive
                }
                db.review.update_one({'_id':ObjectId(under_id_receive)}, {'$set': doc})
                return jsonify({'msg':'수정 완료!', 'login':'true'})
            else: # 다르면
                return jsonify({'msg':'본인이 작성한 리뷰만 수정 가능합니다!', 'login':'true'})
        else: # token 값이 없다면 (로그아웃 상태라면)
            return jsonify({'msg':'먼저 로그인을 해주세요!', 'login':'false'})
    except jwt.ExpiredSignatureError:
        return redirect("/recipe")
    except jwt.exceptions.DecodeError:
        return redirect("/recipe")

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

    # doc = {
    #         'review':review_receive
    # }
    # db.review.update_one({'_id':ObjectId(under_id_receive)}, {'$set': doc})
    # return jsonify({'msg':'수정완료!'})
    

# 리뷰 삭제
@blue_review.route("/", methods=["DELETE"])
def review_delete():
    id_receive = request.form['id_give'] ## 댓글의 id
    under_id_receive = request.form['under_id_give']

    token_receive = request.cookies.get('mytoken')
    try:
        if token_receive is not None: # token 값이 있다면 (로그인 상태라면)
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
            user_id = payload['id']
            if id_receive == user_id: # 로그인 사용자와 해당 리뷰를 남긴 사용자가 같으면
                db.review.delete_one({'_id':ObjectId(under_id_receive)})
                return jsonify({'msg':'삭제 완료!', 'login':'true'})
            else: # 다르면
                return jsonify({'msg':'본인이 작성한 리뷰만 삭제 가능합니다!', 'login':'true'})
        else: # token 값이 없다면 (로그아웃 상태라면)
            return jsonify({'msg':'먼저 로그인을 해주세요!', 'login':'false'})
    except jwt.ExpiredSignatureError:
        return redirect("/recipe")
    except jwt.exceptions.DecodeError:
        return redirect("/recipe")