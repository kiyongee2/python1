# 리스트에서 내장 메서드 사용하기
할일 = ["기상", "식사", "책읽기", "식사"]

print("'책읽기'의 인덱스는 {}입니다.".format(할일.index('책읽기')))
print("할일 중 '식사'는 {}번 있습니다.".format(할일.count('식사')))

할일.append('운동')
print(할일)

할일.extend(['게임', '잠자기'])
print(할일)

할일.insert(2, '샤워')
print(할일)

할일.remove('게임')
print(할일)

할일.pop(1)
print(할일)

할일.reverse()
print(할일)

할일.sort()
print(할일)
