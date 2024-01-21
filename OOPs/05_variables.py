class Car:
    wheels=4 #class/static variable(belongs to class namespace)
    def __init__(self):
        self.mil=10
        self.com="BMW"# Instance/object variable(belongs to Instance namespace

#namespace is an area where you create and store object/variable
#There are 2 namespace - class/static namespace -object/instance namespace

c1=Car()
c2=Car()

c1.mil=8
#Changing the class variable using Class name, class variable refered to all objects in clthe class
Car.wheels=5

print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)
        
