# Python Scripts
This is a compilation of various concepts of security and other fun scripts to play with thus, such as, 
how to build a simple keylogger, 
a ransomware or 
build a random password's generator.


## Keylogger
1. Modules requirements:
    - pynput
    - logging
2. Description:
    - The 'keylogger ' registre the keys that you press, 
      once execute the script, you need to set a folder that you specify to save the registry file,  
      if you want a better challenge you can prove:
      [this](https://www.thepythoncode.com/article/write-a-keylogger-python)
      
## Random passwords generator
1. Modules requirements:
    - random
    - sys
    - string
2. Description:
    - This script consist in 6 options to generate a random password.
    This code is totally open source use this code as you like, like the others.
    - The password's generated are saved on a file with extension .txt
## Ransomware
1. Modules requirements:
    - cryptography
    - os
    - sys
2. Description:
    - This ransomware encrypts the files that are indicated in a specific folder when run the script.
    - Note, to decrypt the folder that was encrypted previously,
    the key generated must have been in the same folder that decrypt.py.
    - Another thing is that the key generated after encrypting the folder, 
      if we were in reality, the key shouldn't be generated ;).
### General notes
- All scripts are tested on Windows 10-64 bits version, with Python 3.8 version.
- To convert the .py to .exe you can use [pyinstaller](https://www.pyinstaller.org/).
- All the source codes are for educational purposes only.
    I'M NOT RESPONSIBLE FOR ANY BAD AND MALICIOUS USE OF THESE.