import encoder_reader
import motor_driver
import closedloopcontrol
import utime

def main():
    u2 = pyb.UART(2, baudrate=115200, timeout = 5000)
    
    gain = u2.read()
    gain = int(gain.decode('utf-8'))
    gain = gain/1000
    
    M1 = motor_driver.MotorDriver('A10', 'B4', 'B5', 3, 1, 2)
    E1 = encoder_reader.EncoderReader('C6', 'C7', 8, 1, 2)
    CL = closedloopcontrol.cl_loop(gain, 1000)
    M1.enable_motor()

    # Start timing step response
    start_time = utime.ticks_ms()

    while True:
        a = CL.run(E1.read())
        M1.set_duty_cycle(a)
        time_diff = utime.ticks_diff(utime.ticks_ms(), start_time)
        print(time_diff)
        
        # Terminate step response test after 3 seconds
        if time_diff > 3000:
            break
        utime.sleep_ms(10)

    M1.set_duty_cycle(0)
    M1.disable_motor()
    CL.printout()


if __name__ == '__main__':
    main()