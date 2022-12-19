#Python program to extract emails from a file

import re
with open('email.txt') as f:
    fr = f.read()
pattern = re.compile(r'\w*@\w*.\w{2,3}')
fa = pattern.findall(fr)
print('Emails contained in the file:')
print(fa)
