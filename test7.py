# for문 문제 풀기!

# 1 부터 10까지 홀,짝 판단하는 프로그램

# for i in range(1,11):
#     if i % 2 == 0:
#         print("짝")
#     else:
#         print("홀")

# ----------------------------------------------------------------------------------------------------
# 1 부터 n까지 홀수의 합, 짝수의 합

# n = int(input("n 입력 : "))
# even = 0
# odd = 0

# for i in range(1,n+1):
#     if i % 2 == 0:
#         even += i
#     else:
#         odd += i
# print(even,": 짝",odd,": 홀")

# 홀수, 짝수의 개수

    # even += 1
    # odd += 1

# 홀수 짝수를 각각 list에 담기
# even = []
# odd = []
# even.append(i)
# odd.append(i)

# 합 -> print(sum(even),sum(odd))
# 개수 -> print(len(even),len(odd))

# ----------------------------------------------------------------------------------------------------
# 1에서 N까지 3의배수의 합과 개수를 구하시오.

# 1) 변수로 구하기
# N = int(input("N 입력 : "))

# su = 0
# cnt = 0

# for i in range(1,N):
#     if i % 3 == 0:
#         su += i
#         cnt += 1
# print(su,"합",cnt,"개")

# 2) 리스트 사용해서 구하기

# N = int(input("N 입력 : "))

# liN = []

# for i in range(1,N):
#     if i % 3 == 0:
#         liN.append(i)
# print(sum(liN),"합",len(liN),"개")

# ----------------------------------------------------------------------------------------------------

# print의 위치에 따른 출력결과 차이

# li3= []
# for i in range(1,N+1):
# 	if i % 3 == 0:
# 		li3.append(i)


# print(li3) --- 1
# 	print(li3) --- 2
# 		print(li3) --- 3

# 1 2 3 위치에서 실행했을 때 결과를 예상해보세요.
# N = 9
# 1. [3,6,9]
# 2. [][][3][3][3][3,6]...
# 3. [3] [3,6] [3,6,9]

# ----------------------------------------------------------------------------------------------------
# A-B-C-D 가 번갈아 가면서 청소를 하기로 했다.
# 만약 첫날 A가 당번이라면 20일부터 50일까지 당번을 출력해라.

# A=[]
# B=[]
# C=[]
# D=[]
# for i in range(20,51):
#     if i % 4 == 1:
#         A.append(i)
#     elif i % 4 == 2:
#         B.append(i)
#     elif i % 4 == 3:
#         C.append(i)
#     else :
#         D.append(i)
# print("당번(일): \nA ->"A,"\nB ->",B,"\nC ->",C,"\nD ->",D)

# 더 간단한 답안
# li = ["D","A","B","C"]
# for i in range(20,51):
#     print(i, li[i%4])

# ----------------------------------------------------------------------------------------------------
# 지정한 날짜에 당번 확인하기

# for i in range(3,15,20,28,33,49,96,120,159):
#     print(i, li[i%4])

# ----------------------------------------------------------------------------------------------------
# 두 수를 입력받고 두 수 사이의 짝수를 출력하는 프로그램
# A = int(input("수 입력 : "))
# B = int(input("수 입력 : "))
# even = []
# if A<B:
#     for i in range(A+1,B):
#         if i % 2 == 0:
#             even.append(i)
#     print(even)
# elif A>B:
#     for i in range(B+1,A):
#         if i % 2 == 0:
#             even.append(i)
#     print(even)
# else:
#     print("두 수가 같음")

# ----------------------------------------------------------------------------------------------------
# 1에서 N까지 7의 배수의 합과 개수를 구하세요

# N = int(input("N 입력 : "))

# liN =[]

# for i in range(1,N+1):
#     if i % 7 == 0:
#         liN.append(i)
# print(sum(liN),"합",len(liN),"개")

# ----------------------------------------------------------------------------------------------------
# 1에서 N까지 3의 배수의 개수와 5의 배수의 개수의 차를 구하세요.

# N = int(input("N 입력 : "))

# liT=[]
# liF=[]

# for i in range(1,N+1):
#     if i%3==0:
#         liT.append(i)
#     if i%5==0: # 3과 5의 공배수를 지나치지 않기 위해 elif 대신 if 사용
#         liF.append(i)
# print(liT)
# print(liF)
# print(len(liT)-len(liF))

# ----------------------------------------------------------------------------------------------------
# 한 반 학생들의 혈액형입니다. A, B, AB, O 형이 각각 몇명인지 프로그래밍 하세요. 
# ['O', 'O', 'O', 'O', 'AB', 'B', 'A', 'A', 'O', 'AB', 'B', 'A', 'B', 'AB', 'AB', 'AB', 'O', 'A',
#  'A', 'AB', 'B', 'AB', 'O', 'B', 'A', 'O', 'A', 'O', 'AB', 'O', 'AB', 'AB', 'O', 'B', 'B', 'O', 'O', 'AB', 'B', 'A']

# li =['O', 'O', 'O', 'O', 'AB', 'B', 'A', 'A', 'O', 'AB', 'B', 'A', 'B', 'AB', 'AB', 'AB', 'O', 'A', 'A',
#     'AB', 'B', 'AB', 'O', 'B', 'A', 'O', 'A', 'O', 'AB', 'O', 'AB', 'AB', 'O', 'B', 'B', 'O', 'O', 'AB', 'B', 'A']

# cntO = 0
# cntA = 0
# cntB = 0
# cntAB = 0

# for i in li:
#     if i == 'O':
#         cntO += 1
#     elif i == 'A':
#         cntA += 1
#     elif i == 'B':
#         cntB += 1
#     else:
#         cntAB += 1
# print("A형: ",cntA,"명","B형: ",cntB,"명","O형: ",cntO,"명","AB형: ",cntAB,"명")

# ----------------------------------------------------------------------------------------------------
# 현재 당신은 5000 원이 있습니다. 편의점에 있는 물품들의 가격들이 다음과 같습니다. 구매가능한 물품의 개수를 구하세요.
# [6600, 4800, 3400, 3200, 4500, 5500, 3200, 7800, 4200, 5300, 7500, 4200, 7200, 5600, 6700, 8000, 7000, 6700, 6200,
# 6100, 4700, 7200, 7100, 5700, 5900, 4300, 5200, 5600, 5900, 6600, 4900, 5800, 7100, 5800, 4500, 3200, 7800, 5300, 7200, 8000]

# li = [6600, 4800, 3400, 3200, 4500, 5500, 3200, 7800, 4200, 5300, 7500, 4200, 7200, 5600, 6700, 8000, 7000, 6700, 6200, 6100, 4700, 7200,
#     7100, 5700, 5900, 4300, 5200, 5600, 5900, 6600, 4900, 5800, 7100, 5800, 4500, 3200, 7800, 5300, 7200, 8000]

# ava = []
# for i in li:
#     if i <= 5000:
#         ava.append(i)
# print(ava)
# print(len(ava))

# ----------------------------------------------------------------------------------------------------
# 한 반 학생들의 국어 점수이다. 80점 미만은 보충수업을 받아야한다고 했을 때, 보충수업 대상자는 몇명일까?
# [80, 70, 44, 66, 40, 80, 77, 57, 68, 90, 75, 84, 99, 52, 45, 53, 54, 96, 59, 47, 57,
# 68, 74, 68, 79, 60, 63, 67, 43, 100, 43, 54, 77, 59, 75, 60, 97, 47, 100, 54]

# li = [80, 70, 44, 66, 40, 80, 77, 57, 68, 90, 75, 84, 99, 52, 45, 53, 54, 96, 59,
#     47, 57, 68, 74, 68, 79, 60, 63, 67, 43, 100, 43, 54, 77, 59, 75, 60, 97, 47, 100, 54]

# sp =[]

# for i in li:
#     if i < 80:
#         sp.append(i)
# print(sp)
# print(len(sp))

# ----------------------------------------------------------------------------------------------------
# 구구단 출력 프로그램 (3단 : 3x1 =3, 3x2= 6, ...)

# dan = int(input("단 입력 : "))

# for i in range(1,10):
#     print(dan,"x",i,"=",(dan*i))

# ----------------------------------------------------------------------------------------------------
# 프로그램 작성하기
# ----------------------------------------------------------------
# 몇 회 연산을 진행하시겠습니까? 2

# 수 입력 : 10
# 수 입력 : 20
# =============
# 1. 더하기
# 2. 빼기
# 3. 곱하기
# =============
# 연산 입력 : 1
# 10 + 20 = 30

# 수 입력 : 10
# 수 입력 : 20
# =============
# 1. 더하기
# 2. 빼기
# 3. 곱하기
# =============
# 연산 입력 : 5
# 그런 연산 없습니다
# ----------------------------------------------------------------

# atm = int(input("몇 회 연산을 진행하시겠습니까?"))

# for i in range(1,atm+1):
#     a = int(input("수 입력 : "))
#     b = int(input("수 입력 : "))

#     print("="*10)
#     print("1. 더하기")
#     print("2. 빼기")
#     print("3. 곱하기")    
#     print("="*10)
#     op = int(input("연산 입력 : "))
#     if op == 1:
#         print(a,"+",b,"=",a+b)
#     elif op == 2:
#         print(a,"-",b,"=",a-b)
#     elif op == 3:
#         print(a,"*",b,"=",a*b)
#     else:
#         print("그런 연산 없습니다")

# ----------------------------------------------------------------------------------------------------
# 2000년부터 3000년 까지 윤년의 개수를 구하세요
# ※ 2000 년을 첫번째 윤년이라고 할 때, 135 번째 윤년은 몇 년일까요?
# yoon=[]
# for i in range(2000,3001):
#     if i % 4 == 0 and i % 100 != 0 or i % 400 == 0 and i % 100 != 0 :
#         yoon.append(i)
# print(yoon)
# print(len(yoon))
# print("135번째 윤년은 ", yoon[134],"년")

# ----------------------------------------------------------------------------------------------------
# 프로그램 작성하기
# 몇 회 입력 하시겠습니까? 3
# 수 입력 : 15
# 15 홀수
# 수 입력 : 24
# 24 짝수
# 수 입력 : 36
# 36 짝수

# atm = int(input("몇 회 입력 하시겠습니까? "))
# for i in range(1,atm+1):
#     a = int(input("수 입력(0제외) : "))
#     if a % 2 == 0:
#         print(a,"짝수")
#     else:
#         print(a,"홀수")

# ----------------------------------------------------------------------------------------------------
# 프로그램 작성하기
# 몇 회 입력 하시겠습니까? 4
# 수 입력 : 13
# 수 입력 : 24
# 수 입력 : 31
# 수 입력 : 22
# 13 홀수
# 24 짝수
# 31 홀수
# 22 짝수
# liA=[]
# atm = int(input("몇 회 입력 하시겠습니까? "))
# for i in range(1, atm+1):
#     a = int(input("수 입력 : "))
#     liA.append(a)
# for i in liA:
#     if i % 2 == 0:
#         print(i,"짝수")
#     else:
#         print(i,"홀수")

# ----------------------------------------------------------------------------------------------------
# 프로그램 작성하기
# 학생은 몇명인가요? 10
# 점수 입력 : 31
# 점수 입력 : 32
# 점수 입력 : 55
# 점수 입력 : 100
# 점수 입력 : 40
# 점수 입력 : 21
# ...
# 10 명의 평균 53.3
# 평균 이하인 학생 5명!
# liPt = []
# liAvg = []
# std = int(input("학생은 몇명인가요? "))
# for i in range(std):
#     pt = int(input("점수 입력 : "))
#     liPt.append(pt)
# avg = sum(liPt)/len(liPt)
# print(std,"명의 평균 : ",avg)
# for i in liPt:
#     if i <= avg:
#         liAvg.append(i)
# print("평균 이하인 학생",len(liAvg),"명!")

# ----------------------------------------------------------------------------------------------------
# 이어적기
# 1에서 N까지 이어적었을 때의 그 결과와 길이를 출력해주는 코드
# ex) 수 입력: 10
# 12345678910 -> 길이는 11
# ex) 수 입력: 20
# 1234567891011121314151617181920 -> 31

N = int(input("수 입력 : "))
strN = ""
for i in range(1,N+1):
    strN += str(i)
print(strN,"길이는",len(strN))
# print(str(liN),"길이는",len(str(liN)) - 2 - (N-1)*2)

# ----------------------------------------------------------------------------------------------------

