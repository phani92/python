# Example to create classes and use decorators

class Employee:
    salary = 100000
    increment = 1

    @property
    def salAfterInc(self):
        return self.salary * self.increment

    @salAfterInc.setter
    def salAfterInc(self, sai):
        self.increment = sai / self.salary

    @salAfterInc.setter
    def salAfterInc(self, sai):
        self.salary = sai

    def showInc(self):
        print(f"The salary of the employee is {self.salary}")




phani = Employee()
phani.showInc()
phani.salAfterInc = 150000
phani.showInc()

