# import pymongo
#
# class Mymongo:
#     def __init__(self,):
#         self.client = pymongo.Mongoclient()
#         self.db = self.client[db]
#         self.collection = self.db[collection]
import pymongo
# 建立连接
client = pymongo.MongoClient()
# 连接数据库
db = client['python']
# 连接集合
my_cool = db['hhh']
# 插入数据
my_cool.insert_many([{'name': 'al', 'age': 18}, {'name': 'al', 'age': 18}])
# 查询一个数据
www = my_cool.find_one()
print(www)
# 查询多个数据
# qqq = my_cool.find()
# for i in qqq:
#     print(i)
# 改变数据
# my_cool.update_one({'name': 'al'}, {"$set": {"age": 19}})
# qqq = my_cool.find_one()
# print(qqq)
# 删除数据
# my_cool.delete_one({'name': 'al'})










