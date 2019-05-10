import image_processing.vision_api as vision
#import vehicle_control.esc as esc

# Movement variable defines the direction of the vehicle
#   1 means forward
#   0 means stop
movement = 1

# Stop detected signals if a stop sign is seen anywhere in the frame
stop_detected = vision.is_stop_sign("images/stopsign.txt")

while True:
    try:
        if stop_detected:
            movement = 0
        else:
            movement = 1
        if movement == 1:
            print("moving forward")
        else:
            print("stopped")
        stop_detected = vision.is_stop_sign("images/stopsign.txt")
    except KeyboardInterrupt:
        exit(0)
