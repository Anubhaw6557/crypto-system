from my_functions import input_validation_index,input_validation_integer
print("----------------------WELCOME To Home--------------------- \n 1 Ceaser Cipher \n 2 Substitution Cipher \n 3 Homophonic Substitution cipher \n 4 XOR Encryption \n 5 Vigenere Cipher \n 6 See and Store Keys \n 7 Receive Or Send Messages \n 8 RSA Encryption \n 9 Diffie Hellman")
x=input_validation_index([1,2,3,4,5,6,7,8,9])
if x==1:
    exec(open("ciphers\\ceasercipher.py").read())
elif x==2:
    exec(open("ciphers\\substitutioncipher.py").read())
elif x==3:
    exec(open("ciphers\\homophonicsubs.py").read())
elif x==4:
    exec(open("ciphers\\XOR.py").read())
elif x==5:
    exec(open("ciphers\\vigenere.py").read())
elif x==6:
    exec(open("users\\storeandseekeys.py").read())
elif x==7:
    exec(open("users\\client.py").read())
elif x==8:
    exec(open("ciphers\\RsaEncryption.py").read())
elif x==9:
    exec(open("ciphers\\diffie hellman.py").read())