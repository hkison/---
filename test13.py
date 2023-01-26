# set : 중복없고, 순서없는 자료형

# set는 순서가 없다
# s = {1,2,3,4}
# print(type(s)) # <class 'set'>
# set 는 인덱스가 없다 not subscriptable

# set는 중복을 허용하지 않는다
# s = {1,1,1,1,1,1,2,2,2}
# print(s) # {1,2} 즉, 중복 허용 X

# set는 집합연산이 가능하다(용이하다) -> 교집합 &, 합집합 |, 차집합 -
# li1 = [1,2,3,4,5]
# li2 = [3,4,5,6,7]
# li3 = [3,5,6,7,9]

# print(set(li1) & set(li2)) # -> li1 과 li2의 교집합
# print(set(li1) | set(li3)) # -> li1 과 li3의 합집합
# print(set(li2) - set(li3)) # -> li2 과 li3의 차집합

# set 자료추가, 제거
# .add(x) ,remove(x)
# 비어있는 set는 s = set() 로만 만들 수 있다
# s ={} # -> <class 'dict'>

# ----------------------------------------------------------------------------------------------------

# st ="""
#  cause i i i m in the stars tonight
# so watch me bring the fire and set the night alight
# shoes on  get up in the morn
# cup of milk  let s rock and roll
# king kong  kick the drum  rolling on like a rolling stone
# sing song when i m walking home
# jump up to the top  lebron
# ding dong  call me on my phone
# ice tea and a game of ping pong  huh
# this is getting heavy
# can you hear the bass boom  i m ready  woo hoo
# life is sweet as honey
# yeah  this beat cha ching like money  huh
# disco overload  i m into that  i m good to go
# i m diamond  you know i glow up
# hey  so let s go
#  cause i i i m in the stars tonight
# so watch me bring the fire and set the night alight  hey
# shining through the city with a little funk and soul
# so i ma light it up like dynamite  whoa oh oh
# bring a friend  join the crowd
# whoever wanna come along
# word up  talk the talk
# just move like we off the wall
# day or night  the sky s alight
# so we dance to the break of dawn
# ladies and gentlemen  i got the medicine
# so you should keep ya eyes on the ball  huh
# this is getting heavy
# can you hear the bass boom  i m ready  woo hoo
# life is sweet as honey
# yeah  this beat cha ching like money
# disco overload  i m into that  i m good to go
# i m diamond  you know i glow up
# let s go
#  cause i i i m in the stars tonight
# so watch me bring the fire and set the night alight  hey
# shining through the city with a little funk and soul
# so i ma light it up like dynamite  whoa oh oh
# dy na na na  na na  na na na  na na na  life is dynamite
# dy na na na  na na  na na na  na na na  life is dynamite
# shining through the city with a little funk and soul
# so i ma light it up like dynamite  whoa oh oh
# dy na na na  na na  na na  ayy
# dy na na na  na na  na na  ayy
# dy na na na  na na  na na  ayy
# light it up like dynamite
# dy na na na  na na  na na  ayy
# dy na na na  na na  na na  ayy
# dy na na na  na na  na na  ayy
# light it up like dynamite
#  cause i i i m in the stars tonight
# so watch me bring the fire and set the night alight
# shining through the city with a little funk and soul
# so i ma light it up like dynamite  this is ah
#  cause i i i m in the stars tonight
# so watch me bring the fire and set the night alight  alight  oh
# shining through the city with a little funk and soul
# so i ma light it up like dynamite  whoa  light it up like dynamite
# dy na na na  na na  na na na  na na na  life is dynamite
# dy na na na  na na  na na na  na na na  life is dynamite
# shining through the city with a little funk and soul
# so i ma light it up like dynamite  whoa oh oh
# """

# words = st.split()

# for i in set(words):
#     print(f"{i}의 등장 횟수 {words.count(i)}")

# ----------------------------------------------------------------------------------------------------
# dict : 자료끼리 관계를 지어줌
# 단어 / 뜻     상품명 / 가격       아이템 / 확률       이름 / 개인정보들
# Key / Value

# d = {} # -> 빈 dict
# key value 사이에 :
# d ={ 1:"one", 2:"two", '3':"three"}
# li = ["A","B","C"]
# dict도 인덱싱이 당연히 안됨!
# 하지만 키 인덱싱은 가능!
# indexing : index를 가지고 자료에 접근
# key indexing : key를 가지고 value에 접근
# print(d[1]) # -> one
# print(li[0])
# li[0] = "one"
# print(li[0]) # -> one
# key indexing 을 통해서 value 변경 가능(기존에 dict에 key가 존재할 때)
# d[1] = "일"
# print(d[1]) # -> 일
# key indexing 을 통해서 value 추가 가능(기존에 dict에 key가 존재하지 않을때)
# d[100] = "백"
# print(d) # -> 키 인덱싱은 인덱싱보다 자유롭다

# in 멤버연산자 : 기본단위 in[iter]
# 기본단위가 존재 True, 존재하지 않으면 False

# del d[1] -> key 1이 사라짐 : 당연히 key 1의 value 도 사라짐

# dict - for 문
# d = {1:"one",2:"two",3:"three"}

# for i in d:
#     print(i, d[i])
# dict 선언 시에는 key, value 주석으로 정리하기! (헷갈릴 우려가 있음)

# ----------------------------------------------------------------------------------------------------
# words = st.split() # st는 dynamite 가사
# di = {}
# for i in set(words):
#     di[i]= words.count(i)

# print(di)

# ----------------------------------------------------------------------------------------------------
# 거북이 가지고 놀기
# import turtle as t # 파일이름이 turtle.py 동작안해요
# import random as r

# t.shape("turtle") # 거북이 모양으로 커서설정
# t.colormode(255) # 색상설정을 숫자로 하겠다
# t.color((r.randint(0,255),r.randint(0,255),r.randint(0,255)))
# t.pensize(7)
# t.speed(0)

# t.fd(200) # 머리방향기준 앞으로 200 전진
# t.lt(90) # 머리방향기준 왼쪽으로 90 도 회전
# t.fd(200) # 머리방향기준 앞으로 200 전진
# t.rt(225) # 머리방향기준 오른쪽으로 225 도 회전

# t.pu()
# t.goto(300, -200)
# t.pd()
# t.fd(100)

# t.pd() # 펜을 내려놓겠다
# t.pu() # 펜을 올리겠다

# 5 5 5 5
# t.shape("turtle")
# t.colormode(255)
# t.color(0,30,255)
# t.pensize(1)

# t.speed(0.3)
# x = 10
# while True:
#     t.fd(x)
#     t.lt(90)
#     t.fd(x)
#     t.lt(90)
#     t.fd(x)
#     t.lt(90)
#     t.fd(x)
#     t.pu()
#     x += 10
#     t.fd(x)
#     t.lt(90)
#     x += 10
#     t.pd()
# t.mainloop() # 창을 유지시켜줌 (맨아래 위치)
# st ="""
#  cause i i i m in the stars tonight
# so watch me bring the fire and set the night alight
# shoes on  get up in the morn
# cup of milk  let s rock and roll
# king kong  kick the drum  rolling on like a rolling stone
# sing song when i m walking home
# jump up to the top  lebron
# ding dong  call me on my phone
# ice tea and a game of ping pong  huh
# this is getting heavy
# can you hear the bass boom  i m ready  woo hoo
# life is sweet as honey
# yeah  this beat cha ching like money  huh
# disco overload  i m into that  i m good to go
# i m diamond  you know i glow up
# hey  so let s go
#  cause i i i m in the stars tonight
# so watch me bring the fire and set the night alight  hey
# shining through the city with a little funk and soul
# so i ma light it up like dynamite  whoa oh oh
# bring a friend  join the crowd
# whoever wanna come along
# word up  talk the talk
# just move like we off the wall
# day or night  the sky s alight
# so we dance to the break of dawn
# ladies and gentlemen  i got the medicine
# so you should keep ya eyes on the ball  huh
# this is getting heavy
# can you hear the bass boom  i m ready  woo hoo
# life is sweet as honey
# yeah  this beat cha ching like money
# disco overload  i m into that  i m good to go
# i m diamond  you know i glow up
# let s go
#  cause i i i m in the stars tonight
# so watch me bring the fire and set the night alight  hey
# shining through the city with a little funk and soul
# so i ma light it up like dynamite  whoa oh oh
# dy na na na  na na  na na na  na na na  life is dynamite
# dy na na na  na na  na na na  na na na  life is dynamite
# shining through the city with a little funk and soul
# so i ma light it up like dynamite  whoa oh oh
# dy na na na  na na  na na  ayy
# dy na na na  na na  na na  ayy
# dy na na na  na na  na na  ayy
# light it up like dynamite
# dy na na na  na na  na na  ayy
# dy na na na  na na  na na  ayy
# dy na na na  na na  na na  ayy
# light it up like dynamite
#  cause i i i m in the stars tonight
# so watch me bring the fire and set the night alight
# shining through the city with a little funk and soul
# so i ma light it up like dynamite  this is ah
#  cause i i i m in the stars tonight
# so watch me bring the fire and set the night alight  alight  oh
# shining through the city with a little funk and soul
# so i ma light it up like dynamite  whoa  light it up like dynamite
# dy na na na  na na  na na na  na na na  life is dynamite
# dy na na na  na na  na na na  na na na  life is dynamite
# shining through the city with a little funk and soul
# so i ma light it up like dynamite  whoa oh oh
# """
# words = st.split()
# di = {}
# # for i in set(words):
# t.setup(1600,900)
# t.ht() # 커서 숨김
# t.speed(0)
# t.pu()
# t.colormode(255)     

# for i in set(words):
#     di[i] = words.count(i)
# print(di)

# for i in di:
#     t.color(r.randint(0,255),r.randint(0,255),r.randint(0,255))
#     t.write(i,font=("맑음",di[i]+10,"bold"))
#     t.goto(r.randint(-700,400),r.randint(-300,300))


# for i in range(1,1001):
#     t.color(r.randint(0,255),r.randint(0,255),r.randint(0,255))    
#     t.write("hello world", font =("맑은고딕",30,"bold"))
#     t.goto(r.randint(-800,400),r.randint(-400,400))


# for i in set(words):
#     t.color(r.randint(0,255),r.randint(0,255),r.randint(0,255))
#     t.write(i,font=("궁서체",words.count(i)+10,"bold"))
#     t.goto(r.randint(-700,400),r.randint(-300,300))

# t.mainloop()

# ----------------------------------------------------------------------------------------------------
# 나만의 단어장 만들기 프로그램

di={}

while True:
    print("="*15)
    print("1.단어검색")
    print("2.단어추가")
    print("3.단어수정")
    print("4.단어삭제")
    print("5.종료")
    print("="*15)

    user = int(input("메뉴입력 > "))
    if user == 1:
        sch = input("검색할 단어를 입력해주세요 : ")
        if sch in di:
            print(sch,"의 뜻은",di[sch],"입니다")
        else:
            print("등록된 단어가 아닙니다")
    elif user == 2:
        word = input("추가할 단어를 입력해주세요 : ")
        print(word,end =" ")
        mean = input("의 뜻을 입력해주세요 : ")
        mean = di[word]
        print(di[word])



# ----------------------------------------------------------------------------------------------------