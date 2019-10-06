from telloUDP import TelloUDP
from time import sleep


if __name__ == '__main__':
    ip = '192.168.1.107'
    c = TelloUDP()
    c.start()
    print('sending command')
    c.sendCommand(ip,'command')
    while c.getCommand() == []:
        sleep(.1)
    print('sending takeoff')
    c.sendCommand(ip,'takeoff')
    while c.getCommand() == []:
        sleep(.1)
    print('sending land')
    c.sendCommand(ip,'land')
    while c.getCommand() == []:
        sleep(.1)
    print('stopping')
    print(c.getData())
    c.stop()