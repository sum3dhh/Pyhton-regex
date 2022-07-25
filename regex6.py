import re

f = re.compile('a*b')#a*b or ab*
print(f.findall("aaaabaaaabababbbabababbababbbbbababbbbbabbabababa"))