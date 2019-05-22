fin = open('input.txt')
word = dict()
for i in fin:
    q = list(i.split())
    for w in q:
        word[w] = word.get(w, 0) + 1
        print(word[w] - 1, end=' ')
