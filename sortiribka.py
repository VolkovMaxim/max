def countSort(a):
    gr = [0] * 101
    for i in a:
        gr[i] += 1
        a = []
    for i in range(101):
        a += [i] * gr[i]
    return a
a = list(map(int, input().split()))
print(*countSort(a))
