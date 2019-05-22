q = list(map(int, input().split()))
k = q[0]
p = 0
for i in range(0, len(q)):
    if q[i] >= k:
        k = q[i]
        p = i

print(k, p)
