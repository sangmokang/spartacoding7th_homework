import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)


# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.

soup = BeautifulSoup(data.text, 'html.parser')

# song = soup.find("a", {"class" : "title ellipsis"})
# singer = soup.find("a", {"class" : "artist ellipsis"})
# rank = soup.find("td", {"class" : "number"})
# print (song.text)

tr_tags = soup.select("table.list-wrap > tbody > tr.list")
rank = 1

for tr_tag in tr_tags:
    song = tr_tag.select_one(".info > a.title") #이 부분잉 잘 이해가 안되네.
    singer = tr_tag.select_one(".info > a.artist")
    print (rank, song.text.strip(), singer.text)
    rank += 1

#배워야 할 것
# select, find_all : Array
# find, select_one: 한가지 선택