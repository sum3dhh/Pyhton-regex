import imp
from re import split

print(split('\W+',"ramen ramen ,, ramen *ramama*maamam"))
print(split('\W+','On 12th++Jan 2016, at 11:02 AM'))
print(split('\d+','On 12th Jan 2016, at 11:02 AM'))
