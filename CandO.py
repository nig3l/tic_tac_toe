#practice concepts  

class person:

    def __init__(self,age,name,height):
        self.age = age
        self.name = name
        self.height = height
        
    def say_hi(self):
        print("i am ",self.name)
        print("i am " ,self.age,"years old")
        print("i am ",self.height," feet tall")

person1=person(12 , "bosco",5.6)
person1.say_hi()