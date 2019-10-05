from _telloUDP import TelloUDP
from time import sleep

if __name__ == '__main__':  # Ensure all files that use TelloUDP have this or threading errors occur

    # Store my tello ip as a variable
    ip = '192.168.1.107'

    # Create a TelloUPD instance and start the threads
    tello = TelloUDP()
    tello.start()

    # Put the tello into command mode
    print('Command Mode')
    tello.sendCommand(ip,'command')

    # Just give it a second...never a bad idea
    sleep(1)

    # Launch the tello
    print('Takeoff')
    tello.sendCommand(ip,'takeoff')

    sleep(5)

    # Send the tello forward 100cm
    print('forward')
    tello.sendCommand(ip,'forward 100')

    sleep(10)

    # Bring the tello back 100cm
    print('back')
    tello.sendCommand(ip,'back 100')

    sleep(10)

    # Rotate 360 degrees
    print('rotate')
    tello.sendCommand(ip,'cw 360')

    sleep(10)

    # Tell the tello to land
    print('land')
    tello.sendCommand(ip,'land')

    # Shut down the TelloUDP instance
    tello.stop()