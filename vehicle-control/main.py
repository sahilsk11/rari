#!/usr/bin/python

from PCA9685 import PCA9685
import time

Dir = [
    'forward',
    'backward',
]
pwm = PCA9685(0x40, debug=False)
pwm.setPWMFreq(50)

class MotorDriver():
    def __init__(self):
        self.PWMA = 0
        self.AIN1 = 1
        self.AIN2 = 2
        self.PWMB = 5
        self.BIN1 = 3
        self.BIN2 = 4

    def MotorRun(self, motor, index, speed):
        if speed > 100:
            return
        if(motor == 0):
            pwm.setDutycycle(self.PWMA, speed)
            if(index == Dir[0]):
                pwm.setLevel(self.AIN1, 0)
                pwm.setLevel(self.AIN2, 1)
            else:
                pwm.setLevel(self.AIN1, 1)
                pwm.setLevel(self.AIN2, 0)
        else:
            pwm.setDutycycle(self.PWMB, speed)
            if(index == Dir[0]):
                pwm.setLevel(self.BIN1, 0)
                pwm.setLevel(self.BIN2, 1)
            else:
                pwm.setLevel(self.BIN1, 1)
                pwm.setLevel(self.BIN2, 0)

    def stop(self, motor='movement'):
        if (motor == 'steering'):
            motor = 1
        elif (motor == 'movement'):
            motor = 0
        if (motor == 0):
            pwm.setDutycycle(self.PWMA, 0)
        else:
            pwm.setDutycycle(self.PWMB, 0)

    def turn(self, direction, speed=100):
        if (direction == 'left'):
            direction = 'forward'
        else:
            direction = 'backward'
        self.MotorRun(1, direction, speed)

    def move(self, direction, speed=100):
        self.MotorRun(0, direction, speed)

    def terminate(self):
        self.stop(0)
        self.stop(1)

if (__name__ == "__main__"):
    rari = MotorDriver()
    rari.move('forward', 50)
    rari.stop()
    time.sleep(1)
    rari.turn('left')
    time.sleep(1)
    rari.turn('right')
    time.sleep(1)
    rari.terminate()
