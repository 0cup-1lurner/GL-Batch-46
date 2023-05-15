# increase_salary still uses the .salary attribute
# add setter functionality

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

    # b/w compatible
    # the property decorator will turn the regular salary method into property
    # read-only
    @property
    def salary(self):
        return self._salary

    # Name of func has to match(salary) the name of attribute (salary)
    # Decorator: <Name of func decorated by property>.setter  
    @salary.setter
    def salary(self, salary):
        if salary < 60_000:
            raise ValueError('Minimum wage is Rs. 60,000')
        self._salary = salary
    
    
employee1 = Employee("Virat", 34, "Data Scientist", 1_000_000)

#employee1.set_salary(10000)
#print(employee1.get_salary())

 
employee1.salary = 60000
#print(employee1.get_salary())
print(employee1.salary)


