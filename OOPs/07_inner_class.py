class Student:
    #This is a outer class
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        #You can create object of inner class inside the outer class like below
        self.lap=self.Laptop()
    def show(self):
        print(self.name, self.rollno)
    
    class Laptop:
        #This is a inner class
        def __init__(self):
            self.brand="HP"
            self.cpu="i5"
            self.ram=8
        def show(self):
            print(self.brand,self.cpu,self.ram)



s1=Student("Arpandev",5)
s2=Student("Priyam",4)
lap1=s1.lap
s1.show()
lap1.show()

#lap1=s1.lap
#lap2=s2.lap
#print(id(lap1))
#print(id(lap2))

##You can create object of inner class outside the outer class provided you use
##outer class name to call it

lap1=Student.laptop()



