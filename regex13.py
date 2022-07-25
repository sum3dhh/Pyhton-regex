 


import re
s = " my name is the  mm rock kkakak"
res = re.search(r"\D{3} k",s)
print(res.group())