import time

class Timer:
    def __init__(self) -> None:
        self.t = 0
        pass

    def start(self):
        self.t = time.process_time_ns()

    def printStop(self):
        elapsed = (time.process_time_ns() - self.t)/1000000.0
        print("Timer ", elapsed, "ms")
        return elapsed