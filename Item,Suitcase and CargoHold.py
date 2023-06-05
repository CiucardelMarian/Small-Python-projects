class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

    def weight(self):
        return self.__weight

    def name(self):
        return self.__name


class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__items = []

    def weight(self):
        p = 0
        for item in self.__items:
            p += item.weight()
        return p

    def __str__(self):
        # Use the one-line condition introduced at the end of part 7
        end_s = "s" if len(self.__items) != 1 else ""

        return f"{len(self.__items)} item{end_s} ({self.weight()} kg)"

    def add_item(self, item):
        if self.weight() + item.weight() > self.__max_weight:
            return

        self.__items.append(item)

    def print_items(self):
        for item in self.__items:
            print(item)

    def heaviest_item(self):
        heaviest = self.__items[0]
        for item in self.__items:
            if item.weight() > heaviest.weight():
                heaviest = item
        return heaviest


class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__suitcases = []

    def __str__(self):
        word = "suitcases"
        if len(self.__suitcases) == 1:
            word = "suitcase"

        return f"{len(self.__suitcases)} {word}, space for {self.__max_weight - self.weight()} kg"

    def weight(self):
        p = 0
        for suitcase in self.__suitcases:
            p += suitcase.weight()
        return p

    def add_suitcase(self, suitcase):
        if self.weight() + suitcase.weight() > self.__max_weight:
            return
        self.__suitcases.append(suitcase)

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()


book = Item("ABC Book", 2)
phone = Item("Nokia 3210", 1)
brick = Item("Brick", 4)

adas_suitcase = Suitcase(10)
adas_suitcase.add_item(book)
adas_suitcase.add_item(phone)

peters_suitcase = Suitcase(10)
peters_suitcase.add_item(brick)

cargo_hold = CargoHold(1000)
cargo_hold.add_suitcase(adas_suitcase)
cargo_hold.add_suitcase(peters_suitcase)

print("The suitcases in the cargo hold contain the following items:")
cargo_hold.print_items()
