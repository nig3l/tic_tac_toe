#practice concepts  

'''class person:

    def __init__(self,age,name,height): # parametarized constructor
        self.age = age
        self.name = name
        self.height = height
        
    def say_hi(self):
        print("i am ",self.name)
        print("i am " ,self.age,"years old")
        print("i am ",self.height," feet tall")

person1=person(12 , "bosco",5.6)
person1.say_hi()'''

#class v instance variables

'''class Dog:

    #class variable

    animal = 'mammal'

    #attr initialisation/constructor
    def __init__(self,breed,color):
        #instance variables
        self.breed = breed
        self.color = color

buzz = Dog('french terrier','black')
julio = Dog('bloodhound','brown')

print("TITLE : Buzz identification")
print("animal type :",buzz.animal)
print("breed :",buzz.breed)
print("furcoat color :",buzz.color)

print("\nTITLE : julio identification")
print("animal type :",julio.animal)
print("breed :",julio.breed)
print("furcoat color :",julio.color)

'''

#to demonstrate inheritance

'''

class Person(): #in python3 and above class person() is the same as class person(object)

  #constructor
    def __init__(self,name):
        self.name = name

#to get name 
    def getName(self):
        return self.name
    
#to check whether is an employee

    def isEmployee(self):
        return False
    
#Subclass 

class Employee(Person):

    #to check whether is an employee

    def isEmployee(self):
        return True
    
emp = Person("smoker")
print(emp.getName(),emp.isEmployee())

emp = Employee("akainu")
print(emp.getName(),emp.isEmployee())
'''

#calling constructors of the parent class

'''class Person(object):
    
    def __init__(self,name,idNumber):
        self.name = name
        self.idNumber = idNumber

    def display(self):
       print(self.name) 
       print(self.idNumber)
   
   #child class
     
class Employee(Person):

    def __init__(self,name,idNumber,salary,post):
        self.salary = salary
        self.post = post

        #invoking the parent class constructor
        Person.__init__(self,name,idNumber) #i believe the super() function can be used this way

a = Employee('Blackbeard',40042,'200k','product manager')
a.display()
       '''

#the super() function

'''class person():
    def __init__(self,name ,age):
        self.name = name
        self.age = age
        
    def display(self):
        print(self.name,self.age)
        

class student(person):
    def __init__(self, name, age):
        self.sName = name
        self.sAge = age

        #inheriting properties of the parent class
        super().__init__('Gorosei',79)

    def display_info(self):
        print(self.sName, self.sAge)

obj = student('usop',18)
obj.display()
obj.display_info()
'''

#adding more features

class Flour():

    def __init__(self,dom,exd):
        self.dom = dom
        self.exd = exd
        
    def display(self):
        print(self.dom,self.exd)

class flour1(Flour):

    def __init__(self, dom, exd,type):
        self.dom = dom
        self.exd = exd
        self.type = type

    super().__init__('18th feb','12th dec')

    

        

        


        

