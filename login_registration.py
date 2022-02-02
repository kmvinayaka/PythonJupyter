# 1-Registration , 2 - login, 3 - update pswd , 4 - del user
# {"kmv":123}
import random
d = {}
while True:
    ch = int(input("Enter 1-Registration , 2 - login, 3 - update pswd , 4 - del user"))
    if ch ==1:
        username = input("Enter user name")
        if username in d.keys():
            print("Enter another username")
        else:
            pswd = input("Enter password")

            d[username] = pswd

    if ch == 2:
        username = input("Enter user name")
        if username in d.keys():
            print("welcome user")
            pswd = input("Enter password")
            if d[username] == pswd:
                print("success ur OTP is:",random.randint(999,10000))
            else:
                print("incorrect pswd")
            
        else:
            print("kindly register")

    if ch == 3:
        username = input("Enter user name")
        if username in d.keys():
            print("welcome user")
            pswd = input("Enter password")
            if d[username] == pswd:
                print("success")
                nwsp = input("Enter new password")
                d[username] = nwsp
            else:
                print("incorrect pswd")
            
        else:
            print("kindly register")
            
    if ch == 4:
        username = input("Enter user name")
        if username in d.keys():
            print("welcome user")
            pswd = input("Enter password")
            if d[username] == pswd:
                print("success")
                del d[username]
                print("deleted user")
            else:
                print("incorrect pswd")
            
        else:
            print("kindly register")

    print(d)
        
