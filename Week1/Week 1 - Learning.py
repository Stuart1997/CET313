#Variables
a = 2
b = a * a       #Don't need to use types or keywords like val/var to declare variables
print(b)
name = "Stuart" #Single or double quotes are used for strings

#Lists and arrays
z = [1,2,3]
print(z)
z.extend([4,5,6])   #Extend is the method for adding to an existing list
print(z)
z.append(0)         #Append is the method for adding another list to the list
print(z)

l = []
l.append(['a', 'b', 'c'])
l.append(['d', 'e', 'f']) 
print(l)    #Appends a list to a list, meaning l contains 2 lists

integerList = [1,2,3,4,5,6,7,8,9]   #Instantiates the list
print(integerList[1])   #Prints the second element of the list
3 in integerList        #Checks if '3' is anywhere in the list

firstTwo = integerList[:2]  #Gets the first two elements
print(firstTwo)
fourToEnd = integerList[4:] #Gets the fourth to the last elements
print(fourToEnd)

#All lists have a sort method
x = [4,2,3,1,5]
print(sorted(x))
x.sort()
print(x)  #Either or works

x = [1,2,3,4,5]
evens = [x for x in range(5) if x % 2 == 0]
print(evens)    

#Tuples in Python are immutable lists/arrays
myTuple1 = (1,2)
myTuple2 = 3,4

#Dictionaries - associate things like in a database
grades = { "Stuart" : 80,  "Bob" : 50 }
print(grades["Stuart"])

s = {}
s[1] = { 'Date': 1/1/16, 'Symbol' : 'Fox', 'Price' : 4.44 }
s[2] = { 'Date': 2/1/16, 'Symbol' : '2ppl', 'Price' : 24.44 }

#Counters turns a sequence of values into a dictionary, useful for histograms
from collections import Counter
c = Counter([0,1,2,0])
print(c)
Counter({0: 2, 1: 1, 2: 1})     #Either or works

#Sets are very fast checking of elements within
stopwords =set=["a", "an", "the", "yet", "you"]
print("you" in stopwords)
print("gong" in stopwords)  #Return booleans

#METHODS
def mySquare(x):
    return(x * x)
myNumber = 3
print(mySquare(myNumber))

##If and while loops
age = 95
if(age > 70): 
    print("Do not drive")
    
ac = 0
while True:
    ac = ac + 1
    print(ac)
    if ac == 4:
        break

#While and for loops doing the same thing
x = 0
while x < 10:
    print(x)
    x += 1
for x in range(10):
    print(x)


#1 Random
import random

random.seed(10)
print(random.random())


#2 Regex
import re
str = "cat"
match = re.search(r'\w\w\w', str)
if match:
    print("Found"), match.group() #Found the word cat
else:
    print("Did not find")
    
match = re.search(r'iii', 'piiig')  #True
if match: 
    print("iii in piiigs")

match = re.search(r'igs', 'piiig')  #False
if match: 
    print("igs in piiigs")


#3 Zipping data together, (Left to right)
x = [1,2,3]
y = [4,5,6]
zipped = zip(x,y)   #Zip object

x2, y2 = zip(*zipped)
print(x2)
print (y2)
x == list(x2) and y == list(y2)


#Classes
class Employee:  #Class name, base class for all employees
    empCount = 0
    
    def __init__(self, name, salary): #Constructs the class
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    
    def displayCount(self):   #Additional method
        return print("Total Employee %d" % Employee.empCount)
    
    def displayEmployee(self):
        return print("Name: ", self.name, ", Salary: ", self.salary)
    
emp1 = Employee("Stuart", 10000)
emp1.displayEmployee()
emp2 = Employee("Bob", 8000)
emp2.displayEmployee()
print("Total Employee Number: %d" % Employee.empCount)