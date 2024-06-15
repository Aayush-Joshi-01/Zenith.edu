from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

class test(Resource):
    def get(self):
        return {"status":"ok"}

api.add_resource(test,'/test')
if __name__ == '__main__':
    app.run(host='172.16.26.155', port=5000)