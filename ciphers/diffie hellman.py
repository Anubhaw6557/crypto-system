from my_functions import input_validation_index,input_validation_integer
import random
from sympy import randprime,factorint
def info():
    print('''______________________________________________________________________________________________________________________________
Overview:
The Diffie-Hellman key exchange is a cryptographic protocol that allows two parties to establish a shared secret over an insecure communication channel. This shared secret can then be used for secure communication, such as encrypting and decrypting messages.

Key Features:
1. Public Key Exchange: Diffie-Hellman is a public key cryptography algorithm that enables secure key exchange.
2. Secure Key Generation: The shared secret key is generated independently by both parties and remains secure even if public keys are intercepted.
3. Computational Complexity: The security of Diffie-Hellman relies on the difficulty of solving the discrete logarithm problem.

Steps in Diffie-Hellman Key Exchange:
1. Key Generation: Both parties generate their public and private key pairs.
2. Public Key Exchange: Each party shares its public key with the other party.
3. Shared Secret Computation: Using their own private key and the received public key, each party independently computes the shared secret key.
4. Symmetric Key Usage: The shared secret key can now be used as a symmetric key for encrypting and decrypting further communication.

Mathematical Representation:
- Let g be a primitive root modulo p, where p is a large prime number.
- Parties select private keys a and b (randomly chosen integers).
- They compute their public keys:
  - A = g^a mod p (Party A's public key)
  - B = g^b mod p (Party B's public key)
- Shared Secret Calculation:
  - s = B^a mod p (Computed by Party A)
  - s = A^b mod p (Computed by Party B)

Security Considerations:
- Diffie-Hellman provides a secure key exchange, but it doesn't authenticate the communicating parties.
- Additional protocols (e.g., digital signatures) are recommended to ensure the authenticity of the exchanged public keys.

Use Cases:
- Secure Communication: Used in cryptographic protocols like TLS/SSL for secure communication over the internet.
- Key Establishment: Establishing shared secret keys for symmetric-key encryption in secure communication systems.''')
def Private_key():
    print("___________________________________________________________________________________________")
    Prime=input_validation_integer("Enter Prime Number ")
    private_key=random.randrange(2,Prime-2)
    print("Private Key",private_key)
def primitive_root_find(prime_num):
    prime_factors=factorint(prime_num-1)
    prime_factors=list(prime_factors.keys())
    for i in range(0,len(prime_factors)):
        prime_factors[i]=(prime_num-1)//prime_factors[i]
    while True:
        candidate=random.randrange(2,prime_num-1)
        l=0
        for i in prime_factors:
            if pow(candidate,i,prime_num)==1:
                l=1
                break
        if l==0:
            break
    return(candidate)
def prime_number():
    print("___________________________________________________________________________________________")
    bits=input_validation_integer("Enter Length Bits ")
    prime_num=randprime(2**(bits-1),2**bits)
    print("Prime Number",prime_num)
def pri_root():
    print("___________________________________________________________________________________________")
    pri_num=input_validation_integer("Enter Prime Number ")
    print("Primitive Root Modulo",primitive_root_find(pri_num))
def modular_exponential(exponent,base,modulus):  
    result=1
    exponent_bin=(bin(exponent))[2:]
    for i in range (0,len(exponent_bin)):
        result=(result*result)%modulus
        if exponent_bin[i]=="1":
            result=(result*base)%modulus
    return result
def Public_key():
    print("__________________________________________________________________________________________")
    private_key=input_validation_integer("Enter Private Key ")
    prime_number=input_validation_integer("Enter Prime Number ")
    pri_root_modulo=input_validation_integer("Enter Primitive Root Modulo ")
    public_key=modular_exponential(private_key,pri_root_modulo,prime_number)
    print("Public Key -",public_key)
def Secret_Key():
    print("__________________________________________________________________________________________")
    private_key=input_validation_integer("Enter Private Key ")
    prime_number=input_validation_integer("Enter Prime Number ")
    public_key=input_validation_integer("Enter Public Key ")
    secret_key=modular_exponential(private_key,public_key,prime_number)
    print("Secret Key -",secret_key)
print("---------------------------------------------Diffie Hellman----------------------------------------------\n 1 Generate Public Key \n 2 Generate Secret Key\n 3 Generate Prime Number\n 4 Generate Primitive Root \n 5 Generate Private Key \n 6 Info")
x=input_validation_index([1,2,3,4,5,6])
if x==1:
    Public_key()
elif x==2:
    Secret_Key()
elif x==3:
    prime_number()
elif x==4:
    pri_root()
elif x==5:
    Private_key()
elif x==6:
    info()
x=input("\nPress Enter to proceed ")
print("_____________________________________________________________\n 1 Return to Diffie Hellman \n 2 Return to Home ")
x=input_validation_index([1,2])
if x==1:
    exec(open("ciphers\\diffie hellman.py").read())
else:
    exec(open("main\\main.py").read())
        