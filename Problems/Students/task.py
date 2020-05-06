class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.id = self.name[0] + self.last_name + self.birth_year

name = input()
surname = input()
year = input()

stu = Student(name, surname, year)
print(stu.id)