from _telloUDP import TelloUDP
from time import sleep


if __name__ == '__main__':
    ip = '192.168.1.107'
    c = TelloUDP()
    c.start()
    c.sendCommand(ip,'command')
    sleep(1)
    c.sendCommand(ip,'takeoff')
    sleep(5)
    for i in range(0,50):
        c.sendCommand(ip,'rc 0 {} 0 0'.format(i))
        print(c.getCommand())
    for i in range(100,-51,-1):
        c.sendCommand(ip,'rc 0 {} 0 0'.format(i))
        print(c.getCommand())
    for i in range(-49,1):
        c.sendCommand(ip,'rc 0 {} 0 0'.format(i))
        print(c.getCommand())
    c.sendCommand(ip,'land')
    c.stop()