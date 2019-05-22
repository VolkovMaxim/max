import functools

print(functools.reduce(lambda x, y: x * (y ** 5), ((1, 1) + tuple(map(int, input().split())))))
