from my_functions import input_validation_integer,input_validation_index,input_validation_string
def encode(y):
    print("____________________________________________________________________________________")
    replacement_set=""
    if y==1:
        replacement_set=EA
    elif y==2:
        replacement_set=AT
    else:
        replacement_set=input("Enter Custom Set ")
    p=len(replacement_set)
    message=input_validation_string(replacement_set+" ","Enter message ")
    key=input_validation_integer("Enter key/shift ")
    message_length=len(message)
    key=key%p
    new_message=""
    for i in range(0,message_length):
        if " " in replacement_set:
            j=replacement_set.find(message[i])
            new_message=new_message+replacement_set[(j+key)%p]
        else :
            if message[i]==" ":
                new_message=new_message+" "
                continue
            j=replacement_set.find(message[i])
            new_message=new_message+replacement_set[(j+key)%p]
    print("Encrypted Text is",new_message)
def decode(y):
    print("____________________________________________________________________________________")
    replacement_set=""
    if y==1:
        replacement_set=EA
    elif y==2:
        replacement_set=AT
    else:
        replacement_set=input("Enter Custom Set ")
    p=len(replacement_set)
    message=input_validation_string(replacement_set+" ","Enter Cipher text ")
    key=input_validation_integer("Enter key/shift ")
    message_length=len(message)
    key=p-key%p
    new_message=""
    for i in range(0,message_length):
        if " " in replacement_set:
            j=replacement_set.find(message[i])
            new_message=new_message+replacement_set[(j+key)%p]
        else :
            if message[i]==" ":
                new_message=new_message+" "
                continue
            j=replacement_set.find(message[i])
            new_message=new_message+replacement_set[(j+key)%p]
    print("Decrypted Text is",new_message)
def info():
    print('''_____________________________________________________________________________________________________________
    Caesar Cipher Information

    Definition:
    The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

    Key Concept:
    Key/Shift: The number of positions each letter is shifted. It's a secret parameter known only to the sender and the recipient.

    Encryption Process:
    1. Each letter in the plaintext is replaced by a letter some fixed number of positions down or up the alphabet.
    2. Non-alphabetic characters (such as spaces or punctuation) remain unchanged.

    Mathematical Representation:
    - The encryption function E(x) for a letter x is defined as E(x) = (x + shift) % 26.
    - Decryption is performed using D(x) = (x - shift) % 26.

    Example:
    - With a shift of 3, 'A' becomes 'D', 'B' becomes 'E', and so on.

    Weakness:
    - Vulnerable to brute-force attacks due to a limited number of possible keys.

    Usage:
    - Historically used by Julius Caesar for military communication.''')
print("---------------------------C3453R CIPH3R--------------------------- \n 1 Encode \n 2 Decode \n 3 info")
EA="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
AT=r'''!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'''
x=input_validation_index([1,2,3])
if x==1:
    print("_____________________________________________________________\n 1 Use English Alphabets[A-Z] \n 2 Use Ascii Table[33-126] \n 3 Use Custom One")
    y=int(input('ENTER INDEX '))
    encode(y)
elif x==2:
    print("_____________________________________________________________\n 1 Use English Alphabets[A-Z] \n 2 Use Ascii Table[33-126] \n 3 Use Custom One")
    y=int(input('ENTER INDEX '))
    decode(y)
elif x==3:
    info()
next_0=input("\nPress Enter to proceed ")
print("_____________________________________________________________\n 1 Return to Ceaser Cipher \n 2 Return to Home ")
x=input_validation_index([1,2])
if x==1:
    exec(open("ciphers\\ceasercipher.py").read())
elif x==2:
    exec(open("main\\main.py").read())
