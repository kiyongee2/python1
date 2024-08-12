# 클래스
class 참치선물세트:

    def __init__(self, 일반, 야채, 고추):
        self.일반 = 일반
        self.야채 = 야채
        self.고추 = 고추

    def 출력(self, 이름):
        print("**", 이름, "내용물 **")
        print("일반참치:", self.일반)
        print("야채참치:", self.야채)
        print("고추참치:", self.고추)

#참01호 = 참치선물세트(4, 2, 3)
#참01호.출력("참치선물세트 01호")