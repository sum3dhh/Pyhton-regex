import re
def valid_email(email):
      regex_email=re.compile(r"""
                           ^([a-z0-9_\.-]+)                 # local Part
                           @                             # single @ sign
                            ([0-9a-z\.-]+)                 # Domain name
                           \.                             # single Dot .
                            ([a-z]{2,6})$                 # Top level Domain     
                           """,re.VERBOSE | re.IGNORECASE)
      res = regex_email.fullmatch(email)
      
      if res:
          print("{} is Valid email" .format(email))

          print("string body : {}" .format(res.group(1)))
          print(" web name : {}" .format(res.group(2)))
          print("at this : {}".format(res.group(3)))
      else:
          print("Invalid email :{} " .format(email))
       
valid_email("sumedhsonawane@gmail.com")
valid_email("wfyvg.com@gmail")
valid_email(".comeyqwgfygmail@")