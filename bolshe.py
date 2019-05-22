q = list(map(int, input().split()))
k = q[0]
p = 0
for i in range(1, len(q)):
    if q[i] > q[i - 1]:
        print(q[i], end=' ')
