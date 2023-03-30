# 전체 메인
from flask import Flask, render_template
from route import recipe
from route import review
from route import user

application = app = Flask(__name__)

app.register_blueprint(user.blue_user)
app.register_blueprint(recipe.blue_recipe)
app.register_blueprint(review.blue_review)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':  
   app.run()