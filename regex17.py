from tokenize import Special


def passwordGenerator(passwd):
    Specialsym = ['@','#','$','&']
    val = True
    if len(passwd) < 6:
        print("The length of password should be greater than 6")
        val = False
    if len(passwd) > 20:
        print("The lenght of password should be smaller than 9")
        val = False
    if not any(char.isdigit() for char in passwd):
        print("Password must contain numbers")
        val = False
    if not any(char.isupper() for char in passwd):
        print("password must contail a uppercase character")
        val = False
    if not any(char.islower() for char in passwd):
        print("password must contain a lowercase character")
        val = False
    if not any(char in Specialsym for char in passwd):
        print("password must contain a speacial character:(@ # $ % & )")
        val =  False
    if val:
        return val

password = input("enter a password")
passwordGenerator(password)
if passwordGenerator(password):
    print("password is valid")
else:
    print("password is invalid")

