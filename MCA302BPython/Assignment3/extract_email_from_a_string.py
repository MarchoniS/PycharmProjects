# Python Program to extract all email address present in a string
import re
str = "Mile : example@gmail.com, intel has name@intel.com"
pattern = re.compile(r'\w*@\w*.\w{2,3}')
fa = pattern.findall(str)
print(fa)