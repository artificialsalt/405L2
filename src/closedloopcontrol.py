import utime

class cl_loop:
    def __init__(self, gain, setpoint):
        self.gain = gain
        self.setpoint = setpoint
        self.print = []

    def run(self, output):
        pwm = self.gain*(self.setpoint - output)
        time = utime.ticks_ms()
        self.print.append([time, output])
        return pwm

    def set_setpoint(self, setpoint):
        self.setpoint = setpoint

    def set_kp(self, gain):
        self.gain = gain

    def printout(self):
        for point in self.print:
            print(point)