class Computer:
    #Class includes attributes(variables) & Behaviour(Method or function)
    def config(self):
        print("i5,16gb,1TB")

#Creating object of Computer
comp1=Computer()
comp2=Computer()
print(type(comp1))

#Calling the Method of class Computer
# Think Like that Suppose Computer is a human, So below line we're saying
#Hey Human walk & passing the human object
Computer.config(comp1)
Computer.config(comp2)
#Another way
comp1.config()
comp2.confit()

