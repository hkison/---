# crawling
# pip install requests

# import requests

# res = requests.get("https://www.naver.com")
# requests.get(url)
# url 로 request(요청)를 보냄, response(응답)를 반환함

# print(res.text) # html 소스

# 파싱!! 아무 의미없는 문자열을 규격에 맞춰서 해석함!!

# from bs4 import BeautifulSoup

# st= """
# <html>
#     <body>
#         <div id="hello1" class="kgit1">안녕1</div>
#         <div class="hello2">안녕2</div>
#         <div>
#             <span id="kgit2">안녕3</span>
#         </div>
#         <a id="itbank" href="https://www.naver.com">NAVER</a>
#     </body>
# </html>
# """

# soup = BeautifulSoup(st,"html.parser")
# print(soup.select("div"))
# print(soup.select('span'))
# print(soup.select("a"))
# print(soup.select('#hello1'))
# print(soup.select("#itbank"))
# print(soup.select(".hello2"))
# print(soup.select(".kgit1"))
# print(soup.select("html > body > div > span"))
# print(soup.select_one("#hello1").text)

# # 1. requests
# ========================================
# import requests
# res = requests.get(url)
# ========================================
# res 는 Response 클래스 인스턴스
# res.text (HTML 소스)

# 2. res.text in Python 아무의미 없더라...
# 파싱 : 웹의 규격에 맞춰서 해석
# ===========================================
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(문자열, "html.parser")
# ===========================================
# 아무의미없는 문자열을 웹의 형식으로 해석할 수 있는 soup 생성!

# 3. 셀렉터 = 태그를 지칭하는 방법 ( 원하는 정보 가져오려고 )
# - 태그는 그대로, id # , class . , 하위태그 > 

# ----------------------------------------------------------------------------------------------------
# 네이버 웹툰 참교육 111화 평점,참여자 수, 등록일 뽑기!

# res = requests.get('https://comic.naver.com/webtoon/detail?titleId=758037&no=111&weekday=mon')

# st = res.text

# print(st)

# soup = BeautifulSoup(st,"html.parser")
# print(soup.select_one("span#topPointTotalNumber").text) #평점
# print(soup.select_one("span.pointTotalPerson > em").text) #참여자수
# print(soup.select_one(".rt > .date").text) #등록일

# 작품이름, 작가이름, 작품소개, 장르, 연령 뽑아오기

# print(soup.select("h2 > .title")) #작품이름
# print(soup.select("h2 > .wrt_nm")) #작가이름
# print(soup.select(".detail > .txt")) #작품소개
# print(soup.select(".detail_info > .genre")) #장르
# print(soup.select(".detail_info > .age")) #연령

# 텍스트만 깔끔하게 잘라오기
# soup.select("~~"[0].text)
# soup.select_one("~~".text)

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# f = open("cham.csv","w")
# f.write("화,평점,참여자수,등록일\n")

# for i in tqdm(range(1,112)):

#     res = requests.get(f'https://comic.naver.com/webtoon/detail?titleId=758037&no={i}&weekday=mon') # i는 회차
#     soup = BeautifulSoup(res.text,"html.parser")
    
#     a = soup.select_one("span#topPointTotalNumber").text #평점
#     b = soup.select_one("span.pointTotalPerson > em").text #참여자수
#     c = soup.select_one(".rt > .date").text #등록일
#     f.write(f"{i}화,{a},{b},{c}\n")




for i in tqdm(range(1,163)):
    res = requests.get(f"https://lol.inven.co.kr/dataninfo/champion/detail.php?code={i}")
    soup = BeautifulSoup(res.text,"html.parser")

    name = soup.select_one(".korName").text
    rp = soup.select_one(".rp").text
    ip = soup.select_one(".ip").text
    f = open(f"lol/{name}.txt","w",encoding='utf-8')
    f.write(f"ip : {ip}ip, rp : {rp}rp")

