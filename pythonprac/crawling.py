import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://nin187:mongolia@cluster0.bx9tr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
)
db = client.dbsparta

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
data = requests.get(
    "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303",
    headers=headers,
)

soup = BeautifulSoup(data.text, "html.parser")
trs = soup.select("#old_content > table > tbody > tr")

db_list = list()
for tr in trs:
    a_tag = tr.select_one("td.title > div > a")
    if a_tag != None:
        rank = tr.select_one("td > img")["alt"]
        title = a_tag.text
        point = tr.select_one("td.point").text
        doc = {"rank": rank, "title": title, "point": point}
        db.movies.insert(doc)