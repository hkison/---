# 롤
import requests
import os
from bs4 import BeautifulSoup
from tqdm import tqdm

# if not os.path.isdir("롤아이콘"):
#     os.mkdir("롤아이콘")

# res = requests.get("https://lol.inven.co.kr/dataninfo/champion/")
# soup = BeautifulSoup(res.text, "html.parser")


# for i in soup.select(".champImage > a"):
#     A = i.get("title").split("(")[0]
#     B = "https:" + i.select_one("img").get("src")
#     r = requests.get(B)
#     f = open(f"롤아이콘/{A}.png", "wb")
#     f.write(r.content)


# ----------------------------------------------------------------------------------------------------
# 포켓몬

if not os.path.isdir("poke"):
    os.mkdir("poke")

res = requests.get("https://pokemongo.inven.co.kr/dataninfo/pokemon/")
soup = BeautifulSoup(res.text, "html.parser")


for i in tqdm(soup.select("a.pokemonicon")):
    nameP = i.select_one("span.pokemonname").text
    iconP = "https:" + i.select_one("img").get("src").replace("pokemonicon","pokemonimage")
    r = requests.get(iconP)
    f = open(f"poke/{nameP}.png", "wb")
    f.write(r.content)
    
