from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://nin187:mongolia@cluster0.bx9tr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
)
db = client.dbsparta

# 영화제목 '매트릭스'의 평점을 가져오기
movie = db.movies.find_one({"title": "매트릭스"}, {"_id": False})
print(f'A1. 매트릭스의 평점: {movie["point"]}\n')

# '매트릭스'의 평점과 같은 평점의 영화 제목들을 가져오기
movie = db.movies.find_one({"title": "매트릭스"}, {"_id": False})
print(f'A2. 평점이 {movie["point"]}인 영화들')
tmp_point = movie["point"]
movies = list(db.movies.find({"point": tmp_point}, {"_id": False}))
for tmp_movie in movies:
    print(tmp_movie["title"])
# print("\n")

# 매트릭스의 평점을 0으로 만들기
db.movies.update_one({"title": "매트릭스"}, {"$set": {"point": 0}})
movie = db.movies.find_one({"title": "매트릭스"}, {"_id": False})
print(f'\nA3. {movie["title"]}의 평점을 {movie["point"]}으로 변경했습니다.')
movie = db.movies.find_one({"title": "매트릭스"}, {"_id": False})
db.movies.update_one({"title": "매트릭스"}, {"$set": {"point": tmp_point}})
print(f'{movie["title"]}의 평점을 다시 {tmp_point}으로 변경했습니다.')