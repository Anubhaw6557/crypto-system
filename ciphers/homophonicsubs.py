import random
from my_functions import input_validation_index,input_validation_integer,input_validation_string
def info():
    print('''____________________________________________________________________________________________
Overview:
A homophonic cipher is a cryptographic algorithm that replaces each letter in the 
plaintext with multiple symbols. This technique adds complexity to the encryption 
process and makes frequency analysis more challenging. Homophonic ciphers are a 
type of substitution cipher where each character can map to several possible 
substitutes.
''')
def encode(y):
    print("____________________________________________________________________________________")
    if y==1:
        set=EA
    if y==2:
        with open("ciphers\\homocusset.txt","r") as file:
            lines=file.readlines()
            set=lines[0]
    with open("ciphers\\humosubs.txt","r") as file:
        lines=file.readlines()
        replacement_set=eval(lines[y-1].strip())
    len_set=len(set)
    message=input_validation_string(set,"Enter Message ")
    new_message=""
    for kl in range(0,len(message)):
        index=set.find(message[kl])
        j=random.randrange(0,len(replacement_set[index]))
        new_message=new_message+replacement_set[index][j]
    print("Encrypted text",new_message)
def decode(y):
    if y==1:
        set=EA
        len_set=len(set)
    if y==2:
        with open("ciphers\\homocusset.txt","r") as file:
            lines=file.readlines()
            set=lines[0]
    with open("ciphers\\humosubs.txt","r") as file:
        lines=file.readlines()
        replacement_set=eval(lines[y-1].strip())
    e_text=str(input("_______________________________________________________________________\nEnter Cipher Text "))
    message=""
    len_str=len(replacement_set[0][0])
    for i in range(0,len(e_text)//len_str):
        elem=e_text[len_str*i:len_str*i+len_str]
        for j in range(0,len(set)):
            if elem in replacement_set[j]:
                break
        message=message+set[j]
    print("Decrypted Text",message)
def see_mapping():
    print("_____________________________________________________________\n 1 English Alphabets[A-Z] and Space\n 2 Custom One")
    y=input_validation_index([1,2])
    if y==1:
        set=EA
    if y==2:
        with open("ciphers\\homocusset.txt","r") as file:
            lines=file.readlines()
            set=lines[0]
    with open("ciphers\\humosubs.txt","r") as file:
        lines=file.readlines()
        replacement_set=eval(lines[y-1].strip())
    for i in range(0,len(set)):
        print(set[i],"-",replacement_set[i])
def change_mapping():
    print("_____________________________________________________________\n 1 English Alphabets[A-Z] and Space(Random shuffle)\n 2 Custom One")
    y=input_validation_index([1,2])
    if y==1:
        set=EA
        lst_num=[]
        replacement_set=[]
        lst_num = [str(i).zfill(3) for i in range(1, 102)]
        random.shuffle(lst_num)
        j=0
        for k in range(0,len(set)):
            lst_elem=[]
            a=j+proportion_lst[k]
            while j<a:
                lst_elem.append(lst_num[j])
                j=j+1
            replacement_set.append(lst_elem)
    if y==2:
        set=""
        replacement_set=[]
        print("_______________________________________________________\nEnter Mapping like (a-['01','ab'] ; b-['20','mn']) use strings of same length")
        mapping=input()
        mapping_lst=mapping.split(";")
        for k in range(0,len(mapping_lst)):
            mapping_lst_elem=mapping_lst[k]
            set=set+((mapping_lst_elem.split("-"))[0]).strip()
            replacement_set.append(eval((mapping_lst_elem.split("-"))[1]))
        with open("ciphers\\homocusset.txt","w") as file:
            file.write(set)
    with open("ciphers\\humosubs.txt","r") as file:
        replacement_sets=file.readlines()
        replacement_sets[y-1]=str(replacement_set)+"\n"
        replacement_sets_str="".join(replacement_sets)
    with open("ciphers\\humosubs.txt","w") as file:
        file.write(replacement_sets_str)
print("---------------------------H0M0PH0NIC 5U357ITU7I0N CIPH3R--------------------------- \n 1 Encode \n 2 Decode \n 3 Change and See Mpping \n 4 info")
EA="ABCDEFGHIJKLMNOPQRSTUVWXYZ "
proportion_lst=[8,2,2,4,12,2,2,6,7,1,1,4,2,7,7,2,1,6,6,9,2,1,2,1,2,1,1]
x=input_validation_index([1,2,3,4])
if x==1:
    print("_____________________________________________________________\n 1 Use English Alphabets[A-Z] and Space\n 2 Use Custom One")
    y=input_validation_index([1,2])
    encode(y)
if x==2:
    print("_____________________________________________________________\n 1 Use English Alphabets[A-Z] and Space\n 2 Use Custom One")
    y=input_validation_index([1,2])
    decode(y)
if x==3:
    print("__________________________________________________________________\n 1 Change Mapping \n 2 See Mapping")
    y=input_validation_index([1,2])
    if y==1:
        change_mapping()
    if y==2:
        see_mapping()

k=input("\nPress Enter To Proceed ")
print("_____________________________________________________________\n 1 Return to Homoohonic Substition Cipher \n 2 Return to Home ")
x=input_validation_index([1,2])
if x==1:
    exec(open("ciphers\\homophonicsubs.py").read())
else:
    exec(open("main\\main.py").read())