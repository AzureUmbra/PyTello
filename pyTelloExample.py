from pyTello import PyTello
from telloUDP import TelloError
from time import sleep




if __name__ == '__main__':  # Ensure all files that use PyTello have this or threading errors occur

    # This is the IP address of the tello you got from your router.
    myTelloIP = '192.168.1.107'

    # Creates a PyTello instance and opens the connections.
    tello = PyTello(myTelloIP)
    tello.start()

    # Tells the tello to get ready to receive commands.
    # We are using a print statement as the "sendCommandNoWait" function does not waits for a response from the tello
    #     but it does return True if it was able to send it.
    print(tello.sendCommandNoWait('command'))

    # Tells the tello to take off.
    # We are using print here as the "sendCommand" function waits for a response from the tello.
    # Sometimes you may get more than one item in the list that returns. This is a list of all previously unread responses
    #     from the tello.
    print(tello.sendCommand('takeoff'))

    # Tell the tello to fly 100cm forward.
    print(tello.sendCommandNoWait('forward 100'))

    # We have to call this because we didn't wait for a response from the tello, but we still have to let it finish
    #     before flying backward.
    sleep(10)

    # If you don't want to guess on the time to sleep, here is another way to wait.
    # First, you make sure there are no unread commands
    print(tello.getCommandResponse())
    # Then, tell the tello to fly 100cm back.
    print(tello.sendCommandNoWait('back 100'))
    # Set a flag for a loop, and create the loop.
    waiting = False
    while waiting is False:
        # Sleep in short increments...
        sleep(0.1)
        # ...and keep checking for a response, assigning the response to your flag
        waiting = tello.getCommandResponse()
    # Once data comes in, the loop will stop, and you can print the response if you want to.
    print(waiting)

    # Tell the tello to spin 360 degrees clockwise.
    print(tello.sendCommand('cw 360'))

    # Tell the tello to land.
    print(tello.sendCommand('land'))

    # Cleanly exit the PyTello instance. Once you close it, you have to create a new one to begin flying again.
    # Failing to call "stop()" can result in connection issues to your tello.
    # If this happens, just wait about 5 minutes or restart your computer.
    tello.stop()
