'''!
@file main.py
This file contains code that runs a step response test on a motor and transmits time and position data back via UART.
This file should be run before running the PC code (control_serial.py).

@author Richard Kwan, Jackie Chen, Chayton Ritter
@date 31-Jan-2023
'''

import encoder_reader
import motor_driver
import closedloopcontrol
import utime

def main():
    # Configure UART2 on board
    u2 = pyb.UART(2, baudrate=115200)
    
    # Wait for data to be sent to board
    while True:
        if u2.any():
            break

    # Read the gain
    gain = u2.read()
    gain = float(gain.decode('utf-8'))
    
    # Create instances of motor, encoder, and controller
    M1 = motor_driver.MotorDriver('A10', 'B4', 'B5', 3, 1, 2)
    E1 = encoder_reader.EncoderReader('C6', 'C7', 8, 1, 2)
    CL = closedloopcontrol.cl_loop(gain, 1000)
    M1.enable_motor()

    # Start timing step response
    start_time = utime.ticks_ms()

    while True:
        # Adjust motor power 
        a = CL.run(E1.read())
        M1.set_duty_cycle(a)
        time_diff = utime.ticks_diff(utime.ticks_ms(), start_time)
        
        # Terminate step response test after 3 seconds
        if time_diff > 3000:
            break
        utime.sleep_ms(10)

    # Turn off motor
    M1.set_duty_cycle(0)
    M1.disable_motor()

    # Get position data from controller class
    pos_data = CL.get_pos_data()
    pos_data_as_str = [str(i) for i in pos_data]    # Turns every list item into a string
    tx_buf = ','.join(pos_data_as_str)              # Turns the list into a really long string (a tx buffer)
    u2.write(tx_buf)                                # Writes the really long string into UART

if __name__ == '__main__':
    main()