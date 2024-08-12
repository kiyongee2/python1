
name = ['흥부', '콩쥐', '놀부', '콩쥐']

same_name = set()
print(same_name)
n = len(name)
for i in range(0, n-1):
    for j in range(i+1, n):
        if name[i] == name[j]:
            same_name.add(name[i])

print(same_name)