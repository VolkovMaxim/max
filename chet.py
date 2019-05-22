q = list(map(int, input().split()))
for i in range(0, len(q)):
    if q[i] % 2 == 0:
        print(q[i], end=' ')
