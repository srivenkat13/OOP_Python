#  If its Aggregation that means they are working together,but if one class is removed other still continues. Aggregation  and composition is the subset of association
# aggregation is a unidirectional realtion , so they can survive individually


class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annualSalary(self):
        return (self.pay * 12) + self.bonus


# Employee class is the container of Salary class
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.obj_salary = salary

    def totalSalary(self):
        return self.obj_salary.annualSalary()

my_salary=Salary(15000,10000)
# here the salary object is created 
emp=Employee("Venkat",23,my_salary)
# also the employee object is created
#both  classes can create thier own objects also
print(emp.totalSalary())