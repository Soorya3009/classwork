# You are building a basic user account system. Every user has a name and a year they joined. Your task is to:
# Create a general User class that cannot be used directly to make objects, but stores name and joining year.
# Add a method to calculate how many years the user has been on the platform (assume current year is 2025).
# Add two types of users: Customer and Vendor, each showing their specific role when asked.
# Use a special print message for each user that shows their name, role, and how many years they’ve been using the platform.



from abc import ABC, abstractmethod
class User(ABC):
    def _init_(self,name,join_year):
        self.name = name
        self.join_year = join_year
    def calculate_year(self):
        current_year = 2025
        return current_year - self.join_year
  
    @abstractmethod
    def display(self):
        pass

class Customer(User):
    def _init_(self, name, joined_year):
        super()._init_(name, joined_year)
        self.role = "Customer"

    def display(self):
        print("Name: ",self.name)
        print("Role: ",self.role)
        print("Years on Platform: ",self.calculate_year())


class Vendor(User):
    def _init_(self, name, joined_year):
        super()._init_(name, joined_year)
        self.role = "Vendor"

    def display(self):
        print("Name: ", self.name)
        print("Role: ", self.role)
        print("Years on Platform: ",self.calculate_year())
customer = Customer("Miya", 2020)
vendor = Vendor("Kiran", 2018)
print("Customer")
customer.display()
print("Vendor")
vendor.display()