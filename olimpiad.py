n = int(input())
m = [input().split() for i in range(n)]
for k in sorted(m, key=lambda x: int(x[1]), reverse=True):
    print(k[0])
