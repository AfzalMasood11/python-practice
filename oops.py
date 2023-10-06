class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        print("$", self.salary)


afzal = Employee('Afzal', '300k')
afzal.getSalary()