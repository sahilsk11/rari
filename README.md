# :red_car: Rari
## Let's make self-driving technology accessible to everyone.

## Welcome!
Welcome to Rari! The goal of this project is to create an open source kit and code base for anyone to build their own autonomous vehicle prototype.
The project is broken up into 3 components:

### 1. Self driving technology
- The current model uses Google Vision API calls to detect object such as stop signs, road markers, etc. to decide to move or not. (primitive, but works and is easy to learn!)
- Ultrasonic sensor is used to detect objects and stop if needed.
- ROOM FOR IMPROVEMENT: develop custom Tensorflow model to detect images or shapes in realtime

### 2. The hardware kit
- Most standard remote controlled cars are built two DC motors, for movement and steering. Using a Raspberry Pi 0, motor chip, and breadboard, it's possible to completely remove existed hardware and replace it with these components.
- However, these components are clunky and tricky to put together; especially the motor chip.

### 3. The user side
- Rari is only as awesome as the people who use it! I envision having Rari kits be accessible mostly to middle schoolers and high schoolers, and developing learning modules and creating libraries that they can build on top of can be complex.
- I plan to create customed python libraries that build on top of our classes that can help students learn without the overhead of starting from scratch. I need the most help here!

### Want to contribute? I'd love it.
Feel free to fork or reach out!
You can reach me at projectcarbon.io@gmail.com
<3
