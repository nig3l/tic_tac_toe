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

class Person(object):

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


        

