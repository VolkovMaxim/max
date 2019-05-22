fin = open('input.txt')
word = dict()
for i in fin:
    q = list(i.split())
    for w in q:
        word[w] = word.get(w, 0) + 1

print(sorted(word.items(), key=lambda item: (-item[1], item[0]))[0][0])
