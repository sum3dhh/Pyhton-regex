import re

regex = "([a-zA-Z]+) (\d+)"
match = re.search(regex," i was born in june 24")

if match != None:
    print("Match at index %s %s" % (match.start(),match.end()))
    print("full match %s " % (match.group(0)))
    print("Month %s" % (match.group(1)))
    print("date : %s " % (match.group(2)))
else:
    print("YOU ARE EXTREMELY WRONG")