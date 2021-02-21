from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://nin187:mongolia@cluster0.bx9tr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
)
db = client.dbsparta

# 저장 - 예시
doc = {"name": "bobby", "age": 21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({"name": "bobby"})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({"age": 21}, {"_id": False}))

# 바꾸기 - 예시
db.users.update_one({"name": "bobby"}, {"$set": {"age": 19}})

# 지우기 - 예시
db.users.delete_one({"name": "bobby"})

"""
기능 insert / find /update /delete

<insert 예제>
doc = {'name': 'jane', 'age': 21}
db.users.insert_one(doc)

<find 예제>
### db.xxxxx.find({'xxxxx': xxxxx}, {'_id': False})를 가장 많이 사용함
same_ages = list(db.users.find({'age': 21}, {'_id': False}))

or

same_ages = list(db.users.find({}, {'_id': False}))

for person in same_ages:
    print(person)

<find_one 예제>
user = db.users.find_one({'name':'bobby'}, {'_id': False})
print(user)

<update 예제>
### update_many는 위험하므로 거의 안씀

db.users.update_one({'name': 'bobby'}, {'$set': {'age': 19}})
bobby = db.users.find_one({'name': 'bobby'}, {'_id': False})
print(bobby)

<delete 예제>
### delete_many는 위험하므로 거의 안씀

db.users.delete_one({'name':'kihoon'})
"""