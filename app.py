from flask import Flask, send_from_directory,request
from flask_restful import Api, Resource, reqparse
#from flask_cors import CORS #comment this on deployment
# from api.HelloApiHandler import HelloApiHandler
from flask_cors import CORS
# from scripts import translated_text

app = Flask(__name__)
CORS(app) #comment this on deployment
api = Api(app)

# print("hello")

@app.route("/", defaults={'path':''}, methods=['POST', 'GET','OPTIONS'])
def serve(path):
    return "Success"

@app.route('/test', methods=['GET'])
def test():
    testdata = {'data': [12, 19, 3], 'bardata': {'Hazardous': [12, 17, 3, 9, 7, 10], 'Dry Waste': [5, 4, 6, 11, 15, 13], 'Biodegradable': [7, 6, 5, 4, 10, 12]}, 'Linedata': {'Waste Limit': [30,30,30,30,30,30], 'Total waste': [0,0,0,0,0,0]}}
    # for i in range(0, len(testdata['bardata']['Hazardous'])):
    #     testdata['Linedata']['Waste Limit'][i] = 30

    for ei, i in enumerate(testdata['bardata']['Hazardous']):
        for ej, j in enumerate(testdata['bardata']['Dry Waste']):
            for ek, k in enumerate(testdata['bardata']['Biodegradable']):
                if ei==ej and ej==ek:
                        testdata['Linedata']['Total waste'][ei] = i+j+k
    return testdata
# @app.route('/test', methods=['GET', 'POST'])
# def analyze_data():
#     if request.method == 'POST':
#         print("hello")
#         f = request.files['file']
#         # f.save()
#         return "test"

# api.add_resource(HelloApiHandler, '/flask/hello')
