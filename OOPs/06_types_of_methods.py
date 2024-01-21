#There are 3 types of method -1.Instance method 2.Class method 3. Static method

class Student:
    school="Telusko" # Class variable

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):# Instance method: It's works with instance variable
        return (self.m1+self.m2+self.m3)/3
    
    def get_m1(self): # Acessor-> get method fetch the value
        return self.m1
    def set_m1(self,value):#Mutator -> set method chage the values
        self.m1=value

    @classmethod #Decoretors (will  talk about later)
    def getSchool(cls):# clsss method: It's works with class variable
        return cls.school
    @staticmethod
    def info():# Static method: it's a method which have nothing do with class variables or instance variablesor in
        print("This is Student class")

# Creating objects
s1=Student(32,45,79)
s2=Student(89,32,12)

#printing the avg(calling avg instance method)
print(s1.avg())
#calling the class method
print(Student.getSchool())
#Note: if you want to call class method with class name
#you have to use @classmethod decoretor of the method

#calling the static method
Student.info()
      
  
