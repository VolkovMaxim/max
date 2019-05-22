
a = list(map(int, input().split()))
b = a.copy()
for i in range(len(a)):
    if i % 2 != 0:
        b[i] = a[i - 1]
    elif i != len(a) - 1:
        b[i] = a[i + 1]
print(*b)
