from Class_creation import Person
import random


class student(Person):
    def __init__(self, name, age):
        super.__init__(self, name, age)
        self.grades = []
        self.avg_grades = 0

    def __str__(self):
        return f"{self.name} has an average grade of {self.avg_grades}"

    def get_grades(self):
        self.grades = [4, 5, 6, 4, 3, 3]
        return self.grades

    def calc_avg_grades(self):
        self.avg_grades = round(sum(self.grades) / len(self.grades), 2)
        return self.avg_grades


p1 = student("Glen", 33)
p1.get_grades()
p1.calc_avg_grades()
print(p1)
