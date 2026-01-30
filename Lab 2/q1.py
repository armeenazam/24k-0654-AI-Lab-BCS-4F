#Task 1
class Vehicle:
  def __init__ (self, vehicle_id, brand, rent_per_day):
    self.vehicle_id = vehicle_id
    self.brand = brand
    self.rent_per_day = rent_per_day

  def display_details(self):
    print(f"Vehicle id: {self.vehicle_id}")
    print(f"Brand: {self.brand}")
    print(f"Rent per Day: {self.rent_per_day}")  

  def calculate_rent(self, days):
    total_rent = self.rent_per_day * days
    print (f"Rent for {days} days: {total_rent}")


car = Vehicle(1357, "Toyota", 5000)
bike = Vehicle(2468, "Honda", 1500)

print("....Car Details....\n")
car.display_details()
car.calculate_rent(5)
car.calculate_rent(2)

print("\n....Bike Details....\n")
bike.display_details()
bike.calculate_rent(3)
bike.calculate_rent(6)
