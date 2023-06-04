# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
'''class Vehicle:

    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelx = Vehicle(200,12)
print(modelx.max_speed,modelx.mileage)

 '''

# Create a Vehicle class without any variables and methods
'''class Vehicle:
    pass
'''

# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
'''class Vehicle:
    def __init__(self,name,maxspeed,mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

'''


# Create a Bus class that inherits from the Vehicle class. 
# Give the capacity argument of Bus.seating_capacity() a default value of 50.
# Expected output: The seating capacity of a bus is 50 passengers


'''class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    # assign default value to capacity
    def seating_capacity(self,capacity = 50):
        return super().seating_capacity(capacity)

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())


'''

# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
# Expected Output:

# Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
# Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18


'''class Vehicle:

    color = "white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_volvo = Bus("School_volvo",180,12)
print(School_volvo.color,School_volvo.name,School_volvo.max_speed,School_volvo.mileage)

Audi_Q5 = Car("Audi_Q5",240,18)
print(Audi_Q5.color,Audi_Q5.name,Audi_Q5.max_speed,Audi_Q5.mileage)

 '''
     
# Create a Bus child class that inherits from the Vehicle class.
#  The default fare charge of any vehicle is seating capacity * 100. 
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. 
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

# Note: The bus seating capacity is 50. so the final fare amount should be 5500. 
# You need to override the fare() method of a Vehicle class in Bus class.

# Expected Output:

# Total Bus fare is: 5500.0

'''class Vehicle:
    def __init__(self,name,mileage,capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100
    
class Bus(Vehicle):

    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount


        
    

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())

'''

#  Check type of an object
# Write a program to determine which class a given Bus object belongs to.


'''class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

print(type(School_bus))

'''
# Determine if School_bus is also an instance of the Vehicle class

'''class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print(isinstance(School_bus, Vehicle))

'''

# Create a class called Employee with attributes name, salary, and department.
#  Implement a method called apply_raise that increases the salary of the employee by a certain percentage. 
# Also, implement a method called display that prints the employee's name, salary, and department.

'''class Employee:
    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department

    def apply_raise(self,amountp):
        self.salary += amountp * (amountp/100)    # the '+=' operator is meant to increase the self.salary attribute by the value of amountp
    
    def display(self):
        print(self.name,self.salary,self.department)

    '''

# Create a class called Car with attributes make, model, and year. 
# Implement a method called start_engine that prints a message indicating that the car's engine has started.
# Also, implement a method called drive that takes a distance as an argument and prints a message indicating the distance driven.

'''class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("the car has started")

    def drive(self,distance):
        self.distance = distance
        print("Distance covered is : ", distance)
'''




        
