from flask import Flask, render_template, jsonify
from flask_cors import CORS
from flask_restful import Api
from sqlalchemy import create_engine
from sqlalchemy import text
import json

app = Flask(__name__)
api = Api(app)
CORS(app)


@app.route('/')
def hello_world():

    # DATABASE_URL  = 'mysql+mysqldb://admin:12345678@flask-backend.ckxv07dhtiyg.ap-northeast-1.rds.amazonaws.com:3306/'
    # engine = create_engine(DATABASE_URL, pool_recycle=280)
    # #with engine.connect() as connection:
    # engine.connect().execute("use flaskbackend")
    # query = text("SELECT * FROM ecdsa")
    # blog_posts = engine.connect().execute(query)
    # x = []
    # for post in blog_posts:
    #     x.append(post)
    # print(x)
    return str('abc')


if __name__ == '__main__':
    app.run(debug=False)