from random import *
from datetime import datetime
import time

userPass = input("Enter the password: ").lower()

random_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                  'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                  'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

datetime1 = time.time()

guss = ''
count = 0

while guss != userPass:
    guss = ''

    for letters in range(len(userPass)):
        guss_pass = random_letters[randint(0, 35)]
        guss = str(guss_pass)+str(guss)

    count += 1
    print(guss)

datetime2 = time.time()

print("your paswword was founded :\"" + guss + "\" in time : " + str(datetime2-datetime1))
print(f"Tried combination: {count}")

'''
.
.
.
sqi
vlz
qtm
fol
uqt
jsr
eel
wys
mau
prp
ckp
gmy
hpw
try
your paswword was founded :"try" in time : 2.561178207397461
Tried combination: 26220
'''
