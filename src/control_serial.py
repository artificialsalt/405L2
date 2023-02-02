'''!
@file control_serial.py
This file contains code to communicate motor position data with the MicroPython board and plot the resulting data.
This code should be run prior to running the MicroPython code.

@author Richard Kwan, Jackie Chen, Chayton Ritter
@date 31-Jan-2023
'''

import serial 
import array 
from matplotlib import pyplot

time_list = [] 
data_list = []

# Change test settings here
gain = 100 # 0.05

# Open serial port and communicate motor position with board
with serial.Serial('COM10', 115200) as s_port:
    # Write motor gain to board
    s_port.write(bytes(str(gain), encoding = 'utf-8'))

    # Read motor position data
    #print(s_port.readline ().split (b','))
    # Close port
    print('Closing port...')
'''
# Plot motor position
pyplot.plot(time_list, data_list)
pyplot.title(f'Motor step response with setpoint {ticks} and gain {gain}')
pyplot.xlabel('Time [ms]')
pyplot.ylabel('Encoder ticks')
pyplot.show()
'''