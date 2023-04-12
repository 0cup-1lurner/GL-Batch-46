
class Employee:
    def __init__(self, name, age, role, salary):
        self.__dict__['name'] = name
        self.__dict__['age'] = age
        self.__dict__['role'] = role
        self.__dict__['salary'] = salary
    
a = Employee("Virat", 34, "Data Scientist", 1_000_000)


