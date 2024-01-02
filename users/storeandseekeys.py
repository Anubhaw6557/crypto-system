import csv
from my_functions import input_validation_index,input_validation_integer
def store_keys(key_name,key):
    lst=[str(key_name), str(key)]
    with open("users\\keys.csv","a",newline="") as file:
        csv_writer=csv.writer(file)
        csv_writer.writerow(lst)
def see_key_names():
    with open("users\\keys.csv","r") as file:
        csv_reader=csv.reader(file)
        for row in csv_reader:
            print(row[0])
def see_key(key_name):
    with open("users\\keys.csv","r") as file:
        csv_reader=csv.reader(file)
        for row in csv_reader:
            if row[0]==str(key_name):
                print("key =",row[1])
                return(0)
        print("key name not found")
print("----------------------------------------------Keys-------------------------------------------\n 1 Store Key \n 2 See Key Names List \n 3 See a key")
x=input_validation_index([1,2,3])
print("________________________________________________________________________________________")
if x==1:
    key_name=input("Enter Key Name ")
    key=input("Enter Key ")
    store_keys(key_name,key)
elif x==2:
    see_key_names()
elif x==3:
    key_name=input("Enter Key Name ")
    see_key(key_name)
x=input("\nPress Enter to proceed ")
print("_____________________________________________________________\n 1 Return to Keys \n 2 Return to Home ")
x=input_validation_index([1,2])
if x==1:
    exec(open("users\\storeandseekeys.py").read())
else:
    exec(open("main\\main.py").read())
