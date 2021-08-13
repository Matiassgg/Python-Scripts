import hashlib
import sys
import os

input_hash = input("Enter md5 hash of victim: ")

passwords_file_name = "10-million-password-list-top-1000000.txt"
os.chdir('..')
parent_folder = os.getcwd()
passwords_file = open(parent_folder + '/' + passwords_file_name, "r")


for password in passwords_file:
    password = password.replace("\n", "")
    enc = password.encode('utf-8')
    digest = hashlib.md5(enc.strip()).hexdigest()

    print("password " + password + " = " + digest)

    if input_hash == digest:
        print("password is found! password is: " + password)
        sys.exit(1)
