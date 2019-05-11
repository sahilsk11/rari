# Vehicle Setup (software)

To be honest, setting up the software for the vehicle is unnecessarily tricky. Because of this, I've set up starter code that handles all of it on the back-end. Use this doc as a reference.

All of the code is stored in a file called `esc.py`.

## Documentation

### Getting Started

Typically when you are writing a file that will move the car, start by importing the pre-defined esc (electronic speed control) library. This is the file I've compiled that makes moving the car easier.

`import esc`

### Set the Direction

Now that the `esc.py` library is imported, we can utilize all of it's functions. To set the car to move forward or backward, use:

`esc.set_direction(direction)`

where direction is the boolean value `True` or `False` for forward or backward. This will depend on the wiring of your kit, so try both to see which works.

Note that `set_direction` does not move the car yet - it only sets the direction to move in.

### Setting the Speed

`esc.set_speed(power_percentage)`

Where `power_percentage` is a percentage between 0 and 100.

Reminder that `set_speed` still does not move the vehicle yet - it only sets the speed for when the vehicle starts.

### Moving the Car

Ok, we're finally here!

`esc.move()`

This is the command that finally puts everything together to move the vehicle. It's used after all of the previous commands.

### Stopping the Car

When we're done, we have two commands:

- `esc.stop()` stops the vehicle in place.
- `esc.terminate()` is used to end the program at the end

## To-Do: Get the car moving

#### Starting with the starter code, create your first program to get the car moving.

Using each of the commands listed above, create a program that moves the car forward for 5 seconds, stops, moves the car backwards for 5 seconds, and terminates.

Start with the starter code `stage0.py`.

#### Solution

```
esc.set_direction(True)
esc.set_power(100)
esc.move()
time.sleep(5)
esc.stop()
esc.set_direction(False)
# we don't need to change power because it is already at 100
esc.move()
time.sleep(5)
esc.stop()
esc.terminate()
```

Onwards!