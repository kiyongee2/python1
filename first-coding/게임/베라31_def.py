# 베스킨 라빈스 31 게임
from random import *

def 원하는정수값받기(질문):
    while True:
        try:
           입력값 = int(input(질문))
           if 입력값>=1 and 입력값 <=3:
               break
           else:
               print("1에서 3사이의 숫자만 입력하세요")
        except:
            print("잘못된 입력입니다. 숫자를 입력하세요")
    return 입력값


print("게임 시작!")

게임수 = 0

while True:
    # 참가자 1
    입력값 = 원하는정수값받기("[참가자1] 숫자 몇 개를 부를 건가요?(1~3): ")

    for 숫자 in range(입력값):
        print('{}!'.format(게임수 + 1 + 숫자))

    게임수 = 게임수 + 입력값

    if 게임수 >= 31:
        break

    # 컴퓨터
    입력값 = randint(1, 3)
    print(f"[컴퓨터] 숫자 몇 개를 부를 건가요?(1~3):{입력값}")

    for 숫자 in range(입력값):
        print('{}!'.format(게임수 + 1 + 숫자))

    게임수 = 게임수 + 입력값

    if 게임수 >= 31:
        break

print("벌칙 당첨!!")
