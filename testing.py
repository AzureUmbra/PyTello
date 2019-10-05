from _telloUDP import TelloUDP
from time import sleep


if __name__ == '__main__':
    c = TelloUDP()
    c.start()
    x = c.sendCommand('127.0.0.1','this is a test of a command')
    print('--{}'.format(x))
    for i in range(15):
        sleep(1)
        print(c.getData())
    c.stop()