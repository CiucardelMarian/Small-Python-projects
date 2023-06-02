class NumberStats:
    def __init__(self):
        self.numbers = []
        self.even = []
        self.odd = []
        self.count = 0

    def add_number(self, number: int):
        self.count += 1
        self.numbers.append(number)

    def count_numbers(self):
        return self.count

    def get_sum(self):
        if len(self.numbers) == 0:
            return 0
        else:
            suma = sum(self.numbers)
            return suma

    def average(self):
        if len(self.numbers) == 0:
            return 0
        else:
            avg = sum(self.numbers) / len(self.numbers)
            return avg


stats = NumberStats()
statsodd = NumberStats()
statseven = NumberStats()
while True:
    print('Please type in integer numbers:')
    n = int(input())
    if n == -1:
        print(f'Sum of numbers: {stats.get_sum()}')
        print(f'Mean of numbers: {stats.average()}')
        print(f'Sum of even numbers: {statseven.get_sum()}')
        print(f'Sum of odd numbers: {statsodd.get_sum()}')
        break

    stats.add_number(n)
    if n % 2 == 0:
        statseven.add_number(n)
    else:
        statsodd.add_number(n)
