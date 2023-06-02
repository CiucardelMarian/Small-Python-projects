class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}"

    def tick(self):
        if self.seconds < 59:
            self.seconds += 1
        else:
            if self.minutes < 59:
                self.minutes += 1
            else:
                if self.hours < 23:
                    self.hours += 1
                else:
                    self.hours = 0
                self.minutes = 0
            self.seconds = 0

    def set(self, h: int, m: int):
        self.hours = h
        self.minutes = m
        self.seconds = 0


clock = Clock(23, 59, 55)
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.set(12, 5)
print(clock)
