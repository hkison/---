# 비트코인으로 돈을 벌자!

# 코인 종류는 5개
# 각각 코인 등락 확률은 옆에 기재!
# 확률 속에 확률을 넣어야함
# 시작금액 100만원
# 1억 달성시 승리
# 잔금이 0원이거나 그 이하일시 대출 1회 가능(라이프 개념)
# 그 이후 다시한번 총 자산이 0원 이하면 패배
# 30초 안에 매수나 매도 하지않으면 자동으로 보류 -> 다음 라운드 이동(코인 등락)
# 수정목록 : seedC ... seedCs 까지 list하나에 묶어서 list의 인덱스에 따른 변화를 일으키면 코인보유현황이 바뀔수있음
#           seed로 바꿀것
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


seedMoney = 1000000
seedC = 0
seedPy = 0
seedJ = 0
seedCp = 0
seedCs = 0
seedlistC = [0]
seedlistPy = [0]
seedlistJ = [0]
seedlistCp = [0]
seedlistCs = [0]

aS = 0

buy = 1
sell = 2

upDownPer = 50

upDownCntC = 0
upDownCntPy = 0
upDownCntJ = 0
upDownCntCp = 0
upDownCntCs = 0

def coinBuyLogic(a,b,c): # a = seed b = coinValue c=seedlist
        global coinAmount
        global seedMoney
        print("현재 최대 가능 매수 : ", seedMoney // b)
        coinAmount = input("얼마나 매수하시겠습니까? : ")
        try :
            if int(coinAmount) > seedMoney // b :
                print("보유하신 금액이 부족합니다")
                time.sleep(2)
            elif (coinAmount).isnumeric():
                print(coinAmount,"개 매수 완료.")
                a += int(coinAmount)
                c.clear()
                c.append(a)
                seedMoney -= int(coinAmount) * b
                print("{:,}".format(int(coinAmount) * b * -1))
                print("현재 보유 금액 : ""{:,}".format(seedMoney))
                time.sleep(2)
            else:
                print("숫자를 입력해주세요.")
                time.sleep(1)
        except:
            print("에러 ! 유효하지 않은 메뉴나 값입니다")
            time.sleep(1.5)

def coinSellLogic(a,b,c): # a = seed b = coinValue c=seedlist
    global coinAmount
    global seedMoney
    print("현재 최대 가능 매도 : ", c)
    coinAmount = input("얼마나 매도하시겠습니까? : ")
    try :
        if sum(c) < int(coinAmount) :
            print("보유하신 코인이 부족합니다")
            time.sleep(2)
        elif (coinAmount).isnumeric():
            print(coinAmount,"개 매도 완료.")
            aS = sum(c)
            aS -= int(coinAmount)
            a = aS
            del c[0]
            c.append(a)
            seedMoney -= int(coinAmount) * b
            print("{:,}".format(int(coinAmount) * b ))
            print("현재 보유 금액 : ""{:,}".format(seedMoney))
            time.sleep(2)
        else:
            print("숫자를 입력해주세요.")
            time.sleep(1)
    except:
        print("에러 ! 유효하지 않은 메뉴나 값입니다")
        time.sleep(1.5)

while True:
    # time.sleep(0.1)
    os.system("cls")
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┓")
    print("┃ 오늘의 비트코인 시세","%26s" % " ","┃보유 코인 현황  ┃")
    print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━┫")
    print("┃ 코인종류          등락확률(%) 현재시세 등락률(%)┃""                ┃")
    print("┃","%47s" % " ","┃                ┃")
    print("┃ 1.C코인","%19s %10s %7s" % (upDownPer,C,CPer),"%┃","%14s" % (seedlistC), "┃")
    print("┃ 2.파이썬코인","%14s %10s %7s" % (upDownPer,Py,PyPer),"%┃","%14s" % (seedlistPy),"┃")
    print("┃ 3.자바코인","%16s %10s %7s" % (upDownPer,J,JPer),"%┃","%14s" % (seedlistJ),"┃")
    print("┃ 4.C++코인","%17s %10s %7s" % (upDownPer,Cp,CpPer),"%┃","%14s" % (seedlistCp),"┃")
    print("┃ 5.C#코인","%18s %10s %7s" % (upDownPer,Cs,CsPer),"%┃","%14s" % (seedlistCs),"┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━┛")

    print("매수 : 1번\t\t 현재금액 : ",end ="")
    print("{:,}".format(seedMoney))
    print("매도 : 2번")

    user = input("메뉴를 선택하세요 : ")
    if user == '1':
        coinKind = input("매수 종목 선택 : ")
        if coinKind == '1':
            coinBuyLogic(seedC,C,seedlistC)
        elif coinKind == '2':
            coinBuyLogic(seedPy,Py,seedlistPy)
        elif coinKind == '3':
            coinBuyLogic(seedJ,J,seedlistJ)
        elif coinKind == '4':
            coinBuyLogic(seedCp,Cp,seedlistCp)
        elif coinKind == '5':
            coinBuyLogic(seedCs,Cs,seedlistCs)
        else:
            print("번호를 입력하여 주십시오.")
            time.sleep(2)
    elif user == '2':
        if (seedlistCp and seedlistC and seedlistCs and seedlistJ and seedlistPy) == False:
            print("보유하신 코인이 없습니다")
            time.sleep(1.4)
        else:
            coinMenu = input("매도 종목 선택 : ")
            if coinMenu == '1':
                coinSellLogic(seedC,C,seedlistC)
            elif coinMenu == '2':
                coinSellLogic(seedPy,Py,seedlistPy)
            elif coinMenu == '3':
                coinSellLogic(seedJ,J,seedlistJ)
            elif coinMenu == '4':
                coinSellLogic(seedCp,Cp,seedlistCp)
            elif coinMenu == '5':
                coinSellLogic(seedCs,Cs,seedlistCs)
            else:
                print("번호를 입력하여 주십시오.")
                time.sleep(2)
    else:
        print("번호를 맞게 입력하여 주십시오.")
        time.sleep(2)

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

    
    