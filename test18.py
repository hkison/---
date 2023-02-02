# 사진 흑백처리하기
# 마음에 드는 사진 아무거나 requests 로 다운받고, 각 픽셀의 rgb 값을 모두 더한 뒤
# 3으로 나눈 몫을 가각의 픽셀(r,g,b)에 동등하게 넣어주면 흑백처리가 된다

import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By

# res = requests.get("https://gdb.voanews.com/09680000-0a00-0242-4999-08da6423abcb_cx0_cy18_cw0_w650_r1_s.jpg")

# f = open(f"우주망원경.png","wb")
# f.write(res.content)

# img = Image.open(f"우주망원경.png")
# print(img.mode,img.size) #RGB 650,366
# # img.resize((500,500))

# for i in range(img.size[0]):
#     for j in range(img.size[1]):
#         color = img.getpixel((i,j))
#         img.putpixel((i,j),(sum(color)//3,sum(color)//3,sum(color)//3))
# img.show()

# ----------------------------------------------------------------------------------------------------
# 셀레니움
# 1. 크롬드라이버.exe
# 2. pip install selenium
driver = webdriver.Chrome("chromedriver.exe")

# driver.get("https://www.naver.com")
# 네검 = driver.find_element(By.CSS_SELECTOR,"#query")
# 네검.send_keys("악동뮤지션")
# 검버 = driver.find_element(By.CSS_SELECTOR,"#search_btn")
# 검버.click()
# 이버 = driver.find_element(By.CSS_SELECTOR,"#lnb > div.lnb_group > div > ul > li:nth-child(2) > a")
# 이버.click()
# 네홈 = driver.find_element(By.CSS_SELECTOR,"#header_wrap > div > div.gnb_wrap > div.header_group > div > h1 > a")
# 네홈.click()
# 광고 = driver.find_element(By.CSS_SELECTOR,"#ac_banner_a > img")
# print(광고.text)
# 태그를 지정한 후 할 수 있는 메서드/필드
# 1. sends_keys(x)  입력창에 값을 넣어줌!
# 2. click()        클릭(버튼)
# 3. text           텍스트 부분 검출
# 4. clear()        입력창 비우기!

# input()

# ----------------------------------------------------------------------------------------------------
# 선생님의 개인 미션깨기(셀레니움 응용)
# 1번페이지
# driver.get("https://hansh.pythonanywhere.com/sel/nium1/")
# 버튼 = driver.find_element(By.CSS_SELECTOR,"body > button")
# for i in range(1000):
#     버튼.click()
# input()
# 2번페이지
# driver.get("https://hansh.pythonanywhere.com/sel/jejudo")
# 버튼 = driver.find_element(By.CSS_SELECTOR,"#python1")
# 버튼2 = driver.find_element(By.CSS_SELECTOR,"#python2")
# for i in range(500):
#     버튼.click()
#     버튼2.click()
# input()
# 3번페이지
# driver.get("https://hansh.pythonanywhere.com/sel/cal")
# for i in range(99):
#     텍스트 = driver.find_element(By.CSS_SELECTOR,"#ques")
#     a = int(텍스트.text.split(" + ")[0].strip())
#     b = int(텍스트.text.split(" + ")[1].strip())
#     답 = a + b
#     정답입력 = driver.find_element(By.CSS_SELECTOR,"#val")
#     정답입력.send_keys(답)
#     제출 = driver.find_element(By.CSS_SELECTOR,"body > button")
#     제출.click()
#     정답입력.clear()

# input()