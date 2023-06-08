class Money:
    def __init__(self, _euros: int, _cents: int):
        self._euros = _euros
        self._cents = _cents

    def __str__(self):
        return f"{self._euros}.{str(self._cents).zfill(2)} eur"

    def __eq__(self, another):
        return self._euros == another._euros and self._cents == another._cents

    def __lt__(self, another):
        euro1 = self._euros + self._cents / 100
        euro2 = another._euros + another._cents / 100
        return euro1 < euro2

    def __gt__(self, another):
        euro1 = self._euros + self._cents / 100
        euro2 = another._euros + another._cents / 100
        return euro1 > euro2

    def __ne__(self, another):
        euro1 = self._euros + self._cents / 100
        euro2 = another._euros + another._cents / 100
        return euro1 != euro2

    def __add__(self, another):
        euros = self._euros + another._euros
        cents = self._cents + another._cents
        if cents > 99:
            cents = cents % 100
            euros += 1
        return f"{euros}.{str(cents).zfill(2)} eur"

    def __sub__(self, another):
        euros = self._euros - another._euros
        cents = self._cents - another._cents
        if cents < 0:
            cents = self._cents + 100 - another._cents
            euros -= 1
        if euros < 0:
            raise ValueError("a negative result is not allowed")
        return f"{euros}.{str(cents).zfill(2)} eur"


e1 = Money(4, 5)
e2 = Money(2, 95)

e3 = e1 + e2
e4 = e1 - e2

print(e3)
print(e4)

e5 = e2 - e1
