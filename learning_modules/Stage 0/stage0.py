'''

Starter code for Stage 0

'''

import esc #everytime you want to implement car control, import the esc library
import time

esc.set_direction(True) #sets the direction to forward



# to-do: implement code to set the power to 100%, move forward



time.sleep(5) #pauses the program for 5 seconds

esc.set_direction(False) #sets the direction to backward



#to-do: move backwards!



esc.terminate() # ends the program
