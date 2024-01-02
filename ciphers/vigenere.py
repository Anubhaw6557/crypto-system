from my_functions import input_validation_index,input_validation_integer
def info():
    print('''________________________________________________________________________________________________________
Vigenère Cipher in Python

Overview:
The Vigenère cipher is a polyalphabetic substitution cipher that enhances the Caesar cipher by using a keyword.
It encrypts a message by shifting each letter based on a corresponding letter in the keyword.

Implementation:

- Key Generation:
  - The key is repeated to match the length of the message.
  - If the key is shorter than the message, it's repeated cyclically.

- Encryption:
  - Each letter in the message is shifted by the corresponding letter in the key.
  - The shift is performed independently for each letter.
  - The result is the encrypted message.

- Decryption:
  - Similar to encryption, but the shift is reversed.
  - Each letter in the encrypted message is shifted back using the key.''')
def encode():
    print("_________________________________________________")
    message=input("Enter Message ")
    key=input_validation_integer("Enter Key ")
    len_message=len(message)
    len_key=len(key)
    new_message=""
    k=0
    for j in range(0,len_message):
        if message[j]==" ":
            new_message=new_message+" "
        else:
            Index_m=EA.find(message[j])
            Index_k=EA.find(key[k%len_key])
            index_nm=Index_m+Index_k
            new_message=new_message+EA[index_nm%26]
            k=k+1
    print("Encrypted Message",new_message)
def decode():
    print("_________________________________________________")
    message=input("Enter CipherText ")
    key=input_validation_integer("Enter Key ")
    len_message=len(message)
    len_key=len(key)
    new_message=""
    k=0
    for j in range(0,len_message):
        if message[j]==" ":
            new_message=new_message+" "
        else:
            Index_m=EA.find(message[j])
            Index_k=EA.find(key[k%len_key])
            index_nm=26+Index_m-Index_k
            new_message=new_message+EA[index_nm%26]
            k=k+1
    print("Decrypted Message",new_message)
print("----------------------------Vigenere Cipher------------------------------\n 1 Encode \n 2 Decode \n 3 info")
EA="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
x=input_validation_index([1,2,3])
if x==1:
    encode()
elif x==2:
    decode()
elif x==3:
    info()
x=input("\nPress Enter to proceed ")
print("_____________________________________________________________\n 1 Return to Vigenere Cipher \n 2 Return to Home ")
x=input_validation_index([1,2])
if x==1:
    exec(open("ciphers\\vigenere.py").read())
elif x==2:
    exec(open("main\\main.py").read())