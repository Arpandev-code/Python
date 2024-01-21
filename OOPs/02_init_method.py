##init
class Computer:
    #__init__ is an instance method that initializes a newly created object.
    #It takes the object as its first argument followed by additional arguments. 
    #If you're from Java backgroud you can think __init__ method as a constructor
    def __init__(self,cpu,ram):
        print("in init")
        self.cpu=cpu
        self.ram=ram
        
    def config(self):
        print("Config is",self.cpu,self.ram)
        
comp0=Computer('i5',16)
comp3=Computer('Ryzen 3',8)
# In output "in init" prints two times cuz when new object created init special
# method get called everytime. Here we created two object
comp0.config()
comp3.config()
