
class Employee:
    def __init__(self, name, age, role, salary):
        self.name = name
        self.age = age
        self.role = role
        self.salary = salary

    def increase_salary(self, hike):
        self.salary += (self.salary * hike/100)

    
    
a = Employee("Virat", 34, "Data Scientist", 1_000_000)


# __new__
