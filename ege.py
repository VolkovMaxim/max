fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
q = []
k = int(fin.readline())
sum = []
for line in fin:
    q.append(line.split())
for i in range(len(q)):
    if int(q[i][-1]) >= 40 and int(q[i][-2]) >= 40 and int(q[i][-3]) >= 40:
        sum.append(int(q[i][-1]) + int(q[i][-2]) + int(q[i][-3]))
sum.sort()

sum1 = sum[::-1]
res = sum1[0]
w = 0
if k < len(sum1):
    while w < k:
        if sum1[w] != sum1[w + 1]:
            res = sum1[w]
        w += 1
    if sum1.count(res) <= k:
        print(res)
    else:
        print(1)
elif k >= len(sum):
    print(0)
