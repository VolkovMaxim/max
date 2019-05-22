e = int(input())
a = list(map(int, input().split()))
q = int(input())
w = 2000
for i in a:
    if 0 <= i - q <= w:
        w = i - q
        e = i
    elif 0 <= q - i <= w:
        w = q - i
        e = i

print(e)
