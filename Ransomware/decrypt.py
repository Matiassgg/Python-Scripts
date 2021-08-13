from cryptography.fernet import Fernet
from shared import get_path_mode_on_so
import os
import sys
  

def set_path():
    return input("Specify the folder to recover:")


def load_key():
    try:
        return open('key.key', 'rb').read()
    except IOError:
        print("The key wasn't find in the folder, please try again")
        sys.exit(1)


def decrypt(_items, _key):
    f = Fernet(_key)
    for item in _items:
        with open(item, 'rb') as file:
            encrypted_data = file.read()
        decrypt_data = f.decrypt(encrypted_data)
        with open(item, 'wb') as file:
            file.write(decrypt_data)


def remove_on_directory(_directory, _file):
    _full_path = path_to_decrypt + get_path_mode_on_so() + _file
    if os.path.exists(_full_path):
        os.remove(_full_path)


if __name__ == '__main__':
    path_to_decrypt = set_path()
    remove_on_directory(path_to_decrypt, 'rescue.txt')

    items = os.listdir(path_to_decrypt)
    full_path = [path_to_decrypt + get_path_mode_on_so() + item for item in items]

    key = load_key()
    decrypt(full_path, key)
