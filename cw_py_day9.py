# You are tasked with building a Vehicle Rental Management System to help a car rental company manage different types of vehicles (Cars and Bikes) and calculate their rental charges for billing purposes. 
# Requirements:

# Create a base class Vehicle to store common vehicle details.
# Attributes (protected, not private):
#      _vehicle_id: A string representing the unique vehicle identifier (e.g., "CAR001", "BIKE001").
#      _base_rate: A float representing the base daily rental rate (e.g., 100.00).
# Include a constructor to initialize _vehicle_id and _base_rate.
# Provide a method display_details() to return a string with the vehicle ID and base rate.
# Include a method rental_charge() that returns a placeholder value (0.0) to be overridden by subclasses.x

# Create a subclass Car that inherits from Vehicle:
#      Add an attribute num_seats (integer, e.g., 4 for a sedan).
#      Override the rental_charge() method to calculate the daily rental charge as _base_rate * num_seats.
# Create a subclass Bike that inherits from Vehicle:
#      Add an attribute bike_type (string, e.g., "Scooter", "Motorcycle").
#      Override the rental_charge() method to calculate the daily rental charge as _base_rate * 0.5.

# Write a function calculate_rental that accepts a Vehicle object and calls its rental_charge() method to return the rental charge. This demonstrates polymorphism by working with any vehicle type.





class vehicle:
    def _init_(self,vehicle_id,base_rate):
        self.vehicle_id = vehicle_id
        self.base_rate = base_rate
    def display_details(self):
        return f"Vehicle ID: {self.vehicle_id}, Base Rate: {self.base_rate}"
    def rental_charge(self):
        return 0.0        

class car(vehicle):
    def _init_(self, vehicle_id, base_rate,num_seats):
        super()._init_(vehicle_id, base_rate)
        self.num_seats = num_seats
    def rental_charge(self):
        return self.base_rate * self.num_seats
    
class bike(vehicle):
    def _init_(self, vehicle_id, base_rate,bike_type):
        super()._init_(vehicle_id, base_rate)
        self.bike_type = bike_type
    def rental_charge(self):
        return self.base_rate * 0.5
def calculate_rental(vehicle):
    return vehicle.rental_charge()
car1 = car("CAR001",100.0,4)
bike1 = bike("BIKE001",50.0,"SCOOTER")
print(car1.display_details())
print(bike1.display_details1())
print("Car rental charge: ",calculate_rental(car1))
print("Bike rental charge: ",calculate_rental(bike1))