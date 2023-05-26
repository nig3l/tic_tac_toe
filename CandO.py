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

'''class Flour():

    def __init__(self,dom,exd):
        self.dom = dom
        self.exd = exd
        
    def display(self):
        print(self.dom,self.exd)

class flour1(Flour):

    def __init__(self, dom, exd,type):
        self.f1_dom = dom
        self.f1_exd = exd
        self.type = type

        super().__init__("JUNE-2023","AUG-2024")

    def display_Info(self):
        print(self.f1_dom,self.f1_exd,self.type)

obj = flour1('12th jan','13th june','Maize flour')
obj.display()
obj.display_Info()
'''
# multiple inheritance

# Python example to show the working of multiple
# inheritance

'''class Base1(object):
	def __init__(self):
		self.str1 = "paramesia"
		print("high diff")


class Base2(object):
	def __init__(self):
		self.str2 = "zoan"
		print("mid diff")


class Derived(Base1, Base2):
	def __init__(self):

		# Calling constructors of Base1
		# and Base2 classes
		Base1.__init__(self)
		Base2.__init__(self)
		print("Derived")

	def printStrs(self):
		print(self.str1,self.str2)


ob = Derived()
ob.printStrs()'''

#the most basic multi-level inheritance
'''class Base(object):
    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name
    
class Child(Base):
        def __init__(self, name, age):
             Base.__init__(self, name)
             self.age = age

        def getAge(self):
           return self.age
    

class grandchild(Child):

    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address


    def getAddress(self):
        return self.address
    
obj = grandchild("boa", 39, "amazonlily")
print(obj.getName(),obj.getAge(),obj.getAddress())

'''

#heirarchical inheritance which is pretty interesting to say the least

'''
class Father(object):
    def __init__(self,sirname):
        self.sirname = sirname

    def getSirname(self):
        return self.sirname

class Kid1(Father):
    def __init__(self, firstname, sirname):
        Father().__init__(sirname)  
        self.firstname = firstname

    def getFirstname(self):
        return self.firstname

class Kid2(Father):
    def __init__(self, firstname2,sirname):
        Father().__init__(sirname) 
        self.firstname2 = firstname2

    def getfirstname2(self):
        return self.firstname2
    
fullname2 = Kid2("Ace","D.")
fullname1 = Kid1("Sabo","D.")
print(fullname2.getfirstname2())
print(fullname1.getFirstname())

'''

'''print(len("string"))'''

#polymorohism with class methods

class Kenya():
	def capital(self):
		print("Nairobi is the capital of India.")

	def language(self):
		print("swahili is the most widely spoken language of India.")

	def type(self):
		print("kenya is a developing country.")

class USA():
	def capital(self):
		print("Washington, D.C. is the capital of USA.")

	def language(self):
		print("English is the primary language of USA.")

	def type(self):
		print("USA is a developed country.")

obj_ken = Kenya()
obj_usa = USA()
for country in (obj_ken, obj_usa):
	country.capital()
	country.language()
	country.type()


        

        


        

