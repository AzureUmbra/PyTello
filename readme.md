## Setting Up Python for Tello (Beginner)
1. Install Python, PyCharm, Git, and Packet Sender.
2. Open Pycharm and create a new project.
3. Click VCS->Git->Clone
4. At the top of this page, click *Clone or download*. Copy the link.
5. Paste it in the *URL* box in the PyCharm window.
6. Click *test* to ensure everything is set-up right.
7. Select a directory where you want to download the repository.
8. Click *Clone*. The project should open up after downloading.
## Setting Up Python for Tello
1. Git Clone this repo.
2. Sorry, this is not *pip install*-able, nor is it a binary wheel...yet. Just deal with the clone for now.
## Setting Up Tello for Python (Beginner)
1. Ensure you have access to your router's control panel.
2. Double Click the *telloWifiConnect.py* file on the left side.
3. Click Run->Run...->telloWifiConnect
4. Follow the instructions on the bottom of your screen. You will have to do this any time you go somewhere with different wifi.
5. When you want to put your tello back into normal mode (you have just put your tello into SDK mode), ensure it is turned
on, and then press and hold the power button for 5 seconds.
6. Login to your router's control panel and find the ip address of your tello. Write this down.
## Setting Up Tello for Python
1. Send a packet on UDP port 8889 to 192.168.10.1 with the message *command*.
2. Send another packet with the message *ap YOUR_SSID YOUR_PASSWORD*.
3. Login to your router and grab the tello ip (I recommend statically assigning it).
## Programming Your Tello (Beginner)
1. Right-Click the pyTello Folder and select New->Python File.
2. Name it whatever you want.
3. At the top, type `from telloUDP import TelloError`
4. On the next line, add `from pyTello import PyTello`
5. Skip down a few lines and add `if __name__ == '__main__':`
6. All of your tello code will go here, indented one tab. See *pyTelloExample.py* for some example code.
## Programming Your Tello
1. Import PyTello from pyTello.
2. Import TelloError from telloUDP (not sure why this isn't automatic, but oh well).
3. Due to threading, everything must be run from inside `if __name__ == '__main__':`
4. Feel free to directly use the telloUDP module, hope you like threading!
## Common Errors
- Did you check to see if you have *Packet Sender* or similar software running? Only one port can be bound at a time.
Close the software and try again.
## Notes to Python Beginners
If you ever see a function or file beginning with a single underscore, that function has been declared as "private",
and as such, the developer expects you to never call that function or import that file. Bad things can happen if you do.

If you ever see a double underscore, that is a reserved python name, and as such, you should never overwrite or call it 
directly. If you do, understand that you are assuming responsibility for what that function previously did.
## Current Issues
- Tello sometimes requires *"command"* to be sent twice if it has just been turned on
- *getData()* always returns an empty list, function is currently useless