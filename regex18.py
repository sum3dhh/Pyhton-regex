import re
def  main():
    password = input("Enter a password : ")
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    pag = re.compile(reg)
    mat = re.search(pag,password)
    if mat:
        print("password is valid")
    else:
        print("password is invalid")

if __name__ == '__main__':
    main()