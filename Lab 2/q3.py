#Task 3
class Student:
  def __init__(self, name):
   self.name = name
   self.__marks = 0

  def set_marks(self, marks):
    if 0 <=  marks <=100:
      self.__marks = marks
    else:
      print("Invalid marks")  

  def get_marks(self):
    return self.__marks

  def calculate_grade(self):
    if self.__marks >= 90:
      return "A+"
    elif self.__marks >= 80:
      return "A"
    elif self.__marks >= 70:
      return "B"
    elif self.__marks >= 60:
      return "C"
    elif self.__marks >= 50:
      return "D"
    else:
      return "F"

  def display(self):
    print(f"Name: {self.name}")
    print(f"Marks: {self.get_marks()}")
    print(f"Grade: {self.calculate_grade()}\n")    

student1 = Student("Armeen")
student2 = Student("Ali")

student1.set_marks(59)
student2.set_marks(72)

student1.display()
student2.display()
  
