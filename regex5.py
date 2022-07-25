import re
c = re.compile('\w')#[ a-z , A-Z , 0-9]
print(c.findall("hello my name is *** 54 46 45 45 but i dont know 4 ur `` name"))

l = re.compile('\w+')# group of alphanumeric characters
print(l.findall("hello 54my **** name is just so  345 346 536 embarrasing im sorry lol"))

f = re.compile('\W')#non alphanumeric characters = speacial characters
print(f.findall("hahahhhaa ....342534 ,, ````` *** u are so funny"))