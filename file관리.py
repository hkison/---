import os

# os.listdir(x) -> x 폴더 아래의 파일/폴더명을 리스트로 반환
# x의 디폴트값은 현재경로

# ----------------------------------------------------------------------------------------------------
# 현재 경로의 파일, 폴더의 개수 각각 출력하기
# li = os.listdir()
# file = 0
# folder = 0

# for i in li:
#     if os.path.isdir(i):
#         folder += 1
#     else:
#         file += 1

# print(f"{folder}개의 폴더,{file}개의 파일")

# ----------------------------------------------------------------------------------------------------
# 구구단 파일들 열기
# for i in os.listdir("99단"):
#     f = open(f"99단/{i}", "r")
#     print(f.read())

# ----------------------------------------------------------------------------------------------------
# 웹툰 각 요일별 개수 세기
# li = os.listdir("웹툰")

# for i in li:
#     w_count = len(os.listdir(f"웹툰/{i}"))
#     print(f"{i} = ", end ="")
#     print(w_count)

# ----------------------------------------------------------------------------------------------------
# os.rename(A, B)
# A 기존에 존재하는 파일이름(경로포함)
# B 바뀔 파일이름

# ----------------------------------------------------------------------------------------------------
# 실습 안에있는 파일을 바꾸기
# 001_print.py > kgit(001)-[print].py
# 002_print.py > kgit(002)-[print].py

# print(os.listdir("실습"))
# for i in os.listdir("실습"):
#     num = i[:3]
#     name = i.split("_")[1].split(".py")[0]
#     change = f"kgit({num})-[{name}].py"
#     os.rename(f"실습/{i}",f"실습/{change}")

# ----------------------------------------------------------------------------------------------------
# poke 파일들 이름 바꾸기

# for i in os.listdir("poke"):
#     A = i.split(".")
#     ch = f"{A[0].zfill(3)}_{A[1][:-1]}.png"
#     os.rename(f"poke/{i}", f"poke/{ch}")

# ----------------------------------------------------------------------------------------------------
# 사진관리

from PIL import Image

# img = Image.open("poke/001_이상해씨.png") #이미지파일을 엶!

# print(img.size) #(256,256)
# img.resize((500,500)) #사이즈를 500,500으로 확대한 img 객체 반환

# img.save() #경로를 포함한 파일이름

# img.show() #현재 이미지 상태보기

# ----------------------------------------------------------------------------------------------------
# poke 폴더 아래있는 모든 사진을 500x500으로 확대해서 poke500 이라는 폴더 안으로 저장하기(파일이름은 그대로 유지!)

# if not os.path.isdir("poke500"):
#     os.mkdir(f"poke500")

# for i in os.listdir("poke"):
#     img = Image.open(f"poke/{i}")

#     img = img.resize((500,500))

#     img.save(f"poke500/{i}")

# ----------------------------------------------------------------------------------------------------


# img.mode -> RGBA A는 투명도 0(투명) ~ 255(선명)

# print(img.getpixel( (0,0) )) #0,0의 색상을 반환해줌

# img.putpixel( (0,0) , (255,0,0,255) ) #0,0에 빨간색 칠함
# img = Image.open("poke500/001_이상해씨.png")
# for i in range(500):
#     for j in range(500):
#         rgba = img.getpixel((i,j))
#         if rgba[3] > 100 :
#             img.putpixel((i,j),(0,0,0,255))
# img.show()

# ----------------------------------------------------------------------------------------------------
# pokedark 라는 폴더안에 poke500 에있는 친구들 전체를 뭘까요 상태로 저장하기

from tqdm import tqdm

if not os.path.isdir("pokedark"):
    os.mkdir("pokedark")

for i in tqdm(os.listdir("poke500")):
    img = Image.open(f"poke500/{i}")
    for j in range(500):
        for k in range(500):
            rgba = img.getpixel((j,k))
            if rgba[3] > 100 :
                img.putpixel((j,k),(0,0,0,255))
    img.save(f"pokedark/{i}")

# ----------------------------------------------------------------------------------------------------
