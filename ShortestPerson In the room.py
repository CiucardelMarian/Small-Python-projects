class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name


class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        if len(self.persons) == 0:
            return True
        return False

    def print_contents(self):
        for item in self.persons:
            print(f'{item.name} ({item.height} cm)')

    def shortest(self):
        if self.is_empty():
            return None
        shortest = self.persons[0]
        for item in self.persons:
            if item.height < shortest.height:
                shortest = item
        return shortest

    def remove_shortest(self):
        person_to_remove = self.shortest()
        if not self.is_empty():
            self.persons.remove(person_to_remove)
        return person_to_remove


room = Room()
room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.add(Person("Nina", 162))
room.add(Person("Ally", 166))
room.print_contents()
print()
removed = room.remove_shortest()
print(f"Removed from room: {removed.name}")
print()
room.print_contents()
