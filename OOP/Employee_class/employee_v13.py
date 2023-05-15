# getter and setter here are just adding new layers. 
# self.salary should not be allowed to access outside class.Use `_` before the attribute name
# Exlusive internal use: self.age incremented every year

class Employee:
    def __init__(self, name, age, role, salary):
        self.name = name
        self.age = age
        self.role = role
        self.set_salary(salary)

    def increase_salary(self, hike):
        self.salary += (self.salary * hike/100)

    def __str__(self):
        return f"{self.name} is {self.age} years old. Employee is a {self.role} with \
the salary of Rs.{self.salary}"

    def __repr__(self):
        return (
            f"Employee("
            f"{repr(self.name)}, {repr(self.age)},"
            f"{repr(self.role)}, {repr(self.salary)})"
        )
    
    def get_salary(self):
        return self._salary
    
    def set_salary(self, salary):
        if salary < 60_000:
            raise ValueError('Minimum wage is Rs. 60,000')
        self._salary = salary
    
    
employee1 = Employee("Virat", 34, "Data Scientist", 1_000_000)

#employee1.set_salary(10000)
#print(employee1.get_salary())
# 
employee1.set_salary(60000)
print(employee1.get_salary())

