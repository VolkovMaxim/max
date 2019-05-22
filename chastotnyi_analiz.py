fin = open('input.txt')
word = dict()

for w in fin:
    q = list(w.split())
    for i in q:
        word[i] = word.get(i, 0) + 1

for i in sorted(word.items(), key=lambda item: (-item[1], item[0])):
    print(i[0])
