"""
vending_machine = ['게토레이', '레쓰비', '생수', '이프로']

while True:
    drink = input("마시고 싶은 음료? ")
    if drink in vending_machine:
        vending_machine.remove(drink)
        print(drink, "드릴께요")
    elif drink == 'q' or drink == 'Q':
        break
    else:
        print(f'{drink}는 지금 없네요..')
print("프로그램 종료")
"""

vending_machine = ['게토레이', '레쓰비', '생수', '이프로']

while True:
    who = int(input('사용자를 입력하세요:\n1.소비자\n2.주인\n'))
    if who == 1:
        drink = input("마시고 싶은 음료? ")
        if drink in vending_machine:
            vending_machine.remove(drink)
            print(drink, "드릴께요")
            print("남은 음료수: ", vending_machine)
        else:
            print(f'{drink}는 지금 없네요..')
    else:
        todo = int(input("할 일 선택(1.추가, 2.삭제): "))
        if todo == 1:
            print("남은 음료수: ", vending_machine)
            drink = input("추가할 음료수? ")
            vending_machine.append(drink)
            vending_machine.sort()
            print("추가 완료!")
            print("남은 음료수: ", vending_machine)
        else:
            print("남은 음료수: ", vending_machine)
            drink = input("삭제할 음료수? ")
            if drink in vending_machine:
                vending_machine.remove(drink)
                print("삭제 완료!!")
                print("남은 음료수: ", vending_machine)
            else:
                print("없음")

