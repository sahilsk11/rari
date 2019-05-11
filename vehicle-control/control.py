import esc
#import steering
import RPi.GPIO as GPIO

esc_pwm = esc.setup()
#steering_pwm = steering.setup()
try:
    while (True):
            inp = input("Direction\n")
            speed = input("Speed\n")
            if (inp == 0):
                esc.set_direction(True)
                esc.run(esc_pwm, speed)
            elif (inp == 1):
                esc.set_direction(False)
                esc.run(esc_pwm, speed)
            elif (inp == 2):
                steering.set_direction(True)
                steering.run(steering_pwm, 100)
            elif (inp == 3):
                steering.set_direction(False)
                steering.run(steering_pwm, 100)
            elif (inp == 4):
                steering.set_direction(False)
                steering.stop(steering_pwm)
            else:
                esc.terminate(esc_pwm)
                steering.terminate(steering_pwm)
                break
            #run(time=-1)
except KeyboardInterrupt:
    esc.terminate(esc_pwm)