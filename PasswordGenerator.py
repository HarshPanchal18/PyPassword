import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"

lens = int(input("Enter the length of password: "))
pNum = int(input("Enter the number of password: "))

for i in range(0, pNum):
    password = ""
    for x in range(0, lens):
        passChar = random.choice(chars)
        password = password+passChar
    print("Password:"+password)

'''
Enter the length of password: 5
Enter the number of password: 5
Password:ynClY
Password:K1(y^
Password:bR8oe
Password:NHtq&
Password:v^TDx
'''
