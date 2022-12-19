# Pyhton program to extract Telephone numbers from a string

import re

str = """John: 5487621580,Mike: 6187962017, Jessi: 3157846027, Jessy: 2148930146"""
pattern = re.compile(r'\d{10}')
fa = pattern.findall(str)
print(fa)
