# BluePrint

class Car:
    #constructor function
    def __init__(self,name,tyres):
        self.name=name
        self.tyres=tyres
    #methods 
    def start(self,userName):
        print("Starting the car "+self.name+" By "+userName)
    def stop(self):
        print("Stopping the car "+self.name)

class Cat(Car):
    #constructor function
    def __init__(self,name,legs):
        self.name=name
        self.leg=legs
    
    # methods
    def speak(self):
        print("Meow.... by "+self.name)
        
    

    

car1= Car("audi",5)
# car2= Car("benz",4)
# car3= Car("honda",10)

cat1=Cat("Tom",4)

cat1.start()



# car3.start("Leo")

# cat1.speak()

# str1="Hello"

#print(type(str1)) #<class 'str'>
# print(type(cat1)) #<class 'str'>