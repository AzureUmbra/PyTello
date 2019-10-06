from telloUDP import TelloUDP
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

    # Wait for the tello to respond that it is done with the previous command
    while tello.getCommand() == []:
        sleep(0.1)

    # Send the tello forward 100cm
    print('forward')
    tello.sendCommand(ip,'forward 100')

    # Wait for the tello to respond that it is done with the previous command
    while tello.getCommand() == []:
        sleep(0.1)

    # Bring the tello back 100cm
    print('back')
    tello.sendCommand(ip,'back 100')

    # Wait for the tello to respond that it is done with the previous command
    while tello.getCommand() == []:
        sleep(0.1)

    # Rotate 360 degrees
    print('rotate')
    tello.sendCommand(ip,'cw 360')

    # Wait for the tello to respond that it is done with the previous command
    while tello.getCommand() == []:
        sleep(0.1)

    # Tell the tello to land
    print('land')
    tello.sendCommand(ip,'land')

    # Shut down the TelloUDP instance
    tello.stop()