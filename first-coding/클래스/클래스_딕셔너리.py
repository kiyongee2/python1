# 딕셔너리도 클래스임
성적 = {'승준': 60, '은희': '결석', '태호': 60, '지영': 80}
print(type(성적))

# key 값만 뽑아내기
키값만 = 성적.keys()
print(키값만)

리스트로 = list(키값만)
print(리스트로)

튜플로 = tuple(키값만)
print(튜플로)

for 키값 in 성적.keys():
    print(키값)

# value 값만 뽑아내기
밸류만 = 성적.values()
print(밸류만)

리스트로 = list(밸류만)
print(리스트로)

튜플로 = tuple(밸류만)
print(튜플로)

for 밸류값 in 성적.values():
    print(밸류값)

# 키값 찾아서 삭제하기
성적.pop('태호')
print(성적)

# key-value 쌍 추가하기
성적['기용'] = 70
print(성적)