
class Employee:
    def __init__(self, name, age, role, salary):
        self.name = name
        self.age = age
        self.role = role
        self.salary = salary

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

    
    
employee1 = Employee("Virat", 34, "Data Scientist", 1_000_000)

salary_input = int(input("Input Salary: "))
if salary_input < 60_000:
    raise ValueError('Minimum wage is Rs. 60,000')
else:
    employee1.salary = salary_input

# validation is done in application code. OOP: The logic has to be inside of the class
# employee1.salary = 10_000 can be accessed directly