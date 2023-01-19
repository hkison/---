# 비트코인으로 돈을 벌자!

# 코인 종류는 5개
# 각각 코인 등락 확률은 옆에 기재!
# 확률 속에 확률을 넣어야함
# 시작금액 100만원
# 1억 달성시 승리
# 잔금이 0원이거나 그 이하일시 대출 1회 가능(라이프 개념)
# 그 이후 다시한번 총 자산이 0원 이하면 패배
import time
import os
import random

C = 5000
CPer = 0
Py = 5000
PyPer = 0
J = 4000
JPer = 0
Cp = 4000
CpPer = 0
Cs = 1000
CsPer = 0
SeedMoney = 1_000_000

while True:
    # time.sleep(0.1)
    os.system("cls")
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃ 오늘의 비트코인 시세","%14s" % " ","┃")
    print("┃","%35s" % " ","┃")
    print("┃ C코인","%20s %7s" % (C,CPer),"%┃")
    print("┃ 파이썬코인","%15s %7s" % (Py,PyPer),"%┃")
    print("┃ 자바코인","%17s %7s" % (J,JPer),"%┃")
    print("┃ C++코인","%18s %7s" % (Cp,CpPer),"%┃")
    print("┃ C#코인","%19s %7s" % (Cs,CsPer),"%┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

    CPer =  random.randint(-90,90)
    PyPer =  random.randint(-50,50)
    JPer =  random.randint(-90,90)
    CpPer =  random.randint(-50,50)
    CsPer = random.randint(-20,20)

    C += int(C*CPer/100)
    Py += int(Py*PyPer/100)
    J += int(J*JPer/100)
    Cp += int(Cp*CPer/100)
    Cs += int(Cs*CsPer/100)

    time.sleep(5)
    os.system("cls")

