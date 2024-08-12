# 베스킨 라빈스 31 게임
from random import *

print("게임 시작!")

게임수 = 0

while True:
    try:
        # 참가자 1
        입력값 = int(input("[참가자1] 숫자 몇 개를 부를 건가요?(1~3): "))

    except:
        print("잘못된 입력입니다. 숫자만 입력해주세요")

    else:
        if 입력값 >=1 and 입력값 <=3:
            for 숫자 in range(입력값):
                print('{}!'.format(게임수 + 1 + 숫자))

            게임수 = 게임수 + 입력값

            if 게임수 >= 31:
                break

            # 참가자 2
            # 입력값 = int(input("[참가자2] 숫자 몇 개를 부를 건가요?(1~3): "))

            # 컴퓨터
            입력값 = randint(1, 3)
            print(f"[컴퓨터] 숫자 몇 개를 부를 건가요?(1~3):{입력값}")

            for 숫자 in range(입력값):
                print('{}!'.format(게임수 + 1 + 숫자))

            게임수 = 게임수 + 입력값

            if 게임수 >= 31:
                break
        else:
            print("1에서 3사이의 숫자만 입력하세요")

print("벌칙 당첨!!")
