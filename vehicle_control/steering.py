import RPi.GPIO as GPIO
from time import sleep

def setup(enable_pin=37):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(33, GPIO.OUT)
    GPIO.setup(35, GPIO.OUT)
    GPIO.setup(37, GPIO.OUT)
    pwm=GPIO.PWM(37, 100)
    pwm.start(0)
    return pwm
    
#Adjust pin 7
#Pin 7 is enable
#Second parameter is "power" to apply out of 100

def set_direction(direction):
    #direction True = forward
    #Sets direction to forward
    GPIO.output(35, not direction)
    GPIO.output(33, direction)

def set_power(pwm, duty_cycle):
    GPIO.output(37, False)
    pwm.ChangeDutyCycle(duty_cycle)

def run(pwm, power, time=-1, enable_pin=37):
#Turns on enable
    set_power(pwm, power)
    if (time > -1):
        sleep(time)

def stop(pwm, enable_pin=37):
    #Turns of enable
    set_power(pwm, 0)

def terminate(pwm):
    pwm.stop()
    GPIO.cleanup()
    
def custom_control(pwm):
    while (True):
        inp = input("Direction\n")
        if (inp == 0):
            set_direction(True)
        elif (inp == 1):
            set_direction(False)
        else:
            terminate(pwm)
            break
        run(time=-1)
        
''' 
pwm = setup()
set_direction(True)
set_power(pwm, 100)
custom_control(pwm)
'''
'''
run()
set_direction(False)
run()
terminate(pwm)
'''