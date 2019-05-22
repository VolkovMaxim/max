q = list(map(int, input().split()))
k = 0
for i in range(0, len(q)):
    if q[i] > 0:
        k += 1
print(k)
