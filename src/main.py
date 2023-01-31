import encoder_reader
import motor_driver
import closedloopcontrol

def main():
    M1 = motor_driver.MotorDriver('A10', 'B4', 'B5', 3, 1, 2)
    E1 = encoder_reader.EncoderReader('C6', 'C7', 8, 1, 2)
    CL = closedloopcontrol.cl_loop(0.01, 10000)
    M1.enable_motor()

    while True:
        a = CL.run(E1.read())
        M1.set_duty_cycle(a)
        utime.sleep_ms(10)





if __name__ == '__main__':
    main()