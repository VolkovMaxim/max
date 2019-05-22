S, N = map(int, input().split())
c = sorted([int(input()) for i in range(N)])
d = sum(c)
while d > S and N:
    d -= c.pop()
    N -= 1
print(N)
