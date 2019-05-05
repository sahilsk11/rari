import esc
import ultrasonic_sensor
import time

speed = 100

esc_pwm = esc.setup()
esc.set_direction(False)
while (True):
    distance = ultrasonic_sensor.distance()
    print(distance)
    if (distance < 40):
        speed = 30
    if (distance < 20):
        speed = 10
    if (distance < 10):
        esc.set_direction(True)
        esc.run(esc_pwm, 50)
        time.sleep(0.1)
        esc.terminate(esc_pwm)
        break
    else:
        speed = 100
    esc.run(esc_pwm, speed)
    time.sleep(0.1)
        