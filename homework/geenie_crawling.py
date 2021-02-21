import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
data = requests.get(
    "https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1",
    headers=headers,
)

soup = BeautifulSoup(data.text, "html.parser")
trs = soup.select("#body-content > div.newest-list > div > table > tbody > tr")
for tr in trs:
    # rank = tr.select_one("td.number").text[0:2].strip() # 두자릿수 고정이라 99위까지밖에 적용 못함!!!
    rank = tr.select_one("td.number").text.split()[0]
    title = tr.select_one("td.info > a.albumtitle.ellipsis").text.strip()
    artist = tr.select_one("td.info > a.artist.ellipsis").text.strip()
    print(f'{rank}위: {title} - {artist}')