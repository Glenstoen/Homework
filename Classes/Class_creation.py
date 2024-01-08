class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    def __str__(self):
        return f"{self.name},{self.age}"

    def count_population(self):
        return Person.count


p1 = Person("Glen", 33)
print(p1.count_population())
# print(p1)
