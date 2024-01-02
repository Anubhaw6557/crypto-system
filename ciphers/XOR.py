from my_functions import input_validation_index,input_validation_integer
def encode():
    print("_______________________________________________________________________________________")
    message=input("Enter Message ")
    len_message=len(message)
    key=input("Enter Key ")
    len_key=len(key)
    new_key=""
    for i in range(0,len_message//len_key):
        new_key=new_key+key
    new_key=new_key+key[0:len_message%len_key]
    new_message=""
    for j in range(0,len_message):
        new_message_elem=(hex(ord(message[j])^ord(new_key[j])))[2:]
        new_message=new_message+new_message_elem.zfill(2)
    print("Encryted Message(in hexadecimal) :",new_message)
def decode():
    print("______________________________________________________________________________________")
    e_message=input("Enter CipherText ") 
    len_message=len(e_message)//2
    key=input("Enter Key ")
    len_key=len(key)
    new_key=""
    for i in range(0,len_message//len_key):
        new_key=new_key+key
    new_key=new_key+key[0:len_message%len_key]
    message=""
    for l in range(0,len_message):
        message_elem=chr(int(e_message[2*l:2*(l+1)],16)^ord(new_key[l]))
        message=message+message_elem
    print("Decrypted Message",message)
print("----------------------------XOR Encryption------------------------------\n 1 Encode \n 2 Decode")
x=input_validation_index([1,2])
if x==1:
    encode()
elif x==2:
    decode()
x=input("\nPress Enter to proceed ")
print("_____________________________________________________________\n 1 Return to Xor Encryption \n 2 Return to Home ")
x=input_validation_index([1,2])
if x==1:
    exec(open("ciphers\\XOR.py").read())
else:
    exec(open("main\\main.py").read())