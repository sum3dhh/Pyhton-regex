

import re
string = "The tale of naruto uzumaki...."
s = re.search(r'naruto', string)
print("start index :", s.start())
print("end index :", s.end())
