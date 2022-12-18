#python preogram to print out words with their frequencies
txt = "This is a sample text to test this program a sample program this program"
print(txt)
print(txt.split())
words = txt.split()
wc = dict()
for w in words:
    if w in words:
        wc[w] = wc[w]+1
    else:
        wc[w] = 1
for w in wc:
    print(w," = ",wc[w])