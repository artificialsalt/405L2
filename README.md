# 405L2 - Motor Proportional Control
## Description

This repository contains code that allows for proportional control of a motor. It also includes the necessary motor and encoder classes required for running the controller class.

The approach used in the included code is measuring the difference in motor position (in encoder ticks) between the current position and a given setpoint. The difference is then multiplied by a gain coefficient, which is then translated directly into a PWM value into the motor driver class. PWM percentages of greater than 100 are reduced to a maximum value of 100 by the motor driver class.

This repository also includes code intended for use on a computer that allows a user to run step response tests. The code running on the computer will prompt the user to input a gain value. Once a valid value is given, it will communicate the value via UART to the MicroPython board, which will then run the step response test at the given gain value. The step response test is configured such that the 3d printed disc attached to the motor makes one complete revolution (approximately 1000 ticks). During the step response test, the MicroPython board collects time and position data. At the end of 3 seconds, the test stops and the MicroPython communicates the data back to the computer. The computer then parses the data and plots it to visualize the motor response.

## Usage

Run the MicroPython code (main.py) first, then run the PC code (code_serial.py). The PC code may need to be modified depending on the COM port being used by the computer to communicate with the ST-LINK USB port. By default, it is on COM10. **Ensure that the REPL on UART2 is disabled in boot.py in the MicroPython flash.**

## Example results

(picture here)

Underdamped response

(picture here)

Excessive oscillation

(picture)

Good response
