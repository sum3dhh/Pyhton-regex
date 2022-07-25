import re
s = " welcome to jumanji"
es = re.search(r'j',s)
print(es.start())
print(es.end())
print(es.span())
