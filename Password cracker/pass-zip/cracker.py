import os
import time
import subprocess


process = subprocess.run('sh shell.sh', shell=True, check=True, timeout=5)


# File with most common passwords
passwords_file_name = "10-million-password-list-top-1000000.txt"

os.chdir('..')
parent_folder = os.getcwd()
passwords_file = open(parent_folder + '/' + passwords_file_name, "r")


for password in passwords_file:
    password = password.replace("\n", "")
    cmd = "unzip -P " + password + " secret.zip"

    # Not necessary
    time.sleep(2)

    # todo
    # Finish the program when the password is founded

    print(cmd)
    os.system(cmd)
