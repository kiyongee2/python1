
s = "20240801Rainy"
year = s[:4]
day = s[4:8]
weather = s[8:]
print(year)
print(day)
print(weather)

# 문자열 수정
w = 'pithon'
print(w[:1])
print(w[2:])
print(w[:1] + 'y' + w[2:])