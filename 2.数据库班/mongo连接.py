import pymongo
class Mymongo:
    def __init__(self, db, collection):
        #建立连接
        self.lianjie = pymongo.MongoClient()
        #连接数据库
        self.db = self.lianjie[db]
        #连接集合
        self.collection = self.db[collection]

    def insert(self, date, insert_var=True):
        if insert_var:
            self.collection.insert_one(date)        #增
        else:
            self.collection.insert_many(date)

    def find(self, find_var=True):
        if find_var:
            result = self.collection.find_one()
            print(result)
        else:
            result = self.collection.find()            #查
            for i in result:
                print(i)

    def update(self, date, new_date, update_var=True):
        if update_var:
            self.collection.update_one(date, {'$set': new_date})     #改
        else:
            self.collection.update_many(date, {'$set': new_date})

    def delete(self, date, del_val=True):
        if del_val:
            self.collection.delete_one(date)      #删
        else:
            self.collection.delete_many(date)

m = Mymongo('python', 'hhh')
m.insert([
    {'name': 'al'},
    {'age': 19}
], insert_var=False)
# m.find(find_var=False)
#m.insert([{'name': 'yydal', 'age': '21'}, {'age': 20}], insert_var=False)
# m.delete({'name': 'al'}, del_val=False)
# m.update({'age': 19}, {'age': 32}, update_var=False)
# m.find(find_var=False)








