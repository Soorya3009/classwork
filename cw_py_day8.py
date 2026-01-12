# A company wants to create a simple system to define and display employee profiles based on their role types for record-keeping purposes. You are tasked with creating classes to represent different types of individuals in Python. Complete the following steps:

# Create a class Person with attributes name (string) and age (integer), and a method show_details() that prints the person’s name and age.
# Create a class Employee that inherits from Person, adds an attribute employee_id (string), and includes a show_details() method to print the employee’s name, age, and employee ID.
# Create a class PartTime that inherits from Person, adds an attribute working_hours (float), and includes a show_details() method to print the part-time worker’s name, age, and working hours.
# Create a class Consultant that inherits from both Employee and PartTime, adds an attribute project_name (string), and includes a show_details() method to print the consultant’s name, age, employee ID, working hours, and project name.
# Create one object of each class (Person, Employee, PartTime, Consultant) with sample data.
# Display the details of each object by calling its show_details() method



class Person:
    def _init_(self,name,age):
        self.name = name
        self.age = age
    def show_details(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

class Employee(Person):
    def _init_(self, name, age,employee_id):
        Person._init_(self,name, age)
        self.employee_id = employee_id
    def show_details(self):
        Person.show_details(self)
        print("Employee ID: ",self.employee_id)

class PartTime(Person):
    def _init_(self, name, age,working_hours):
        Person._init_(self,name, age)
        self.working_hours = working_hours
    def show_details(self):
        Person.show_details(self)
        print("Working Hours: ",self.working_hours)

class Consultant(Employee, PartTime):
    def _init_(self, name, age, employee_id, working_hours, project_name):
        Employee._init_(self,name,age,employee_id)
        PartTime._init_(self,name,age,working_hours)
        self.project_name = project_name
    def show_details(self):
        Employee.show_details(self)
        print("Working Hours: ",self.working_hours)
        print("Project_Name: ",self.project_name)

person1 = Person("Miya",22)
employee1 = Employee("Meenu",30,"EMP101")
parttime1 = PartTime("Liya",26,4.5)
consultant1 = Consultant("Amiya",28,"EMP202",5.0,"FULL STACK")

print("\n PERSON DETAILS")
person1.show_details()
print("\n EMPLOYEE DETAILS")
employee1.show_details()
print("\n PART TIME DETAILS")
parttime1.show_details()
print("\n CONSULTANT DETAILS")
consultant1.show_details()