# replace
# 문장을 입력하세요 : hello jeju

# s = input("문장을 입력하세요 : ")

# li=[]

# while True:
#     n = input("가릴문자(입력완료 quit) : ")
#     if n == 'quit':
#         for i in li:
#             s = s.replace(i,"*")
#             print(s)
#         break
#     li.append(n)

# ----------------------------------------------------------------------------------------------------
# 파일이름으로 사용할 수 없는 문자열을 제거하는 코드
# \ " / ? : * < > |

# n = input("파일이름 : ")
# li = ["\",""","/","?",":","*","<",">","|"]

# for i in li:
#     if i in n:
#         n = n.replace(i,"")
# print(n)

# ----------------------------------------------------------------------------------------------------
# count
# 1에서 12345 까지 숫자를 셀때, 2가 등장한 횟수

# st =""
# for i in range(1,12346):
#     st += str(i)
# print(st.count('2'))

# ----------------------------------------------------------------------------------------------------
# 369 게임
# 숫자에 3,6,9 가 들어간 횟수만큼 박수를 쳐야한다. 이 때, X 번째 박수가 나온 수를 N 이라고 할 때, 패스워드를 구하여라
# 만약 X 가 3 이면 N 은 9 가 된다.
# X 가 4 라면 N 은 13 이 된다.
# 3 6 9 13 16 19 23 26 29 30 31 32 33
# X 가 1004 일 때 N 를 A 라고 한다.
# X 가 7979 일 때 N 을 B 라고 하고
# X 가 8282 일 때 N 를 C 라고 한다.
# A,B,C 를 구해주세요

# n = int(input("입력 : "))
# cntClap = 0
# cnt = 1
# while True:
#     for i in "369":
#         cntClap += str(cnt).count(i)
#     if cntClap >= n:
#         print(cnt)
#         break
#     cnt += 1

# ----------------------------------------------------------------------------------------------------
# n = int(input("입력 : "))

# st =""
# cntN = 1

# while True:
#     st += str(cntN)
#     if st.count(str(n)) >= n:
#         print(cntN)
#         break
#     cntN += 1

# ----------------------------------------------------------------------------------------------------
# 한번만 쓰인단어 추출
# ly = """my life is  been magic  seems fantastic
# i used to have a hole in the wall with a mattress
# funny when you want it  suddenly you have it
# you find out that your gold is  just plastic
# every day  every night
# i have  been thinking back on you and i
# every day  every night
# i worked my whole life
# just to get right  just to be like
# look at me  i am  never coming down
# i worked my whole life
# just to get high  just to realize
# everything i need is on the
# everything i need is on the ground
# on the ground
# everything i need is on the ground
# nah  but they do not  hear me though
# yeah  what goes up must come down
# nah  but they do not  hear me though
# you are  running out of time
# my world is  been hectic  seems electric
# but i have  been waking up with your voice in my head
# and i am  tryna send a message and let you know that
# every single minute i am  without you  i regret it
# every day  every night
# i have  been thinking back on you and i
# every day  every night
# i worked my whole life
# just to get right  just to be like
# look at me  i am  never coming down
# i worked my whole life
# just to get high  just to realize
# everything i need is on the
# everything i need is on the ground
# on the ground
# everything i need is on the ground
# nah  but they do not  hear me though
# yeah  what goes up must come down
# nah  but they do not  hear me though
# you are  running out of time
# i am  way up in the clouds
# and they say i have  made it now
# but i figured it out
# everything i need is on the ground  yeah  yeah
# just drove by your house  just drove by your house
# so far from you now  so far from you now
# but i figured it out
# everything i need is on the
# everything i need is on the ground
# on the ground
# everything i need is on the ground
# nah  but they do not  hear me though
# on the ground
# nah  but they do not  hear me though
# everything i need is on the ground
# """

# lys = ly.split()
# once =[]
# for i in lys:
#     if lys.count(i) < 2:
#         once.append(i)
# print(once)

# ----------------------------------------------------------------------------------------------------
# upper, lower, strip <- 반환하므로 변수의 값을 변화시키진 않는다!

# 문자열 입력 : i am A StudEnt
# 첫 글자만 대문자로 바꿔서 출력해주는 코드

# n = input("문자열 입력 : ")
# print(n[0].upper()+ n[1:].lower())

# ----------------------------------------------------------------------------------------------------
# print(chr(12610),chr(12623)) -> ㅂ ㅏ
# print(ord('ㅂ')) -> 12610
# print(ord('ㅏ')) -> 12623
# 다음 유니코드를 문자로 번역해서 메세지를 완성하세요
# st= '''
# 50668 47084 48516 32 54252 44592 54616 51648 32 47560 49464 50836 32 54624 32 49688 32 51080 50612 50836 126 126 32 112 121 116 104 111 110 32 50640 49436 32 47928 51228 32 51217 44540 54616 45716 32 49324 44256 47141 51012 32 44592 47476 49884 44256 32 45796 47480 32 44284 47785 50640 49436 32 51312 44552 51060 45208 47560 32 49688 50900 54616 44172 32 54617 49845 54616 49492 50556 32 54633 45768 45796 33 33 33 32 51109 45812 54616 45716 45936 32 47928 51228 45716 32 51228 32 49688 50629 32 46412 32 54396 44172 32 45908 32 50612 47140 50872 32 44144 50640 50836'''

# sts = st.split()
# for i in sts:
#     print(chr(int(i)), end ='')

# ----------------------------------------------------------------------------------------------------
# st ="여러분 포기하지마세요~~"

# for i in st:
#     print(ord(i), end = " ")

# ----------------------------------------------------------------------------------------------------
# Q. 구구단을 2단부터 9단까지 출력하세요.
# ===================================
# 3 이 등장하는 횟수 A
# 5 가 등장하는 횟수 B
# 7 가 등장하는 횟수 C
# 9 가 등장하는 횟수 D
# ===================================
# 문자열 formatting

# su = 0

# for i in range(2,10):
#     for j in range(1,10):
        # 1. 서식문자 표기법
        # print("%d x %d = %d" % (i,j,i*j)) 
        # 2. 문자열 함수 format
        # print("{} x {} = {}".format(i,j,i*j))
        # 3. f string
        # print(f"{i} x {j} = {i*j}")

# st ="""
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27
# 4 x 1 = 4
# 4 x 2 = 8
# 4 x 3 = 12
# 4 x 4 = 16
# 4 x 5 = 20
# 4 x 6 = 24
# 4 x 7 = 28
# 4 x 8 = 32
# 4 x 9 = 36
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 6 x 1 = 6
# 6 x 2 = 12
# 6 x 3 = 18
# 6 x 4 = 24
# 6 x 5 = 30
# 6 x 6 = 36
# 6 x 7 = 42
# 6 x 8 = 48
# 6 x 9 = 54
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 8 x 1 = 8
# 8 x 2 = 16
# 8 x 3 = 24
# 8 x 4 = 32
# 8 x 5 = 40
# 8 x 6 = 48
# 8 x 7 = 56
# 8 x 8 = 64
# 8 x 9 = 72
# 9 x 1 = 9
# 9 x 2 = 18
# 9 x 3 = 27
# 9 x 4 = 36
# 9 x 5 = 45
# 9 x 6 = 54
# 9 x 7 = 63
# 9 x 8 = 72
# 9 x 9 = 81"""

# for i in st:
#     if i in "9":
#         su += 1
# print(su)


# ----------------------------------------------------------------------------------------------------
# 카이사르 암호학을 이용해서 암호화한 문자이다. 키값을 찾아서 메세지를 해독해라!

# =====================================================================================
# 카이사르 암호학은 고대 암호학으로써 영어와 관련이 깊은 암호학입니다.
# 만약 key 값이 3 이라고 했을 때, A 는 D 로, B 는 E 로 , C 는 F 로 암호화 됩니다.
# 예를들어, Hello 라는 글자는 key 가 3 일 때 Khoor 가 되는 방식으로 암호화 하는 것입니다.
# 만약 Khoor 를 다시 Hello 로 되도리려면 거꾸로 3 칸을 가야겠죠? ㅎㅎ
# =====================================================================================
# Htwwjhy~ Z W xt Ljsnzx!! N lnaj Z uwjxjsy ktw ufxxnsl ymnx Vzjxy~ Gzy Dtz Mfaj Yt Xfd 'RTTDFMT' yt Rd Pfpft Yfqp Fhhtzsy. Mfmf~~

st = "72 116 119 119 106 104 121 126 32 90 32 87 32 120 116 32 76 106 115 110 122 120 33 33 32 78 32 108 110 97 106 32 90 32 117 119 106 120 106 115 121 32 107 116 119 32 117 102 120 120 110 115 108 32 121 109 110 120 32 86 122 106 120 121 126 32 71 122 121 32 68 116 122 32 77 102 97 106 32 89 116 32 88 102 100 32 39 82 84 84 68 70 77 84 39 32 121 116 32 82 100 32 80 102 112 102 116 32 89 102 113 112 32 70 104 104 116 122 115 121 46 32 77 102 109 102 126 126"

for j in range(-20,21):
    print()
    for i in st.split(" "):
        print(chr(int(i)+j), end="")

# CorrectyURsoGeniusIgi\eUpresentforpassingthisQuestyBut?ouHa\eToSa_"MOO?AHO"toM_KakaoTalkAccount)Hahayy


# ----------------------------------------------------------------------------------------------------

# st="""54620 45804 46041 50504 32 44256 49373 47566 51004 49512 49845 45768 45796 126 32 54056 49828 50892 46300 45716 32 52264 47049 32 48264 54840 54032 50640 32 51080 45716 32 49707 51088 47484 32 52264 47168 45824 47196 32 51077 47141 54616 49884 47732 32 46121 45768 45796 46 32 50937 32 48652 46972 50864 51200 32 50668 49884 44256 33 33 32 50668 44592 47196 32 46308 50612 44032 48372 49464 50836 32 104 116 116 112 115 58 47 47 119 119 119 46 99 111 117 112 97 110 103 46 99 111 109 47 118 112 47 112 114 111 100 117 99 116 115 47 53 49 50 51 50 54 56 49 48 49 63 105 116 101 109 73 100 61 55 48 48 53 48 48 57 53 48 51 38 118 101 110 100 111 114 73 116 101 109 73 100 61 55 52 50 57 55 50 55 51 57 52 50 38 115 114 99 61 49 48 52 50 53 48 51 38 115 112 101 99 61 55 48 51 48 52 55 55 55 38 97 100 100 116 97 103 61 52 48 48 38 99 116 97 103 61 53 49 50 51 50 54 56 49 48 49 38 108 112 116 97 103 61 73 55 48 48 53 48 48 57 53 48 51 86 55 52 50 57 55 50 55 51 57 52 50 65 51 52 51 53 50 51 54 53 51 38 105 116 105 109 101 61 50 48 50 50 49 50 51 48 49 52 53 56 52 56 38 112 97 103 101 84 121 112 101 61 80 82 79 68 85 67 84 38 112 97 103 101 86 97 108 117 101 61 53 49 50 51 50 54 56 49 48 49 38 119 80 99 105 100 61 49 54 55 49 48 55 56 53 54 55 55 52 57 49 48 48 53 52 57 53 51 49 49 38 119 82 101 102 61 38 119 84 105 109 101 61 50 48 50 50 49 50 51 48 49 52 53 56 52 56 38 114 101 100 105 114 101 99 116 61 108 97 110 100 105 110 103 38 65 100 78 111 100 101 73 100 61 51 52 51 53 50 51 54 53 51 38 103 99 108 105 100 61 69 65 73 97 73 81 111 98 67 104 77 73 95 99 51 99 113 116 83 103 95 65 73 86 66 115 69 87 66 82 51 56 104 119 67 101 69 65 81 89 65 105 65 66 69 103 73 89 66 102 68 95 66 119 69 38 99 97 109 112 97 105 103 110 105 100 61 49 57 48 55 51 50 49 53 51 53 57 38 97 100 103 114 111 117 112 105 100 61 49 52 55 53 51 52 52 48 55 52 48 49 38 105 115 65 100 100 101 100 67 97 114 116 61
# """

# for i in st.split():
#     print(chr(int(i)), end = "")
