q = set((map(int, input().split())))
w = set((map(int, input().split())))

print(*sorted(list(q & w)))
