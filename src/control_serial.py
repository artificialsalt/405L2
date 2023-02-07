'''!
@file control_serial.py
This file contains code to communicate motor position data with the MicroPython board and plot the resulting data.
This code should be run AFTER running the MicroPython code.

@author Richard Kwan, Jackie Chen, Chayton Ritter
@date 31-Jan-2023
'''

import serial 
from matplotlib import pyplot

# Change test settings here
gain = 0.02

# Open serial port and communicate motor position with board
with serial.Serial('COM10', 115200, timeout=5) as s_port:
    # Write motor gain to board
    print(f'Commanding step response test with gain {gain}')
    s_port.write(bytes(str(gain), encoding = 'utf-8'))

    print('Test in progress, waiting for data...')
    
    # Read motor position data
    raw_data = s_port.readlines()

    # Close port
    print('Data received, closing port...')

# Create a list of values from the incoming string of data
list_of_vals = raw_data[0].decode('utf-8').split(',')

time_list = []
data_list = []

# Separate time and position values
for i in range(len(list_of_vals)):
    if i % 2 == 0:
        time_list.append(int(list_of_vals[i]))
    else:
        data_list.append(int(list_of_vals[i]))

# Plot motor position
pyplot.plot(time_list, data_list)
pyplot.title(f'Motor step response with gain {gain}')
pyplot.xlabel('Time [ms]')
pyplot.ylabel('Encoder ticks')
pyplot.show()