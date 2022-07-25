import re
p = re.compile('[1-9]') #('[a-h]')

print(p.findall("Hello my Number is 123456789 and my friend's number is 987654321"))
