import re
m = re.compile('\d')
print(m.findall("I went to him at 11 A.M. on 4th July 1886"))

n = re.compile('\d+')
print(n.findall("I went to him at 11 A.M. on 4th July 1886"))