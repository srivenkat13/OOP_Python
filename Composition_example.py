# Composition is the resturctured form of aggregation  in which two classes are highly interdependent. 
# when there is composition between two classes the composed object cannot exist without another class.

class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annualSalary(self):
        return (self.pay * 12) + self.bonus


# Employee class is the container of Salary class
class Employee:
    def __init__(self, name, age, pay,bonus):
        self.name = name
        self.age = age
        self.obj_salary = Salary(pay,bonus )

    def totalSalary(self):
        return self.obj_salary.annualSalary()

emp=Employee("Venkat",21,15000,10000)

print(emp.totalSalary())

# here if the Employee object is not created then the Salary Object is not created.

# existence of salary object is not possible if the Employee object is not created
