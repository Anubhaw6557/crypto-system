import random
from my_functions import input_validation_integer,input_validation_index,input_validation_string
def info():
    print('''-----------------------------------------------------------------------------------------------------
    Monoalphabetic Substitution Cipher Information Page
          
    A monoalphabetic substitution cipher is a type of substitution cipher where each letter
    in the plaintext is consistently replaced with the same letter or symbol in the ciphertext.
    This type of cipher provides a simple form of encryption, but it is vulnerable to frequency analysis.

    Key Properties:
    - The key is a one-to-one mapping of letters in the alphabet.
    - Each letter in the plaintext corresponds to a unique letter in the ciphertext.
    - The key is used for both encryption and decryption.

    Security Considerations:
    - Monoalphabetic ciphers are vulnerable to frequency analysis.
    - The security of the cipher depends on the secrecy of the key.

    Example:
    For example, with the key 'ZYXWVUTSRQPONMLKJIHGFEDCBA', 'A' would be replaced by 'Z', 'B' by 'Y', and so on.
    Keep in mind that using a fixed key like this makes the cipher susceptible to known-plaintext attacks.''')
def encode(y):
    print("____________________________________________________________________________________")
    set=""
    replacement_set=""
    if y==1:
        set=EA
    elif y==2:
        set=AT
    else:
        with open("ciphers\\subscustomset.txt",'r') as file:
            lines = file.readlines()
            set=lines[0].strip("\n")
    len_set=len(set)
    with open("ciphers\\subsmap.txt",'r') as file:
        lines = file.readlines()
        replacement_set=lines[y-1].strip("\n")
    message=input_validation_string(set+" ","Enter Message ")
    new_message=""
    len_message=len(message)
    for i in range(0,len_message):
        if " " in set:
            index=set.find(message[i])
            new_message=new_message+replacement_set[index]
        else:
            if message[i]==" ":
                new_message=new_message+" "
                continue
            index=set.find(message[i])
            new_message=new_message+replacement_set[index]
    print("Encrypted Message",new_message)
def decode(y):
    print("____________________________________________________________________________________")
    set=""
    replacement_set=""
    if y==1:
        set=EA
    elif y==2:
        set=AT
    else:
        with open("ciphers\\subscustomset.txt",'r') as file:
            lines = file.readlines()
            set=lines[0].strip("\n")
    len_set=len(set)
    with open("ciphers\\subsmap.txt",'r') as file:
        lines = file.readlines()
        replacement_set=lines[y-1].strip("\n")
    message=input_validation_string(replacement_set+" ","Enter Ciphertext ")
    new_message=""
    len_message=len(message)
    replacement_set,set=set,replacement_set
    for i in range(0,len_message):
        if " " in replacement_set:
            index=set.find(message[i])
            new_message=new_message+replacement_set[index]
        else:
            if message[i]==" ":
                new_message=new_message+" "
                continue
            index=set.find(message[i])
            new_message=new_message+replacement_set[index]
    print("Decrypted Message",new_message)
def see_mapping():
    print("_____________________________________________________________\n 1 English Alphabets[A-Z] \n 2 Ascii Table[33-126] \n 3 Custom One")
    x=input_validation_index([1,2,3])
    print("___________________________________________________________________________\n")
    if x==1:
        set=EA
    elif x==2:
        set=AT
    elif x==3:
        with open("ciphers\\subscustomset.txt",'r') as file:
            lines = file.readlines()
            set=lines[0].strip("\n")
    with open("ciphers\\subsmap.txt",'r') as file:
        lines = file.readlines()
        replacement_set=lines[x-1].strip("\n")
    for i in range(0,len(set)):
        print(set[i],"-",replacement_set[i])
def change_mapping():
    print("_____________________________________________________________\n 1 English Alphabets[A-Z](Random Shuffle) \n 2 Ascii Table[33-126](Random Shuffle) \n 3 Custom One")
    x=input_validation_index([1,2,3])
    if x==1 or x==2:
        if x==1:
            set=EA
        elif x==2:
            set=AT
        lst_set=list(set)
        random.shuffle(lst_set)
        replacement_set=''.join(lst_set)
        with open("ciphers\\subsmap.txt",'r') as file:
            lines = file.readlines()
            lines[x-1]=replacement_set+"\n"
            lines_str=''.join(lines)
        with open("ciphers\\subsmap.txt",'w') as file:
            file.write(lines_str)
    else:
        set=""
        replacement_set=""
        print("_____________________________________________________\n Enter Mapping like (a-B,c-D,8-y)")
        mapping=input()
        mapping_lst=mapping.split(",")
        for b in range(0,len(mapping_lst)):
            mapping_lst_elem=mapping_lst[b]
            set_elem=((mapping_lst_elem.split("-"))[0]).strip()
            replacement_set_elem=((mapping_lst_elem.split("-"))[1]).strip()
            set=set+set_elem
            replacement_set=replacement_set+replacement_set_elem
        with open("ciphers\\subsmap.txt",'r') as file:
            lines = file.readlines()
            lines[x-1]=replacement_set+"\n"
            lines_str=''.join(lines)
        with open("ciphers\\subsmap.txt",'w') as file:
            file.write(lines_str)
        with open("ciphers\\subscustomset.txt",'w') as file:
            file.write(set)
print("---------------------------5U357ITU7I0N CIPH3R--------------------------- \n 1 Encode \n 2 Decode \n 3 See and Change Mapping \n 4 info")
EA="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
AT=r'''!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'''
x=input_validation_index([1,2,3,4])
if x==1:
    print("_____________________________________________________________\n 1 Use English Alphabets[A-Z] \n 2 Use Ascii Table[33-126] \n 3 Use Custom One")
    y=int(input('ENTER INDEX '))
    encode(y)
elif x==2:
    print("_____________________________________________________________\n 1 Use English Alphabets[A-Z] \n 2 Use Ascii Table[33-126] \n 3 Use Custom One")
    y=int(input('ENTER INDEX '))
    decode(y)
elif x==3:
    print("____________________________________________________________________\n 1 See Mapping \n 2 Change Mapping")
    x=input_validation_index([1,2])
    if x==1:
        see_mapping()
    elif x==2:
        change_mapping()
elif x==4:
    info()
x=input("\nPress Enter to proceed ")
print("_____________________________________________________________\n 1 Return to Substitution Cipher \n 2 Return to Home ")
x=input_validation_index([1,2])
if x==1:
    exec(open("ciphers\\substitutioncipher.py").read())
elif x==2:
    exec(open("main\\main.py").read())
