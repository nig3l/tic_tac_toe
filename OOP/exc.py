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

# Create a base class called Shape with a method calculate_area() that returns 0. 
# Create a derived class called Rectangle that inherits from Shape and overrides 
# the calculate_area() method to calculate 
# and return the area of a rectangle given its width and height


'''class Shape:

    def calculate_area(self):
        return 0
    
class Rectangle(Shape):
     
     def __init__(self, width, height):
        self.width = width
        self.height = height

     def calculate_area(self):
        return self.height * self.width
        
   '''
# Create a base class called Animal with a method make_sound() that prints "Animal sound". 
# Create a derived class called Dog that inherits from Animal 
# and overrides the make_sound() method to print "Bark".

'''class Animal():

    def make_sound(self):
        print("animal sound")

class Dog(Animal):
    def make_sound(self):
        print("bark")
    
'''

# Create a base class called Vehicle with attributes make and model, 
# and a method display_info() that prints the make and model of the vehicle. 
# Create a derived class called Car that inherits from Vehicle and
# adds an additional attribute year and a method start_engine() that prints "Engine started".

'''class Vehicle():
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def display_info(self):
        print(self.make, self.model)

class car(Vehicle):
    def __init__(self, make, model,year):
        super().__init__(make, model) # you have to call the parents' innit method
        self.year = year

    def start_engine(self):
        print("engine started")

'''

# Create a base class called Employee with attributes name and salary, and a method display_info() that prints the name and salary of the employee. 
# Create a derived class called Manager that inherits from Employee 
# and adds an additional attribute department and 
# a method display_department() that prints the department of the manager.

'''class Employee():
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(self.name, self.salary)

class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department

    def display_department(self):
        print(self.department)

'''
# Create a base class called Shape with attributes color and filled, 
# and a method display_info() that prints the color and filled status of the shape. 
# Create a derived class called Circle that inherits from Shape 
# and adds an additional attribute radius and a method calculate_area() 
# that calculates and returns the area of the circle.

'''import math
class Shape():
    def __init__(self,color,filled):
        self.color = color 
        self.filled = filled

    def display_info(self):
        print(self.color,self.filled)

class Circle(Shape):
    def __init__(self, color, filled,radius):
        super().__init__(color, filled)
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    '''   

#for loop to print numbers 1-10

'''
for i in range(1,11):
    print(i)
 '''

# Calculate the sum of all numbers from 1 to 100.  

'''
sum = 0
for num in range(1,101):
    sum += num
    print(sum)
'''

# Inheritance:
# Create a base class called Shape with a method area() that calculates and returns the area of the shape. 
# Create a derived class Rectangle that inherits from Shape and has additional attributes length and width. 
# Implement the area() method in the Rectangle class to calculate and return the area of the rectangle.

'''class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

rectangle = Rectangle(5, 3)
print(rectangle.area())
     '''


# Polymorphism:
# Create a base class called Animal with a method speak() that prints a generic sound. 
# Create derived classes Dog and Cat that inherit from Animal and override the speak() method to print the specific sound of each animal. 
# Create instances of Dog and Cat and call their speak() methods.

'''class Animal:
    def speak(self):
        print("chirp!!!!!")

class Dog(Animal):
    def speak(self):
        print("woof!")

class Cat(Animal):
     def speak(self):
         print("meow!!!")

I1 = Dog()
I2 = Cat()

I1.speak()
I2.speak()

'''

# Composition:
# Create a class called Author with attributes name and books, where books is a list of book titles written by the author.
# Create another class called Library with an attribute authors, which is a list of Author objects. 
# Implement a method display_books() in the Library class that displays all the book titles and their respective authors.

'''class Author:
    def __init__(self,name,books):
        self.name = name
        self.books = books

        # books = []
       

class Library:
    def __init__(self,authors):
        self.authors = []

    def add_author(self, author):
        self.authors.append(author)



    def display_books(self):
            for author in self.authors:
               print(f"{author.name}:")

            for book in author.books:
                print(book)

                return Author
'''

"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!

class Classy(object):
    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def getClassiness(self):
        classiness = 0
        classiness_points = {
            "tophat": 2,
            "bowtie": 4,
            "monocle": 5
        }
        for item in self.items:
            classiness += classiness_points.get(item, 0)
        return classiness

# Test cases
me = Classy()

# Should be 0
print(me.getClassiness())

me.addItem("tophat")
# Should be 2
print(me.getClassiness())

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print(me.getClassiness())

me.addItem("bowtie")
# Should be 15
print(me.getClassiness())

"""

# Write a function called "show_excitement" where the string
# "I am super excited for this course!" is returned exactly
# 5 times, where each sentence is separated by a single space.
# Return the string with "return".
# You can only have the string once in your code.
# Don't just copy/paste it 5 times into a single variable!


# def show_excitement():
#     return "I am super excited for this course! " * 5

# print(show_excitement())
'''
def show_excitement():
    return " ".join(["I am super excited for this course!"] * 5)

print(show_excitement())

'''

# implementing a data structure using linked lists
# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

# class Stack:
#     def __init__(self):
#         self.head = None

#     def is_empty(self):
#         return self.head is None

#     def push(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def pop(self):
#         if self.is_empty():
#             raise Exception("Stack is empty")
#         popped_value = self.head.data
#         self.head = self.head.next
#         return popped_value
    
# Write a Python program to create a class representing a Circle. 
# Include methods to calculate its area and perimeter. 

'''import math
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2
    
    def get_perimeter(self):
        return 2 * math.pi * self.radius
    
# create an instance of the class 

circle = Circle(9)

area = circle.get_area()
perimeter = circle.get_perimeter()

print("Area of the circle:", area)
print("Perimeter of the circle:", perimeter)

'''


#  Write a Python program to create a person class. 
# Include attributes like name, country and date of birth. 
# Implement a method to determine the person's age. 

'''
from datetime import date
class person:
    def __init__(self,name,country,dob):
        self.name = name
        self.country = country
        self.dob= dob

    def get_age(self):

        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age -= 1

        return age
        
 '''       

#  Write a Python program to create a calculator class. 
#  Include methods for basic arithmetic operations.

'''
class Calc:

    def add(self ,x,y):
        return x + y
    
    def subtract(self,x,y):
        return x - y
    
    def multiply(self,x,y):
        return x * y
    
    def divide(self,x,y):

        if y != 0:
            return x / y
        else:
            return ("Cannot divide by zero.")


'''

# Write a Python program to create a class that represents a shape. 
# Include methods to calculate its area and perimeter. 
# Implement subclasses for different shapes like circle, triangle, and square.


import math

class Shape:

    def calc_area():
        pass
    def calc_perimeter():
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def calc_area(self,radius):

        return math.pi* radius ** 2
    
    def calc_perimeter(self,radius):

        return math.pi * (radius+radius)
    
class Triangle(Shape):
    def __init__(self,base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3


class Rectangle(Shape):
    
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
        
    


    
        
    
   
    



        


