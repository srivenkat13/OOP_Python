# The employee salary system problem

# creating the Employee class, with empolyee id, name, age, and gender attributes
class Employee:
    def __init__(self, name, id, age, gender):
        self.eid = id
        self.ename = name
        self.age = age
        self.gender = gender


# Organization class with Organization names and employee list
class Organization:
    def __init__(self, name, elist):
        self.oname = name
        self.elist = elist

    # Add employee method , which takes id, name, age and gender and appends them to elist, here these are passed to Employee class
    def addEmployee(self, name, id, age, gender):
        print("In addEmployee method")
        e = Employee(name, id, age, gender)
        self.elist.append(e)
        print("Exits addEmployee method")

    # view employee method which displays the employee's detials from the list
    def viewEmployees(self):
        print("In viewEmployees method")
        for e in self.elist:
            print(e.eid)
            print(e.ename)
            print(e.age)
            print(e.gender)
        print("Exits viewEmployees method")

    # this method which counts the lenght of the employee list and returns it
    def getEmployeeCount(self):
        print("In getEmployeeCount method")
        print("Exits getEmployeeCount method")
        return len(self.elist)

    # this method is to find the employee age when an id is given, from the  elist. It gives age if ID exists else  it would return -1, indicating that the ID passed is not in the elist
    def findEmployeeAge(self, id):
        print("In findEmployeeAge method")
        local_age = -1
        # this is a local variable not to be confused with the age in Employee class,
        for e in self.elist:
            if e.eid == id:
                local_age = e.age
                break  # if the condition is meet it would break out of the loop
        print("Exits findEmployeeAge method")
        return local_age

    # method to count the employees based on the age
    def countEmployees(self, age):
        count = 0
        print(" In countEmployees with age method")
        for e in self.elist:
            if e.age > age:
                count = count + 1
        print(" Exits countEmployees with age method")
        return count


# now the main function to pass values against few testcases.
if __name__ == "__main__":
    # creating an employeelist i.eOrganization("TCSL",employees)., elist
    employees = []
    # creating a variable for Organization  ,giving name and passing employees list to it
    o = Organization("TCSL", employees)
    # taking input for number of test cases to be given
    n = int(input())
    # taking inputs for the test cases
    for i in range(n):
        name = input()
        id = int(input())
        age = int(input())
        gender = input()
        # adding the above details  to the elist by calling addEmployee method
        o.addEmployee(name, id, age, gender)
    # to print the list use viewEmployees method
    o.viewEmployees()

    # display the employees count
    print(o.getEmployeeCount())

    # find employee with ID
    id = int(input())
    print(o.findEmployeeAge(id))

    # count the employees based on age
    age = int(input())
    print(o.countEmployees(age))