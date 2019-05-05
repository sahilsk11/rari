import RPi.GPIO as GPIO
from time import sleep

enable_pin = 4
drivetrain_pin_1 = 14
drivetrain_pin_2 = 17
pwm = None


GPIO.setmode(GPIO.BCM)
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(drivetrain_pin_1, GPIO.OUT)
GPIO.setup(drivetrain_pin_2, GPIO.OUT)
pwm = GPIO.PWM(enable_pin, 100)
pwm.start(0)


# Adjust pin 7
# Pin 7 is enable
# Second parameter is "power" to apply out of 100

def set_direction(direction):
    # direction True = forward
    # Sets direction to forward
    GPIO.output(drivetrain_pin_1, not direction)
    GPIO.output(drivetrain_pin_2, direction)


# Changes the speed of the motor. Not used for moving the vehicle.
def set_power(duty_cycle):
    pwm.ChangeDutyCycle(duty_cycle)
    GPIO.output(enable_pin, True)


# Moves the vehicle with certain set speed
def run(power=50, time=-1):
    set_power(power)
    if time > -1:
        sleep(time)


def stop():
    # Turns of enable
    set_power(0)


def terminate():
    pwm.stop()
    GPIO.cleanup()


def custom_control():
    try:
        while (True):
            inp = int(input("Direction\n"))
            if (inp == 0):
                set_direction(True)
            elif (inp == 1):
                set_direction(False)
            else:
                terminate()
                break
            run(time=-1)
    except KeyboardInterrupt:
        terminate()


set_direction(True)
set_power(90)
custom_control()

'''
run()
set_direction(False)
run()
terminate(pwm)
'''
