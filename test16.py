# 모든 사이트는 모든 웹페이지에서 정형화 되어있다.

import requests
from bs4 import BeautifulSoup

# res = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4")

# soup = BeautifulSoup(res.text,"html.parser")

# .title_box > strong.name
# 리스트 반환 -> for 결합
# 불값 반환 -> if 결합

# for i in soup.select(".title_box > strong.name")[:10]:
#     print(i.text)

# top 10 영화 제목


# ----------------------------------------------------------------------------------------------------
# 뉴스 기사 150개 가져오기
# 1 페이지당 30개씩 노출된다

# for i in range(1,6):
#     res2 = requests.get(f"https://news.ycombinator.com/news?p={i}")
#     soup2 = BeautifulSoup(res2.text,"html.parser")
#     for j in soup2.select("span.titleline"):
#         print(j.text)

# ----------------------------------------------------------------------------------------------------
# st = """<html>
#     <body>
#         <div id="hello1" one="kgit">안녕1</div>
#         <div class="hello2" two="bank">안녕2</div>
#         <div>
#             <span three="happy">안녕3</span>
#         </div>
#         <a href="https://www.naver.com" four="newyear">NAVER</a>
#     </body>
# </html>"""

# soup3 = BeautifulSoup(st, "html.parser")
# print(soup3.select_one("#hello1").get("one"))
# print(soup3.select_one(".hello2").get("two"))
# print(soup3.select_one("span").get("three"))
# print(soup3.select_one("a").get("four")

# ----------------------------------------------------------------------------------------------------
# res = requests.get("https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20150113_257%2Fbito701_1421127635914hdlCQ_GIF%2F%25B5%25C5%25C1%25F6%25B0%25ED%25B1%25E2_%25B1%25E8%25C4%25A1%25C2%25EE%25B0%25B3_%25B9%25AC%25C0%25BA%25C1%25F6.gif&type=sc960_832_gif")

# print(res.content)

# f = open("김찌.gif","wb")
# f.write(res.content)

# ----------------------------------------------------------------------------------------------------
# 네이버 월요웹툰 썸네일 파일로 저장

import os
from tqdm import tqdm

# res = requests.get("https://comic.naver.com/webtoon/weekdayList?week=mon")
# soup = BeautifulSoup(res.text,"html.parser")


# os.mkdir("제주도") #제주도 폴더 생성

# print(os.path.isdir("제주도")) #제주도라는 폴더가 존재하면 True, 아니면 False

# def 거르기(st):
#     for i in "/\\\"<>|:*?":
#         st = st.replace(i,"")
#     return st

# def folderMake(n):
#     if not os.path.isdir(n):
#         os.mkdir(n)

# folderMake("월요웹툰")

# for i in tqdm(soup.select(".thumb > a > img")):
#     name = 거르기(i.get("title"))
#     path = i.get("src")

#     r = requests.get(path)
#     f = open(f"월요웹툰/{name}.png","wb")
#     f.write(r.content)

# ----------------------------------------------------------------------------------------------------
# 월요일부터 일요일까지 모든 웹툰 썸네일
# 코드 실행시 웹툰 폴더 아래 mon~sun 폴더 생성
# 각각의 폴더안에는 요일별 웹툰 썸네일 들어있으면 됨

# def 거르기(st):
#     for i in "/\\\"<>|:*?":
#         st = st.replace(i,"")
#     return st

def folderMake(n):
    if not os.path.isdir(n):
        os.mkdir(n)

# folderMake("웹툰")


# for m in ["mon","tue","wed","thu","fri","sat","sun"]:
#     folderMake(f"웹툰/{m}")
#     res = requests.get(f"https://comic.naver.com/webtoon/weekdayList?week={m}")
#     soup = BeautifulSoup(res.text,"html.parser")
#     for i in tqdm(soup.select(".thumb > a > img")):
#         name = 거르기(i.get("title"))
#         path = i.get("src")

#         r = requests.get(path)
#         f = open(f"웹툰/{m}/{name}.png","wb")
#         f.write(r.content)

# ----------------------------------------------------------------------------------------------------
# stst = """
# <html>
#     <body>
#         <div class="champ">
#             <span id="name">케넨</span>
#             <span id="hp">1000</span>
#             <span id="mp">0</span>
#         </div>
#         <div class="champ">
#             <span id="name">티모</span>
#             <span id="hp">800</span>
#             <span id="mp">100</span>
#         </div>
#         <div class="champ">
#             <span id="name">베이가</span>
#             <span id="hp">600</span>
#             <span id="mp">400</span>
#         </div>

#     </body>
# </html>"""

# soup = BeautifulSoup(stst,"html.parser")
# champs ={}

# for i in soup.select(".champ"):
#     name = i.select_one("#name").text
#     hp = i.select_one("#hp").text
#     mp = i.select_one("#mp").text
#     champs[name] = [hp,mp]

# print(champs)

# ----------------------------------------------------------------------------------------------------


# res = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=3&acq=%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4&qdt=0&ie=utf8&query=%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4")

# soup = BeautifulSoup(res.text,"html.parser")
# movie = {}

# for i in soup.select("div.title_box")[:15]:
#     name = i.select_one(".name").text
#     people = i.select_one(".sub_text").text
#     movie[name] = [people]

# print(movie)

# ----------------------------------------------------------------------------------------------------

# res =requests.get("https://music.bugs.co.kr/chart")
# soup = BeautifulSoup(res.text,"html.parser")
# song = {}

# for i in soup.select("tbody > tr")[0:100]:
#     title = i.select_one("p.title").text.strip()
#     # if i.select_one(".more"):
#         # print(i.select_one(".onclick"))
#     singer = i.select_one("p.artist").text.strip()

#     song[title] = [singer]

# print(song)