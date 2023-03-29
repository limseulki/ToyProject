# 전체 메인
from flask import Flask
from route import recipe
from route import review
from route import user

app = Flask(__name__)

app.register_blueprint(recipe.blue_recipe)
app.register_blueprint(review.blue_review)
app.register_blueprint(user.blue_user)

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)