from flask import Flask
from flask import request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017')
db = client.get_database('test_database')
collection = db.get_collection('flask_api_test')

@app.route('/list', methods=['GET'])
def get_list():
    data = [doc for doc in collection.find()]
    return {'data': remove_objectid(data)}

@app.route('/list/id', methods=['GET'])
def get_id_list():
    return {'data': [doc['id'] for doc in collection.find()]}

@app.route('/list/name', methods=['GET'])
def get_name_list():
    return {'data': [doc['name'] for doc in collection.find()]}

@app.route('/detail', methods=['GET'])
def get_detail_query():
    query = request.args
    return {'data': remove_objectid(collection.find_one({'id': query.get('id')}))}

@app.route('/detail/<id>', methods=['GET'])
def get_detail_path(id):
    return {'data': remove_objectid(collection.find_one({'id': id}))}

@app.route('/add', methods=['POST'])
def add():
    body = request.json
    result = collection.insert_one({'id': body.get('id'), 'name': body.get('name')})
    return {'data': {'result': str(result.inserted_id)}}

def remove_objectid(tar):
    if type(tar) is list:
        for t in tar:
            del t['_id']
    elif type(tar) is dict:
        del tar['_id']
    else:
        pass
    return tar

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    finally:
        client.close()