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