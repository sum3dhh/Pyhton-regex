import re

def findDateandMonth(string):
    regex = r"([a-zA-Z]+) (\d+)"
    match = re.match(regex,string)
    if match == None:
        print("invalid arguments")
        return
    print("full date %s" % (match.group()))
    print("month : %s" % (match.group(1)))
    print("date : %s" % (match.group(2)))

findDateandMonth("June 24")
print("")
findDateandMonth("January 26 joe mama")
