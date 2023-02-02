import utime

class cl_loop:
    def __init__(self, gain, setpoint):
        self.gain = gain
        self.setpoint = setpoint
        self.pos_data = []
        self.prev_time = utime.ticks_ms()
        self.time = 0

    def run(self, output):
        pwm = self.gain*(self.setpoint - output)
        interval = utime.ticks_diff(utime.ticks_ms(), self.prev_time)
        self.time += interval
        self.prev_time = utime.ticks_ms()
        self.pos_data.append(self.time)
        self.pos_data.append(output)
        return pwm

    def set_setpoint(self, setpoint):
        self.setpoint = setpoint

    def set_kp(self, gain):
        self.gain = gain

    def get_pos_data(self):
        return self.pos_data