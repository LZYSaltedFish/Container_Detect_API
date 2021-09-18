from flask import Flask, request, make_response, jsonify, Blueprint
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

datas = [{'id': 1, 'name': 'lzy', 'age': 22}, {'id': 2, 'name': 'abc', 'age': 23}]

@app.route('/user', methods=['GET'])
def get_data():
    return {'code': 200, 'msg': 'success', 'data': datas}

if __name__ == '__main__':
    app.run()