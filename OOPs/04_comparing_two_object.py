class Computer:
    def __init__(self):
        self.name="Arpandev"
        self.age=23
    def compare(self,other):#compare(who is calling,whom to compare)
        if self.age==other.age:
            return True
        else:
            return False
# craeting object
c1 = Computer()
c1.age=30
c2 = Computer()
c2.age=30

if c1.compare(c2):
    print("They are same")
else:
    print("They are Different")
