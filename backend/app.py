from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={
            r"*": {"origins": "http://localhost:3000"}})

@app.route('/', methods=['POST'])
# #@cross_origin()
def send_mail():

