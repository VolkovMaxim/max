q = list((map(int, input().split())))
q1 = set()
for i in q:
    if i in q1:
        print('YES')
    else:
        print('NO')
    q1.add(i)
