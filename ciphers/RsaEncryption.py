import random 
from sympy import randprime
from my_functions import input_validation_index,input_validation_integer,input_validation_length
AT=r''' !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'''
def message_To_Number(message):
    num=""
    for i in message:
        index=AT.find(i)
        num=num+str(index).zfill(2)
    return(int(num))
def Number_to_Message(num):
    num_str=str(num)
    message=""
    for i in range(0,len(num_str)//2):
        index=int(num_str[2*i:2*(i+1)])
        message=message+AT[index]
    return(message)
def generate_prime_number(bits=5):
    prime_num=randprime(2**(bits-1),2**bits)
    return(prime_num)
def generate_private_key_exponent(p,q,public_key_exponent):
    eu_n=(p-1)*(q-1)
    x_1=1
    x_2=0
    y_1=0
    y_2=1
    a=public_key_exponent
    while eu_n!=0:
        c=a//eu_n
        a_=a
        a=eu_n
        eu_n=a_%eu_n
        x_1_=x_1
        x_1=x_2
        x_2=x_1_-c*x_2
        y_1_=y_1
        y_1=y_2
        y_2=y_1_-c*y_2
    return(x_1%((p-1)*(q-1)))
def generate_key_pair(bits):
    p=generate_prime_number(bits)
    q=generate_prime_number(bits)
    n=p*q
    public_key_exponent=65537
    private_key_exponent=generate_private_key_exponent(p,q,public_key_exponent)
    public_key="n = "+str(n)+"\ne = "+str(public_key_exponent)
    private_key="p = "+str(p)+"\nq = "+str(q)+"\nd = "+str(private_key_exponent)
    return public_key,private_key
def Encrypt_Message(message,public_key_exponent,n):
    number=message_To_Number(message)
    e_message_num=pow(number,public_key_exponent,n)
    return e_message_num
def Decrypt_message(number,private_key_exponent,n):
    message_num=pow(number,private_key_exponent,n)
    message=Number_to_Message(message_num)
    return(message)
def info():
    print('''''')
print("----------------------------------------------RSA Encryption-------------------------------------------\n 1 Generate Key Pair \n 2 Encrypt Message \n 3 Decrypt Message")
x=input_validation_index([1,2,3])
print("________________________________________________________________________________________")
if x==1:
    bits=input_validation_integer("Enter length of key in bits ")//2
    public_key,private_key=generate_key_pair(bits)
    print("Public Key",public_key,"\nPrivate Key",private_key)
elif x==2:
    n=input_validation_integer("Enter n ")
    public_key_exponent=input_validation_integer("Enter e ")
    len_n=len(str(n))//2-1
    message=input_validation_length(len_n)
    e_message_num=Encrypt_Message(message,public_key_exponent,n)
    print("Encrypted Message =",e_message_num)
elif x==3:
    n=input_validation_integer("Enter n ")
    private_key_exponent=input_validation_integer("Enter d ")
    e_message_num=input_validation_integer("Enter Encrypted Message ")
    message=Decrypt_message(e_message_num,private_key_exponent,n)
    print("message =",message)
x=input("\nPress Enter to proceed ")
print("____________________________________________________________________________________________\n 1 Return to Rsa Encryption \n 2 Return to Home ")
x=input_validation_index([1,2])
if x==1:
    exec(open("ciphers\\RsaEncryption.py").read())
elif x==2:
    exec(open("main\\main.py").read())
