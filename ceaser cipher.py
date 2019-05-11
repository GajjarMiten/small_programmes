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

ans=str(input("Enter Yes to Begin:"))
ans=ans.capitalize()

while(ans in 'Yes'):

    n = str(input("enter E for encryption or enter D for decryption:"))
    n = n.upper()
    wrd = str(input("enter your line :"))
    shift = int(input("enter shift:"))


    if(n=='E'):
        print("Encrypted code is:")
        encrpt(wrd,shift)       #calling the function for encryption
        ans=str(input("\nWant to do again ?"))
        ans=ans.capitalize()
    elif(n=='D'):
        print("Decrypted code is:")
        dcrpt(wrd,shift)        #calling the function for decryption
        ans = str(input("\nWant to do again ?"))
        ans=ans.capitalize()
    else:
        print("enter E or D only")
