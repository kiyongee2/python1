# 파이썬에서는 알고 보면 모든 것이 클래스
아무거나 = 2022
print(아무거나)
print(type(아무거나))

아무거나 = ['첫코딩', '파이썬', 2024]
print(type(아무거나))

개수 = 20
print("사과{}개".format(개수))   # 점을 붙여 사용

문자열 = "사과가 좋아, 사과 좋아"
print(문자열.index('좋아'))
print(문자열.count('좋아'))

리스트 = ['사과', '사과', '바나나']
print(리스트.index('사과'))
print(리스트.count('사과'))

튜플 = ('서울', '부산', '부산')
print(튜플.index('부산'))
print(튜플.count('부산'))

리스트.append('포도')
print(리스트)

리스트.reverse()
print(리스트)

리스트.sort()
print(리스트)

print(ord('바'), ord('사'), ord('포'))  # 유니코드 값 출력 ord()

print(chr(97), chr(98), chr(99), chr(12593), chr(12594)) # 아스키 코드값 출력

print(hex(ord('A')), hex(ord('B')))  # 16진수로 표기