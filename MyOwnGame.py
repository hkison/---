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
                a += int(coinAmount) + sum(c)
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
            seedMoney += int(coinAmount) * b
            print("{:,}".format(int(coinAmount) * b ))
            print("현재 보유 금액 : ""{:,}".format(seedMoney))
            time.sleep(2)
        else:
            print("0보다 큰 숫자를 입력해주세요.")
            time.sleep(1)
    except:
        print("에러 ! 유효하지 않은 메뉴나 값입니다")
        time.sleep(1.5)


def coinR(coin,coinPer,b=-20,c=20):   
    global upDownPer
    if coinPer < 0:
        coinPer = random.randint(b/2,c)
        upDownPer = 66.6
    elif coinPer > 0:
        coinPer = random.randint(b,c/2)
        upDownPer = 33.3
    else:
        coinPer = random.randint(b,c)
        upDownPer = 50
    coin += int(coin*coinPer/100)

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
    print("게임 설명 : 3번")

    user = input("메뉴를 선택하세요 : ")
    if user == '1':
        coinKind = input("매수 종목 선택 : ")
        if coinKind == '1':
            coinBuyLogic(seedC,C,seedlistC)
            coinR(C,CPer)
        elif coinKind == '2':
            coinBuyLogic(seedPy,Py,seedlistPy)
            coinR(Py,PyPer)
        elif coinKind == '3':
            coinBuyLogic(seedJ,J,seedlistJ)
            coinR(J,JPer)
        elif coinKind == '4':
            coinBuyLogic(seedCp,Cp,seedlistCp)
            coinR(Cp,CpPer)
        elif coinKind == '5':
            coinBuyLogic(seedCs,Cs,seedlistCs)
            coinR(Cs,CsPer)
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
                coinR(C,CPer)
            elif coinMenu == '2':
                coinSellLogic(seedPy,Py,seedlistPy)
                coinR(Py,PyPer)
            elif coinMenu == '3':
                coinSellLogic(seedJ,J,seedlistJ)
                coinR(J,JPer)
            elif coinMenu == '4':
                coinSellLogic(seedCp,Cp,seedlistCp)
                coinR(Cp,CpPer)
            elif coinMenu == '5':
                coinSellLogic(seedCs,Cs,seedlistCs)
                coinR(Cs,CsPer)
            else:
                print("번호를 입력하여 주십시오.")
                time.sleep(2)
    elif user == '3':
        print("1.순수 보유금액 1억 달성시 [게임 승리] 입니다")
        print("2.시작 금액은 100만원으로 시작합니다.")
        print("3.코인의 등락확률은 높을수록 상승할 확률이 높고\n낮을수록 하락할 확률이 높습니다")
        print("4.승리 목표에 보유중인 코인의 가치는 합산되지 않습니다.")
        print("5.해당 코인이 이전에 상승했다면 그다음에 코인이 상승할 확률은 낮아집니다.")
        print("6.해당 코인이 이전에 하락했다면 그다음에 코인이 하락할 확률은 낮아집니다.")
        print("7.기타 오류 및 에러 발생 시 모든 데이터가 초기화되므로 양해바랍니다.")
        print("Tip : 매수나 매도를 0개로 설정하더라도 코인의 등락이 이루어집니다! 잘 이용해 보세요!")
        print("8.1억까지 화이팅![게임으로 돌아가려면 아무 키나 누르십시오]")
        input()

    else:
        print("번호를 맞게 입력하여 주십시오.")
        time.sleep(2)

    
    