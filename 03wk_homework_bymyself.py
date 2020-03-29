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
# print (soup.title.getText())
song = soup.find("a", {"class" : "title ellipsis"})
singer = soup.find("a", {"class" : "artist ellipsis"})
rank = soup.find("td", {"class" : "number"})
print (song.text)

tr_list = soup.select("table.list-wrap > tbody > tr.list")
rank = 1
print(rank.text,',', song.text, ',', singer.text,)

for tr in tr_list:
    song = soup.select_one("a", {"class": "title ellipsis"}).text
    singer = soup.select_one(("a", {"class": "artist ellipsis"}).text
    print (song, singer, rank)
    rank += 1




# print (rank.text.strip(), song.text.strip(), singer.text.strip(), )
# print (song, singer, rank.text)


rank = 1

for tr in tr_list:
    song = tr_list.select_one(".info > a.title")
    singer = tr_list.select_one(".info > a.artist")
    print(rank, song.text.strip(), singer.text)
    rank += 1

    # print(rank.text.strip(), song.text.strip(), singer.text.strip())


#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
singer = soup.select("table > tbody > tr > td >.aritst.ellipsis")
song = soup.select("table.list-wrap > tbody > tr.list > td.info >.title.ellipsis")
rank = soup.find("table.list-wrap > tbody > tr.list > td.number > td.number")
print(rank)
# ranks = soup.select(".list-wrap > tr.list")
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1)
rank = 1

# 태그속성에 접근
# .attrs
# attrs['src] : 이미지 소스 위치 등


#
#
# for rank in song:
#     # song_tag = song.select_one(".title.ellipsis")
#     # singer_tag = singer.select_one(".artist.ellipsis")
#     print(rank, song[0], song[1])
#     rank += 1