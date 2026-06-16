# For protected members (Single underscore _)
'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
    
    def display(self):
        print(f"Salary: {self._salary}")
    
emp = Employee("Rahul", 50000)
print(emp._salary)
emp._salary = 60000
'''

# For Private Members (Double Underscore __)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            raise ValueError("Salary must be positive")
        
emp = Employee("Rahul", 50000)

# print(emp._Employee__salary)

print(emp.get_salary())
emp.set_salary(60000)
print(emp.get_salary())
