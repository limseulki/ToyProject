import hashlib      # 복호화 관련 라이브러리
import jwt
import datetime  # 쿠키 세션만료를 위한 시간 데이터 관련
from datetime import datetime, timedelta # 쿠키 세션만료를 위한 시간 데이터 관련
from werkzeug.utils import secure_filename

from pymongo import MongoClient
import certifi

from flask import Flask, render_template, request, jsonify, redirect, Blueprint, url_for, make_response
# app = Flask(__name__)

# client = MongoClient(
#     'mongodb+srv://sparta:test@cluster0.bka3lk3.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=certifi.where())
client = MongoClient('mongodb+srv://sparta:test@cluster0.cirioky.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# ca = certifi.where()


# 전역 변수
SECRET_KEY = 'recipe'


blue_user = Blueprint("user", __name__, url_prefix="/user")
# @blue_user.route("/signin")
# def signin():
#     return render_template('signin.html')


# @blue_user.route("/signup")
# def signup():
#     return render_template('signup.html')


# @ blue_user.route('/main', methods=['GET', 'POST'])
# def home():
#     token_receive = request.cookies.get('mytoken')
#     print(token_receive)
#     try:
#         payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
#         user_info = db.user.find_one({"id": payload['id']})
#         return render_template('main.html')
#     except jwt.ExpiredSignatureError:
#         print("로그인 시간 만료")
#         return redirect("signin.html")
#     except jwt.exceptions.DecodeError:
#         print("로그인 정보 잘못됨")
#         return redirect("signin.html")


@ blue_user.route("/signup", methods=["POST"])
def signup():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    name_receive = request.form['name_give']
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
    doc = {
        "id": id_receive,  # 아이디
        "pw": pw_hash,  # 비밀번호
        "name": name_receive  # 비밀번호
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '회원가입 성공!'})
    # id_receive = request.form['id_give']
    # pw_receive = request.form['pw_give']
    # name_receive = request.form['name_give']
    # print(id_receive,  pw_receive, name_receive)
    # # id = request.json.get('id')
    # # pw = request.json.get('pw')
    # # name = request.json.get('name')
    
    # # 복호화 비밀번호 digest(바이트 문자열) 또는 hexdigest(바이트 -> 16진수 문자열)  - 해싱코드 문자열 리턴
    # pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    # doc = {
    #     'id': id_receive,
    #     'pw': pw_hash,
    #     'name': name_receive
    # }
    # # insert 전 동일 id 검사
    # # chk = db.user.find_one({'id': id})

    # # if chk is None:
    # db.user.insert_one(doc)
    # return jsonify({'msg': '회원가입 완료!'})
    # # else:
    # #     return jsonify({'msg': '회원가입 실패!'})


@ blue_user.route("/signin", methods=["POST"])
def api_login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'id': id_receive, 'pw': pw_hash})

    if result is not None:
        payload = {
            'id': id_receive,
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jsonify({'result': 'success', 'token': token, 'msg': '환영합니다!'})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})
    # id_receive = request.form['id_give']
    # pw_receive = request.form['pw_give']
    # # 복호화 비밀번호 digest(바이트 문자열) 또는 hexdigest(바이트 -> 16진수 문자열)  - 해싱코드 문자열 리턴
    # pwd_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
    # chk = db.user.find_one({'id': id_receive, 'pw': pwd_hash})
    # # print(chk)
    # if chk is not None:
    #     # jwt 토큰 관련
    #     payload = {
    #         'id': id_receive,
    #         # 'iss': 'issuer',
    #         # 'sub': 'jwtTestToken',
    #         # 'aud': 'http://localhost:5000/',
    #         # 'iat': datetime.datetime.utcnow(),
    #         # (seconds=60 * 60 * 5)  # 5시간 유지
    #         'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * 60)
    #     }
    #     # jwt를 암호화
    #     # print(SECRET_KEY)
    #     # token = jwt.encode({"some": "payload"}, private_key, algorithm="ES256")
    #     token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    #     # response = make_response(redirect(url_for('/recipe/')))
    #     # response.set_cookie('mytoken', token)
    #     # print(token)
    #     # return response
    #     return jsonify({'msg': '로그인 성공', 'flag': 'true', 'mytoken': token})
    # else:
    #     return jsonify({'msg': '로그인 실패 : ID/PW를 확인하세요!', 'flag': 'false'})


@ blue_user.route('/signup/checkup', methods=['POST'])
def check_up():
    id_receive = request.form['id_give']
    exists = bool(db.users.find_one({"id": id_receive}))
    # 찾아서 하나라도 있으면 T 없으면 F
    return jsonify({'result': 'success', 'exists': exists})


@ blue_user.route('/signup/checkup2', methods=['POST'])
def check_up2():
    name_receive = request.form['name_give']
    exists = bool(db.users.find_one({"name": name_receive}))
    # 찾아서 하나라도 있으면 T 없으면 F
    return jsonify({'result': 'success', 'exists': exists})


@ blue_user.route("/users", methods=["GET"])
def signup_form():
    return render_template('users.html')


@blue_user.route('/signout', methods=['GET'])
def logout():
    response = make_response(redirect(url_for('/user/users')))
    response.set_cookie('mytoken', '', expires=0)
    return render_template('users.html')

@blue_user.route("/expired", methods=["GET"])
def token_exp():
    return render_template('expired.html')


# if __name__ == '__main__':
#     app.run('0.0.0.0', port=5000, debug=True)