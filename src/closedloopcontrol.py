class cl_loop:
    def __init__(self, gain, setpoint):
        self.gain = gain
        self.setpoint = setpoint

    def run(self, output):
        pwm = self.gain*(self.setpoint - output)
        return pwm

    def set_setpoint(self, setpoint):
        self.setpoint = setpoint

    def gain(self, gain):
        self.gain = gain
