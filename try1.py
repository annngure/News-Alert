# from flask import Flask,render_template

# app = Flask(__name__)

# @app.route("/")#URL is bound with homepage.
# def index():

#         if __name__=='__main__':
#             app.run(debug=True)
from app import app
if __name__ == "__main__":
    app.run(debug=True)