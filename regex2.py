import re

c ="Hello my Number is 123456789 and my friend's number is 987654321"
regex = "\d+"

m = re.findall(regex,c)
print(m)