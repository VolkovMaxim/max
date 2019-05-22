def modul(a):
    if a < 0:
        a = -a
    return a

n = int(input())
gorod = list(map(int, input().split()))
m = int(input())
ybegishe = list(map(int, input().split()))
g = []
y = []
for i in range(n):
    g.append((gorod[i], i))
for i in range(m):
    y.append((ybegishe[i], i))
g.sort()
y.sort()

j = 0
k = []
for i in range(len(g)):
    while j < len(y):
        if j == len(y) - 1:
            k.append([g[i][1], y[-1][1] + 1])
            break
        elif modul((g[i][0] - y[j][0])) < modul((g[i][0] - y[j + 1][0])):
            k.append([g[i][1], y[j][1] + 1])
            break
        j += 1
k.sort()
for i in k:
    print(i[1], end=' ')
