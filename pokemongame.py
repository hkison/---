from tkinter import *
from random import randint, shuffle
from PIL import ImageTk
from time import sleep
import os
from tkinter import messagebox

tk = Tk()
tk.title("뭘까요?")
tk.geometry("500x800+200+200")

pokelist = os.listdir("pokedark")



def 문제출제():
    global correct_idx, bogilist
    correct_idx = randint(0, len(pokelist)-1)

    img = ImageTk.PhotoImage(file=f"pokedark/{pokelist[correct_idx]}")
    la["image"] = img
    la.image = img

    # 오답 붙히기!
    bogilist = [correct_idx]
    while True:
        idx = randint(0, len(pokelist)-1)
        if not idx in bogilist:
            bogilist.append(idx)
        if len(bogilist) == 5:
            break
    shuffle(bogilist)

    for i in range(5):
        pokename = pokelist[bogilist[i]].split("_")[1].split(".")[0]
        buttons[i]["text"] = pokename

la = Label(tk)

score = 0
life = 5
la_life = Label(tk, text="♥ "*life + "♡ "*(5-life), fg="red", font=("맑은고딕",30,"bold"))

la_life.pack()
la.pack()

buttons = [None] * 5

def 채점(idx):
    global life, score
    if bogilist[idx] == correct_idx:
        po = os.listdir("poke500")
        img = ImageTk.PhotoImage(file=f"poke500/{po[correct_idx]}")
        la["image"] = img
        la.image = img
        tk.update()
        sleep(1)
        score += 100
        문제출제()
    else:
        life -= 1
        la_life["text"] = "♥ "*life + "♡ "*(5-life)
        if life == 0:
            messagebox.showinfo("GAMEOVER", f"YOUR SCORE > {score}")
            exit()





for i in range(5):
    buttons[i] = Button(tk, font=("맑은고딕",15,"bold"), background="gray", width=20, command=lambda x=i:채점(x))
    buttons[i].pack()

문제출제()


tk.mainloop()