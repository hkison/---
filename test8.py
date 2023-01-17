# 반복문 탈출 break

# ----------------------------------------------------------------------------------------------------
for i in range(10):
    if i == 5:
        break
    print(i)
0 1 2 3 4

for i in range(10):
    print(i)
    if i == 5:
        break
# 0 1 2 3 4 5

# break는 반복문 안에서만 쓸수있음!

# ----------------------------------------------------------------------------------------------------
for i in [1,2,3]:
    for j in [4,5,6]:
        if j == 5:
            break
        print(i,j)
    print("!")

# break는 제일 가까운 loop 하나만 빠져나간다!

# ----------------------------------------------------------------------------------------------------
for i in range(10):
    if i > 5:
        break
else:
    print(i,"5보다 작음")

# for ~ else 구문
# 반복이 완전하게 돌았다 -> else 종속문장 실행됨
# 반복이 중간에 끊겼다 (break) -> else 종속문장 실행안됨

# ----------------------------------------------------------------------------------------------------
N = int(input())

for i in range(2,N):
    if N % i == 0:
        break
else:
    print(N, "은 0000000 입니다.")
# 0000000 -> 소수입니다

# i는 1을 제외한 N-1 까지의 숫자가 들어가므로 만약 break가 걸리지않는다면 N의 약수가 1과 N만 남기 때문에 N이 소수인걸 증명할 수 있다.

# ----------------------------------------------------------------------------------------------------
# continue
for i in range(10):
    if i < 5:
        continue
    print(i)
# 5 6 7 8 9
# continue는 조건이 성립할 시 다음으로 넘어가란 뜻 -> i가 5가 될 때부터 continue가 실행되지않으므로 5 6 7 8 9가 실행됨
# continue와 break는 프로그램의 속도에 영향을 미친다. -> 잘 사용하면 프로그램의 속도가 빨라짐(불필요한 코드를 실행하지 않기 때문)

# ----------------------------------------------------------------------------------------------------
# while
# for(반복 횟수 명확)
# while(반복 횟수 명확x)
# while Bool:
# Bool 값이 True일 동안 종속문장을 반복한다.
for i in range(1,11):
    print(i)
print("="*30)
i = 1
while i < 11:
    print(i)
    i += 1
print("="*30)
i = 0
while i < 10:
    i += 1
    print(i)
# 세 반복문 모두 같은 결과를 도출한다. 1 ~ 10 -> 종속문장의 실행순서를 잘 보도록 하자

# ----------------------------------------------------------------------------------------------------
# N 단 입력받고 구구단 출력하기!
N = int(input("N 단 입력: "))

i = 1
while i < 10:
    print (N,"x",i,"=",N*i)
    i += 1

# ----------------------------------------------------------------------------------------------------
# while True:
# stop 이라고 입력할 때까지 입력받기

while True:
    N = input("입력(종료 : stop): ")
#   ...
    if N == "stop":
        print("프로그램 종료")
        break

# ----------------------------------------------------------------------------------------------------
# 특정키(0)를 입력할 때까지 반복되도록 프로그램하세요.

while True:
    N = int(input("숫자 입력(0 은 종료) : "))
    if N == 0:
        print("프로그램 종료")
        break

# ----------------------------------------------------------------------------------------------------
# 특정키(0)를 입력할 때까지 수들의 합 구하는 프로그램
su = 0
while True:
    N = int(input("수 입력(0은 종료): "))
    su += N
    if N == 0:
        print(su)
        break
    
# ----------------------------------------------------------------------------------------------------
# 특정키(0)를 입력할 때까지의 수들의 평균을 구하는 프로그램
li = []
while True:
    N = int(input("수 입력(0은 종료) : "))
    li.append(N)
    if N == 0:
        print(sum(li)/(len(li)-1))
        break
-1 보다 li.append(N)의 위치를 바꿔주는게 더 좋은 코딩!

# ----------------------------------------------------------------------------------------------------
# 사용자가 quit 누르기 전까지 입력받고, 종료하면 평균출력
# 1) 숫자입력
#  - 리스트 담아주자
# 2) 문자입력
#  2-1) 종료시그널
#    - 평균 출력 종료
#  2-2) 아닐경우
#    - 숫자입력유도

li = []

while True:
    N = input("입력 (종료quit) : ")

    if N.isnumeric(): # 1
        li.append(int(N))
    else: # 2
        if N == "quit": # 2-1
            if li: #li가 비어있지 않다면
                print("평균 >", sum(li)/len(li))
                break
            else: #li가 비어있다면
                print("입력된 수 없음!")
        else: # 2-2
            print("수를 입력해주세요 !!")

# 요구명세서를 습관적으로 작성하자!

# ----------------------------------------------------------------------------------------------------
# Q. Python 점수를 입력받고 평균을 출력해주는 프로그램
# 1. 숫자 입력시
#   1-1. 0 에서 100 점 까지 입력 시
#   1-2. 유효한 점수 입력이 아닐 시
# 2. 숫자만 입력되지 않았을 시
#   2-1. 종료 시그널 입력 시 (q)
#      2-1-1. 입력된 점수가 존재할때
#      2-1-2. 존재하지않을때
#   2-2. 종료 시그널 입력이 아닐 시
# 1-1) 리스트에 담아준다
# 1-2) 유효한 범위를 알려준다
# 2-1-1) 평균 출력 후 종료 시켜준다
# 2-1-2) 입력된 점수가 없다고 말해주고 종료 시켜준다
# 2-2) 숫자를 입력하라고 안내해준다
liN=[]
while True:
    N = input("숫자 입력 :")
    if N.isnumeric():
        if 100 >= int(N) >= 0:
            liN.append(int(N))
        else:
            print("0에서 100 사이의 점수를 입력하세요!")
    else:
        if N =="quit":
            if liN:
                print("평균: ",sum(liN)/len(liN))    
            else:
                print("입력된 점수가 없습니다!")
            break
        else:
            print("숫자를 입력하세요!")

# ----------------------------------------------------------------------------------------------------
# 자판기 프로그램
import time
import os

mon = 0
while True:
    print("--- Menu ---")
    print("1. 콜라 / 300")
    print("2. 사이다 / 300")
    print("3. 커피 / 200")
    print("4. 현금 투입")
    print("5. 잔돈 반환")
    print("6. 종 료")
    print("------------")
    print("현재금액 :", mon)
    menu = input("메뉴 선택 : ")
    if menu == '1':                          #콜라를 골랐을때
            if mon >= 300:                          #잔돈이 콜라값 이상일때
                mon -= 300                          #콜라값 빼기
                print("콜라 선택")
                time.sleep(1)                
                print("콜라 맛있게 드세요!")
                time.sleep(2)
            else:                                   #잔돈이 콜라값 미만일때
                print("잔액이 부족합니다!")
                time.sleep(1)        
    elif menu == '2':                        #사이다를 골랐을때
            if mon >= 300:                          #잔돈이 사이다값 이상일떄
                mon -= 300                          #사이다값 빼기
                print("사이다 선택")
                time.sleep(1)
                print("사이다 맛있게 드세요!")
                time.sleep(2)                
            else:                                   #잔돈이 사이다값 미만일때
                print("잔액이 부족합니다!")
                time.sleep(1)
    elif menu == '3':                        #커피를 골랐을때
            if mon >= 200:                          #잔돈이 커피값 이상일때
                mon -= 200                          #커피값 빼기
                print("커피 선택")
                time.sleep(1)
                print("커피 맛있게 드세요!")
                time.sleep(2)
            else:                                   #잔돈이 커피값 미만일때
                print("잔액이 부족합니다!")
                time.sleep(1)
    elif menu == '4':                        #현금 투입
            pm = input("돈을 넣어주세요 : ")
            if pm.isnumeric():                      #현금 투입이 숫자일때
                if int(pm) > 0:                     #현금이 0보다 클때
                    mon += int(pm)                   
                else:                               #현금이 0이하 일때
                    print("돈은 1원이상 넣어주세요!")
                time.sleep(1)
            else:                                   #현금 투입이 숫자가 아닐때
                print("금액을 정확히 입력해 주세요!")
                time.sleep(1)
    elif menu == '5':                        #잔돈 반환
            print("잔돈이 반환됩니다.")
            time.sleep(2)
            mon = 0                                 #잔돈을 뺐으므로 0원
    elif menu == '6':                        #프로그램 종료
            print("프로그램을 종료합니다")
            time.sleep(1)
            break                                   #loop탈출
    else:                                           #메뉴가 1~6이 아닐때
        print("올바른 메뉴 선택이 아닙니다")
        time.sleep(1)
    os.system("cls")
    
# ----------------------------------------------------------------------------------------------------

