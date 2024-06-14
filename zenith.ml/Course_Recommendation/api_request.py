from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

class test(Resource):
    def get(self):
        return {"status":"ok"}


if __name__ == '__main__':
    app.run(debug=True, host='192.168.137.1', port=5000)