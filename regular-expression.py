import re

text_to_search = """
abcdefghijklmnopqurtuvwxyz
2 ABCDEFGHIJKLMNOPQRSTUVWXYZ
3 1234567890
4 
5 Ha HaHa
6 
7 MetaCharacters (Need to be escaped):
8 .[{()\^$|?*+
9 
10 coreyms.com
11 
12 321-555-4321
13 123.555.1234
14 
15 Mr. Schafer
16 Mr Smith
17 Ms Davis
18 Mrs. Robinson
19 Mr. T
"""
sentence = "Start a sentence and then brint it to and end"

pattern = re.compile(r"(Mr|Ms|Mrs)\.?\s[A-Z]\w*")

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
# subbed_urls = pattern.sub(r'\2\3', urls)
# print(subbed_urls)
