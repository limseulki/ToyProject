# 전체 메인
from flask import Flask
from route.recipe import blue_recipe

app = Flask(__name__)

app.register_blueprint(blue_recipe)

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)
