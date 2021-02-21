import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.dbsparta

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
data = requests.get(
    "https://online.spartacodingclub.kr/rounds/5fffec205d351cf7a460bd61/dashboard",
    headers=headers,
)

soup = BeautifulSoup(data.text, "html.parser")
trs = soup.select(
    'div[property="CustomModal_Ranking_pg-bar-rank__3n7_T CustomModal_Ranking_low__3BOI3"]'
)
print(trs)

# db_list = list()
# for tr in trs:
#     a_tag = tr.select_one("td.title > div > a")
#     if a_tag != None:
#         rank = tr.select_one("td > img")["alt"]
#         title = a_tag.text
#         point = tr.select_one("td.point").text
#         doc = {"rank": rank, "title": title, "point": point}
#         db.movies.insert(doc)