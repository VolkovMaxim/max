q = list(map(int, input().split()))

p = 1000
for i in range(len(q)):
    if 0 < q[i] <= p:
        p = q[i]
print(p)
