import random
import sys
import string

options_config = [False] * 6
options_desc = ['upper case', 'lower case', 'numbers', 'symbols', 'a initial key word', 'a final key word']
length = int(input("Put the length of the passwords: "))
amount = int(input("Put the amount of the passwords: "))


def set_passwords_options():
    for pos in range(0, 6):
        option = input(f'Want to have {options_desc[pos]} in the passwords?: ')
        if option == 'y':
            options_config[pos] = True
        elif option == 'n':
            pass
        else:
            print('Wrong option , please try again')
            sys.exit(-1)


def set_hardness_passwords():
    print("\nPress 'y' or 'n' to select options for passwords")
    set_passwords_options()


def set_random_word(complete_string, _length):
    if complete_string == "":
        return ""
    else:
        return "".join(random.choice(complete_string) for _ in range(_length))


def generate_passwords():
    complete_string = ""
    _initial_key_word = ""
    _final_key_word = ""
    if options_config[0]:
        complete_string += string.ascii_uppercase
    if options_config[1]:
        complete_string += string.ascii_lowercase
    if options_config[2]:
        complete_string += string.digits
    if options_config[3]:
        complete_string += string.punctuation
    if options_config[4]:
        _initial_key_word = input("Type the initial keyword to passwords: ")
    if options_config[5]:
        _final_key_word = input("Type the final keyword to passwords: ")

    total_length = length - len(_initial_key_word) - len(_final_key_word)
    with open('passwords.txt', 'w') as passwords_file:
        for _ in range(amount):
            intermediate_password = set_random_word(complete_string, total_length)
            final_password = _initial_key_word + intermediate_password + _final_key_word
            passwords_file.write(final_password + '\n')
            print(final_password)
    passwords_file.close()


if __name__ == '__main__':
    set_hardness_passwords()
    generate_passwords()
