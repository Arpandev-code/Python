class Computer:
    def __init__(self):
        self.name="Arpandev"
        self.age=23
    def update(self):
        self.age=60
        
c1=Computer()
c2=Computer()

#printing addresses of the objects
print(id(c1))
print(id(c2))
##Point to note that: Everytime you create an object it is allocated to new space
##Now Question comes into mind that What's the size of an object & who allocates size to object
##Size of an object depends on no. of variables and size of each variable
##& Constructors are responsible to allocates size to object

# Changing the c1 object name & variable
c1.name="Priyam"
c1.age=21
# Update function
c1.update()

#printing name & age
print(c1.name)
print(c1.age)
