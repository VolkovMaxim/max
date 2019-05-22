import math
print(*map(lambda x: int(math.fabs(x[0] - x[1])), zip(map(int, input().split()), map(int, input().split()))))
