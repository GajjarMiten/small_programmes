''' this is for encryption of text in
            caeser cipher
'''

def encrpt(str,x):
    y = len(str)
    for i in range(0, y):
        if (ord(str[i]) != 32):
            print(chr(ord(str[i]) + x), end="")
        else:
            print(str[i], end="")

''' this is for decryption of text in
            caeser cipher
'''

def dcrpt(str,x):
    y=len(str)
    for i in range(0, y):
        if (ord(str[i]) != 32):
            print(chr(ord(str[i]) - x), end="")
        else:
            print(str[i], end="")


# the main code
n=int(input("enter 1 for encryption or enter 0 for decryption:"))
wrd=str(input("enter your line :"))
shift=int(input("enter shift:"))

if(n==1):
    encrpt(wrd,shift)       #calling the function for encryption
elif(n==0):
    dcrpt(wrd,shift)        #calling the function for decryption
else:
    print("enter 1 or 0 only")
