import pyautogui
import subprocess
import sys
import os

# File with most common passwords
passwords_file_name = "10-million-password-list-top-1000000.txt"

secret = input("Set the secret password: ")

# notepad, vim, sublime, etc
program_name = "mousepad"


def crack_password_on(file):
    file_name = "a_name"
    subprocess.Popen([program_name, file_name])
    for password in file:
        password = password.replace("\n", "")
        pyautogui.write(password, interval=0.1)
        pyautogui.press('enter')
        if password != secret:
            print("Wrong password: " + password)
        else:
            print("I found the secret password! Is:" + password)
            sys.exit(1)


os.chdir('..')
parent_folder = os.getcwd()
passwords_file = open(parent_folder + '/' + passwords_file_name, "r")
crack_password_on(passwords_file)
