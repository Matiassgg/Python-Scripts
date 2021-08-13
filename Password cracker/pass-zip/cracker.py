import os
import subprocess


process = subprocess.run('sh shell.sh', shell=True, check=True)


# File with most common passwords
passwords_file_name = "10-million-password-list-top-1000000.txt"

os.chdir('..')
parent_folder = os.getcwd()
passwords_file = open(parent_folder + '/' + passwords_file_name, "r")


for password in passwords_file:
    password = password.replace("\n", "")
    cmd = "unzip -P " + password + " secret.zip"
    print(cmd)
    os.system(cmd)
