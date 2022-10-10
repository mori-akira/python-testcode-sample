from pymongo import MongoClient

with MongoClient('mongodb://localhost:27017') as client:
    # database
    db = client.get_database('test_database')
    # collection
    collection = db.get_collection('test_collection')

    # 全件取得
    print([value for value in collection.find()])
    # 条件指定で取得
    print([value for value in collection.find({'data1': 'hoge'})])
    # 条件を満たす1件取得
    from bson.objectid import ObjectId
    print(collection.find_one({'_id': ObjectId('634297cae34bf135726c554d')}))

    # 1件登録
    result = collection.insert_one({'data1': 'hogehoge', 'data2': 'fugafuga'})
    print(result.inserted_id)
    # 複数件登録
    result = collection.insert_many([{'data': 'abc'}, {'data': '123'}, {'data': 'あいう'}])
    print(result.inserted_ids)

    # 1件更新
    result = collection.update_one({'data': 'abc'}, {'$set': {'data': 'ABC'}})
    print(result.matched_count)
    # 全件更新
    result = collection.update_many({'data': '123'}, {'$set': {'data': '１２３'}})
    print(result.matched_count)

    # 1件削除
    result = collection.delete_one({'data': 'ABC'})
    print(result.deleted_count)
    # 全件削除
    result = collection.delete_many({'data': '１２３'})
    print(result.deleted_count)

    print(collection.find_one({'$and': [{'data1': 'hoge'}, {'data2': 'fuga'}]}))
    print(collection.find_one({'$or': [{'data1': 'hogee'}, {'data2': 'fuga'}]}))

    # 部分一致
    print(collection.find_one({'data1': {'$regex': 'og'}}))
    # 前方一致
    print(collection.find_one({'data1': {'$regex': '^ho'}}))
    # 後方一致
    print(collection.find_one({'data1': {'$regex': 'ge$'}}))

    # 大なり
    print(collection.find_one({'data': {'$gt': 12345}}))
    # 大なりイコール
    print(collection.find_one({'data': {'$gte': 12345}}))
    # 小なり
    print(collection.find_one({'data': {'$lt': 12345}}))
    # 小なりイコール
    print(collection.find_one({'data': {'$lte': 12345}}))

    # $型演算子 (文字列)
    print(collection.find_one({'data': {'$type': 2}}))
    # $型演算子 (オブジェクト)
    print(collection.find_one({'data': {'$type': 3}}))

