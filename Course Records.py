class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self.name = name
        self.grade = grade
        self.credits = credits


class MainApp:
    def __init__(self):
        self.courses = {}

    def add_course(self):
        name = input('course: ')
        grade = int(input('grade: '))
        credits = int(input('credits: '))
        if name not in self.courses:
            self.courses[name] = Course(name, grade, credits)
        if grade > self.courses[name].grade:
            self.courses[name].grade = grade
        if credits > self.courses[name].credits:
            self.courses[name].credits = credits

    def get_data(self):
        course = input('course: ')
        if course not in self.courses:
            print('no entry for this course')
            return
        print(f'{self.courses[course].name} ({self.courses[course].credits} cr) grade {self.courses[course].grade}')

    def statistics(self):
        total_courses = len(self.courses)
        total_credits = 0
        total_grade = 0
        grades = []
        for item in self.courses:
            total_credits += self.courses[item].credits
            total_grade += self.courses[item].grade
            grades.append(self.courses[item].grade)
        if len(self.courses) > 0:
            mean = total_grade / len(self.courses)
        else:
            mean = 0
        print(f'{total_courses} completed courses, a total of {total_credits} credits')
        print(f'mean {round(mean, 1)}')
        print('grade distribution')
        for i in range(5, 0, -1):
            count = grades.count(i)
            print(f'{i}: {"x" * count}')

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_data()
            elif command == "3":
                self.statistics()
            else:
                self.help()


application = MainApp()
application.execute()
