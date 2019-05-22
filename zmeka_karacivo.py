from math import sqrt

n = int(input())


k = int((- 1 + sqrt(1 + n)) // 2)
q = n-4*(k * (k + 1))
if q == 0:
    y1 = k
    x1 = k
elif q - 1 == 0:
    y1 = k + 1
    x1 = k
elif q - 1 <= 2 * (k + 1) - 1:
    y1 = k + 1
    x1 = k
    for i in range(q - 1):
        x1 = x1 - 1
elif q <= 4 * (k + 1):
    y1 = k + 1
    x1 = - (k + 1)
    for i in range(q - (2 * (k + 1))):
        y1 = y1 - 1
elif q <= 6 * (k + 1):
    y1 = - (k + 1)
    x1 = - (k + 1)
    for i in range(q - (4 * (k + 1))):
        x1 = x1 + 1
else:
    y1 = - (k + 1)
    x1 = (k + 1)
    for i in range(q - (6 * (k + 1))):
        y1 = y1 + 1
print(x1, y1)
