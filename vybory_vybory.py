fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
word = dict()
i = 0
for w in fin:
    w = w.strip()
    word[w] = word.get(w, 0) + 1
    i += 1
q = sorted(word.items(), key=lambda item: (-item[1], item[0]))
if q[0][1] > i / 2:
    fout.write(q[0][0])
else:
    fout.write(q[0][0] + '\n')
    fout.write(q[1][0])
fin.close()
fout.close()
