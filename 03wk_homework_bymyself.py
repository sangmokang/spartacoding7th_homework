import requests
from bs4 import BeautifulSoup



# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)


# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.

soup = BeautifulSoup(data.text, 'html.parser')
# print (soup.select("div.newest-list > div > table.list-wrap > tbody"))
print (soup.select(".newest-list > table.list-wrap")
song = soup.select(".newest-list > list-wrap > a.title ellipsis")
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
singer = soup.select(".newest-list > list-wrap > artist ellipsis")
ranks = soup.select(".list-wrap > tr.list")
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1)
rank = 1

for rank in ranks:
    song_tag = song.select_one(".title.ellipsis")
    singer_tag = singer.select_one(".artist.ellipsis")
    print(rank, song_tag.text.strip(), singer_tag.text())
    rank += 1