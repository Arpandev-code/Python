import math
print("Hello World ")
#math.floor() used to round up the flot value
print(math.floor(3.65))
#math.cos()used to find the cos value
print(math.cos(3.65))
##variables
#int
a=1
b=3
#String
c="This is me"
#flot
d=3.4
# To find type of the variable use type()
print(type(d))
##Lets try to add strings
e="1"
f="2"
print(e+f)
# so it's concat the String

## String

str1="this is my first python string"
#Used to capitalize the first letter of the sentance
print(str1.capitalize())
#Used to to find the substring
print(str1.find("this"))
#Note-Strings are mutable in python that's why there in 0 "this" in the str1

# make string upper case
print(str1.upper())
#make it lower case
print(str1.lower())


##Python Collections (Arrays)
#There are four collection data types in the Python programming language:

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.

##LIST: simpaly Variable container

items=[1,2,3]
print(items)
print(type(items))
#Note- List can contain any type variable , not like array

items1=["harray",2,3]
#index     0   1   2
print(items1)
#changing Data in List
items1[0]="Arpandev"
print(items1)

##TUPLES: a type of DS that is very similar to list. The main difference b/w
##the two is that tuples are immutable meaning they cannot be charged once they are created.
##This makes them ideal for storing data that should not be modified,
##such as database record
tup1=(1,2,3)
#tup1[0]=3 TypeError:tuble object doesn't support assignment
print(type(tup1))

##Dictionary
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and
#do not allow duplicates.
#Note-As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

dict={}
print(type(dict))
dict["virat"]=100
dict["sachin"]=500
print(dict["virat"])
#OR
print(dict.get("virat"))
#To Print Dictionary items
print(dict.items())
#To Print keys
print(dict.keys())
# Keep in mind that dictionary just like object in JS.It's just trick to remember

#Dictionary structure 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

##Dictionaries cannot have two items with the same key:
#Ex-
thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict1)
# Note-Duplicate values will overwrite existing values

#To determine how many items a dictionary has, use the len() function:
print(len(thisdict1))

##The values in dictionary items can be of any data type:(String, int, boolean, and list data types)
thisdict2 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
#It is also possible to use the dict() constructor to make a dictionary:(Using the dict() method to make a dictionary)
#thisdict3 = dict(name = "John", age = 36, country = "Norway")
#print(thisdict3)


#A set is a collection which is unordered, unchangeable*, and unindexed.
#*Note that Set items are unchangeable, but you can remove items and add new items.

set1 = {"apple", "banana", "cherry"}
print(set1)

#List -> Set

list0=[1,2,3,4,4,5,6]
s1=set(list0)
print(s1)
# As you can see in the result set removes all dublicate eliments in the list

##Operator
a=5
b=10
print(a+b)
c="Arpandev"
# print(a+b+c) ->ERROR
# you have to typecast a & b as String:
print(str(a)+str(b)+c)
#you can print two things in print():
print("10-5 is",10-5)

##User Input & If-else
var=int(input())
print(var)
if (var>4):
    print("Variable is greater")
elif(var==2):
    print("Variable is 2")
else:
    print("Variable is not greater")

##Loops
    
i=0
for i in range(0,101):
    print(i)


while(i<101):
    print(i)
    i=i+1
##Function
def average(num1,num2):
    avr=(num1+num2)/2
    return avr
print(average(3,6))

##Exception Handeling

try:
    print(index)
except Exception as e:
    print(e)

##File Handeling

#Create & write mode 
f=open("1.txt","w")
f.write("Arpandev")
f.close()

#Read Mode
f=open("1.txt","r")
content=f.read()
f.close()
print(content)




    


























