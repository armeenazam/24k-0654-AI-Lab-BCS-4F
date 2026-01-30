#Task 2
class Employee:
  def __init__(self, name, emp_id):
    self.name = name;
    self.emp_id = emp_id

  def calculate_salary(self):
    return 0  

  def display(self):
    print(f"Name: {self.name}")  
    print(f"Employee id: {self.emp_id}")

class FullTimeEmployee(Employee):
  def __init__(self, name, emp_id, monthly_salary):
    super().__init__(name, emp_id)    
    self.monthly_salary = monthly_salary

  def calculate_salary(self):
    return self.monthly_salary

  def display(self):
    super().display()

class PartTimeEmployee(Employee):
  def __init__(self, name, emp_id, hours_worked, hourly_rate):
    super().__init__(name, emp_id)
    self.hours_worked = hours_worked
    self.hourly_rate = hourly_rate

  def calculate_salary(self):
    return self.hourly_rate * self.hours_worked

  def display(self):
    super().display()  

emp1 = FullTimeEmployee("Armeen", 654, 75000)
emp2 = PartTimeEmployee("Ali", 980, 100, 300)

emp1.display()
print(f"Full Time Employee's Salary: {emp1.calculate_salary()}\n")
emp2.display()
print(f"Part Time Employee's Salary: {emp2.calculate_salary()}")
