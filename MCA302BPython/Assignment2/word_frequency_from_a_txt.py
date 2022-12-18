# Program for word frequencies and print in descending Order


file = open("text.txt", "rt")
data = file.read()
words = data.split()
# print(data)
word_count = {}
for w in words:
    if w in word_count:
        word_count[w] = word_count[w] + 1
    else:
        word_count[w] = 1
x = {k: v for k, v in sorted(word_count.items(), key=lambda item: item[1])}
print(x)
