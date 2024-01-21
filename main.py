class Employee:
    def __init__(self, name , id):
        self.name=name
        self.id=id
    def showdetails(self):
            print(f"the name of employee: {self.name} is id {self.id}")
            
class program(Employee):
    def showlanguage(self):
        print("the defult language is pyhton")
        
e1=Employee("rohan",12)
e1.showdetails()
e2=program("rohan",122)
e2.showdetails()
e2.showlanguage()


class Person(object): 
      
    # Constructor 
    def __init__(self, name): 
        self.name = name 
  
    # To get name 
    def getName(self): 
        return self.name 
  
    # To check if this person is employee 
    def isEmployee(self): 
        return False
  
  
# Inherited or Sub class (Note Person in bracket) 
class Employee(Person): 
  
    # Here we return true 
    def isEmployee(self): 
        return True
  
# Driver code 
emp = Person("Geek1")  # An Object of Person 
print(emp.getName(), emp.isEmployee()) 
  
emp = Employee("Geek2") # An Object of Employee 
print(emp.getName(), emp.isEmployee()) 

# polymofishm

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()
