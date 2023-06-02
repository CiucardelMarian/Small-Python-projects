class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def __str__(self):
        return f"{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}"

    def tick(self):
        if self.seconds < 59:
            self.seconds += 1
        else:
            if self.minutes < 59:
                self.minutes += 1
            else:
                self.minutes = 0
            self.seconds = 0


watch = Stopwatch()
for i in range(3601):
    print(watch)
    watch.tick()
