import encoder_reader
import motor_driver
import closedloopcontrol
import utime

def main():
    while True:
        M1 = motor_driver.MotorDriver('A10', 'B4', 'B5', 3, 1, 2)
        E1 = encoder_reader.EncoderReader('C6', 'C7', 8, 1, 2)
        CL = closedloopcontrol.cl_loop(0.05, 50000)
        M1.enable_motor()

        user_gain = float(input('Please work: '))
        CL.set_kp(user_gain)
    
        while True:
            a = CL.run(E1.read())
            if a < 13:
                break
            M1.set_duty_cycle(a)
            utime.sleep_ms(10)

        M1.set_duty_cycle(0)
        M1.disable_motor()
        CL.printout()



if __name__ == '__main__':
    main()