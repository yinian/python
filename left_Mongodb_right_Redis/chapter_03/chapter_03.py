from pymongo import MongoClient
client = MongoClient('mongodb://root:root@127.0.0.1:27017')
database = client.test
collection = database.users
from bson import ObjectId
# rows = collection.find({'email': '135@qq.com'})

# for row in rows:
#     print(row)

# result = collection.update_many({
#     'email': '135@qq.com'
# }, {'$set': {
#     'name': '二二'
# }})

# collection.insert_many([{
#     'name': 'name1',
#     'email': '1001@1.com',
#     'date': '2019-05-03 01:21:21.49'
# }, {
#     'name': 'name2',
#     'email': '1002@1.com',
#     'date': '2019-05-03 01:21:21.49'
# }, {
#     'name': 'name3',
#     'email': '1003@1.com',
#     'date': '2019-05-03 01:21:21.49'
# }, {
#     'name': 'name4',
#     'email': '1004@1.com',
#     'date': '2019-05-03 01:21:21.49'
# }])

# # 查询 为空
# noneRows = collection.find({'password': None})
# for row in noneRows:
#     print(row)

# # 查询 布尔值
# booleanRows = collection.find({'password': True})
# for row in noneRows:
#     print(row)
# # 排序
# sortRows = collection.find({'password': None}).sort('name', -1)
# for row in sortRows:
#     print(row)
# 根据_id来查
idRows = collection.find({'_id': ObjectId('5cf84e13e45f243c9c96edb9')})
for row in idRows:
    print(row)
'''
读取数据库方式二：
database=client['chapter_3']
collection = client['example_data_3']


方式二：
database_name_list = ['develop_env_alpha','develop_env_beta','develop_env_preflight']
for each_db in database_name_list:
    database = client[each_db]
    collection = database.account

'''
