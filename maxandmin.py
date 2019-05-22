
a = list(map(int, input().split()))
b = a.copy()
max = [a[0], 0]
min = [a[0], 0]
for i in range(len(a)):
    if a[i] < min[0]:
        min[0] = a[i]
        min[1] = i
    if a[i] > max[0]:
        max[0] = a[i]
        max[1] = i
b[max[1]] = min[0]
b[min[1]] = max[0]
print(*b)
