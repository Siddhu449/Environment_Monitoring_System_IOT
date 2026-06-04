
#x = 5
#print(id(x))
#print(x)
#print("Hello World")

#===========data Type=========
Data =""""
a = 23
print(type(a))

f = 2.3
print(type(f))

b = True
print(type(b))

s = " Rahul 123 @ e"
print(type(s))
print(s)


n = None
print(type(n))
print(n)

"""


#=========Input function ===========
#name =input()
#print(name)
#print(type(name))


# Number as input
da = """
x = input()
print(x)
print(type(x))


# type conversion

y = int(x)
print(y)
print(type(y))
"""




#x = input()
#y = int(x)
#print(y)
#print(type(y))

#===========Seperator==============
#print("Rahul", "Rohit", "Kartik", 56, 78, 87, sep=",")
#print("Rahul", "Rohit", "Kartik", 56, 78, 87, sep="->")
#print("Rahul", "Rohit", "Kartik", 56, 78, 87, sep="\n")

#==== CHanging default value of seperator============
#print("Rahul", 26, end=" ")
#print("Rohit", 24)

#print("Rahul", 26, sep="\n", end="->")
#print("Rohit", 24)


#==================Operators===========================
       #========Arithmetic Operators============
ta = """
a = 9
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #   Modulas Operator
print(a//b)   # Floor operator
print(a**b)

 =======String Concatention=========

first = "Rahul"
last = "Patil"
print(first + last)
print(first +" "+ last)

print(first * 3)

print("1"+"1")
"""

#================Comparision Operator=================
Com = """
a = 6
b = 4

print(a == b)
print(a != b)
print(a < b)
print(a <= b)
print(a > b)
print(a >= b)
"""

#==================Assignment Operator===============
Assi="""
a = 5
a = a + 3
print(a)

a = 6
a = a - 3
print(a)
                 # Simple form
a = 7
a = a / 3
print(a)

a = 8
a = a * 3
print(a)
"""
Assig = """
a = 8
a += 3
print(a)

a = 7
a -= 3
print(a)

a = 6
a *= 3
print(a)

a = 5
a /= 3
print(a)
"""

#==================Logical Operator======================
Log= """
   # and operator
print(2 > 3 and 3 > 2)
print(4 > 3 and 3 > 2)

   # or operator
print(2 > 3 or 3 > 2)
print(2 > 3 or 1 > 2) 

   # not operator
print(not 3 > 2)
print(not 1 > 2) 
""" 
#=================Special Operators=============
 # in or is operator
Spe= """"
 # in
name = "Rahul Patil"
print("R" in name)
print("r" in name)
print("V" in name)
print("Vijay" in name)
print("Rahul" in name)

  # is operator tells yo if both object are at same memory location

a = 5
b = 5
print(id(a), id(b))
print(a is b)

c = 6
d = 9
print(id(c), id(d))
print(c is d)
"""
#===============Control Flow Statememt=============
# IF ElSE Condition
ifel = """
age = int(input("Enter your age: "))
if age >= 18:
   print("You are eligible for driving.")
   print("Drive Slow")
else:
   print("You are not eligible for driving.")
"""

# Nested IF Statement
NESTED  = """
age = int(input("Enter the age: "))
if age > 18 :
   if age >= 65:
      print("Take Rest")
   else:
      print("You are eligible")
      print("Drive Slow")   
else:
   print("Wait till you turn 18 ")
"""

# IF ELIF AND ELSE
Elif = """
age = int(input("Enter your age: "))
if age > 10 and age < 18:
   print("You are not eligible for driving, beuz your are under 18")
elif age >= 18 and age <= 65:
   print("You are eligible for driving")
   print("Drive Slow")
elif age > 65:
   print("You are a cross a limitie of age of driving")
else:
   print("Enter The Correct age")
"""

ex2 = """
num = int(input("Enter your num: "))
if num == 0:
   print("Your number is zero(0)")
elif num > 0:
   print("Your Number is Positive(+)")
else:
   print("Your Number is Negative(-)")

   """

# Find maximum in a list
Marks =  """
marks = [90, 30, 100, 50, 80, 95]

highest = marks[0]
for i in marks:
    if i > highest:
        highst = i
print(highest)
"""

Min_Max = """
marks = [90, 30, 100, 50, 80, 95]
highest = max(marks)
lowest = min(marks)

print(highest)
print(lowest)

"""

#================Grading System==============
Geading ="""
marks = int(input("Enter The Marks:"))

if marks >= 90 and marks <= 100:
   print("Your Grade is : A")
elif marks >= 80 and marks < 90:
   print("Your Grade is : B") 
elif marks >= 70 and marks < 80:
   print("Your Grade is : C")
elif marks >= 60 and marks < 70:
   print("Your Grade is : D")
elif marks < 60: 
   print("Your Grade is : E")
else:
   print("You entered a Invalid marks")
   """
#================Loops===============
# While Loop
whil = """
i = 1
while i <= 6:
  print("You are the best!!")
  i+=1
  """
# Printing all number from 1 to 10
All = """
i = 1
while i <= 10:
    print(i, end= " ")
    i += 1
"""

 # Printing all even number from 1 to 10
Even = """
i = 1
while i <= 10:
    if i % 2 == 0:
      print(i)
    i += 1
    """
# Print sum of all number from 1 to 10
p = """
i = 1
total = 0

while i <= 10:
   total += i
   i += 1
print(total)
"""

#==========Range()=================
# start point, jump,,,,  end point,,, 
li= """
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([list[i] for i in range(1, 10, 2)])
print([list[i] for i in range(9, 1, -1)])
print([list[i] for i in range(9, 0, -2)])
"""



#Iterator  ,  Iterable,    Iteration

# For Loop
For = """
for i in range  (1, 11):   # i : iterator
   print(i)

n = int(input("Enter The Number: "))
for i in range (1, 11):
   print(i * n)
"""
#============Pattern============
Pat = """
for i in range( 1, 6):   # Heres a 1 is a row and 6 is a colums 
   print("*" * i)

for i in range( 5, 0, -1):
   print("*" * i)

for i in range(4):
   for j in range(4):
      print("#", end=" ")
   print()
      

n = int(input("Enter The Number: "))
for i in range(1 , n+1):
   print("#" * i)
print()
"""

#=================Break, Continue and Pass===================
# Pass
BCP = """
for i in range(1, 10):
    pass


# Continue
for i in range(1, 10):
   if i == 5:  
        continue
   print(i) # if any value is 5 then this value is skipped using a continue keyword



# Break
for i in range(1, 10):
    if i == 5:
        break
   print(i)


i = 1
while i < 10:
   if i == 5:
    break
    print(i)

    i+= 1

"""
#=========================String=======================
"""
st = "Rahul" == "luhaR"
print(st)

s = "Rahul"
print(type(s))
"""
#---------Ord abd Chr----------------
"""
print(ord("A"))
print(ord("N"))

print(chr(65))
print(chr(110))
"""

#====================Indexing in Strings========================
'''
name ="Rahul Janghu"
print(name[0:5])
print(name[-1])
print(name[0:10:2])
print(len(name[0:10:2]))
'''
"""
name = "Rahul Janghu"
size = len(name)
print(name[-size])
print(size)

"""

#================String Slicing=================
"""
name = "Rahul Patil"
print(name[0:3])
size = len(name)
print(name[2:size])

print(name[:])
print(name[::])
print(name[::2])    #---- starting:ending:jump
print(name[::-1])  #---- Reverse the string
print(name[-1:0])
print(name[-1:0:-1]) 

print(name[-1: -len(name)+1: -1])

"""
#=================String Methods=====================

# 1. capitalize()
"""
name = "Rahul patil"
print(name.capitalize())
print(name.title())
print(name)
"""
# 2. upper() and Lower()
"""
# upper()
name = "Rahul Patil"
print(name.upper())

# Lower()
name1 = "RAHUL PATIL"
print(name1.lower())
"""
# 3. find()
"""
name = "Rahul Patil"
print(name.find("a")) # Find the fist location of a given word of letter
"""
# 4. count(
"""
name = "Rahul Patil"
print(name.count("a")) # Count the number of a given wordor Letter
"""
# 5.index()
"""
name = "Rahul Patil"
print(name.index("a")) # Find the first Location of a given word or Letter
"""
# 6. replace()
"""
name = "Rahul Patil"
print(name.replace("a", "A")) # Replace the given word or string to the new
print(name.replace("Rahul", "Rohan"))
"""
# 7. split()
"""
name = "Rahul Patil"
print(name.split("a")) # Split the given word or letteror sting
print(name.split(" "))
"""
# 8. isupper()
'''
name ="Rahul Patil"
name1="RAHUL PATIL"
print(name.isupper())
print(name1.isupper())
'''
# 9. islower()
"""
name = "Rahul Patil"
print(name.islower())
name1 = "rahul patil"
print(name1.islower())
"""
# 9.isnumeric()
"""
number = "18"
number1 = "18.5"
print(number.isnumeric())
print(number1.isnumeric()) # False becuased it takes aa only a integer value
"""
# 10.isalpha()
"""
name = "Rahul"
name1 = "Rahul123"
print(name.isalpha()) # it takes a puerly alphabetical word not take a any number in a string
print(name1.isalpha())
"""

#=============String Formating================
"""
name = input()
age = input()

print("Hey my name is", name, "And my age i", age)

print("Hey my name is {}. And my age is {}.".format(name, age)) # string formating--------format()
"""

#===============String Concatenation================
"""
first = input()
second = input()

print(first + second)

"""
#=================Print all vowels of a given string================
"""
text= "The quick brown fox jump over the lazy dog"
for i in text :
    if i in "aeiouAEIQOU":
        print(i)
"""

#=================Find if a string is pallindrome==================
"""
text = input("Enter the string:")
if text == text[::-1]:
    print("The Given String Is Pallindrome")
else:
    print("The Given String Is Not Pallindrome")
"""

# ===================List===================
"""
l = list()
print(type(l))

li = [1, 2, 3, 4, 4, 6]
print(list(li))
print(len(lis))
"""
# ------------Accessing--------------------
"""
li = [1, 2, 3, 4]
print(li[0])
print(li[-len(li)])
"""
#-------------Mutablity----------------
"""li = [1, 2, 3, 4]
print(id(li))
li[0] = 9
print(li)
"""

#--------------iterable?-----------------
"""
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in li:
    print(i)
"""

#-------------------------List Slicing-------------------
"""
li = [2, 3, 5, 7, 9, 4]
print(len(li))
print(li[0:3])
print(li[::-1])
print(li[:2:-1])
"""

#-----------------List Operation/Methods--------------------

# 1.count
"""
buget = [100, 200, 150, 200]
print(buget.count(100))
print(buget.count(200))
"""
# 2.index(): Returns the index of list occurence of an object
"""
buget = [100, 200, 300, 400, 500]
print(buget.index(200))
print(buget.index(400))
print(buget.index(100))
"""

# 3. pop(): Remove and returns the last element of a list
"""
name = ['Rahul','Emma','Harry',' Jack']
drop = name.pop()
print(drop)
"""
# 4.remove(): Removes the given object from out list
"""
name = ['Rahul', 'Emma', 'Harry', 'Jack']
name.remove('Emma')
print(name)
"""

# 5.sort(): It sort our list
"""
buget =  [100, 50, 70, 150, 130]
buget.sort()
print(buget)
"""

# 6.Insert(): Helps to add an element at a given index
"""
name = ['Rahul', 'Emma', 'Harry', 'Jack']
name.insert(1, "Kartos")
print(name)
"""

# 7.append(): 
"""
li = [1, 2, 3, 4, 5, ]
li.append("rahul")
li.append(2)
print(li)
l1 = [6, 7, 8]
li.append(l1)
print(li)
"""

# 8.extend():
"""
li = [1, 2, 3, 4, 5, ]
l1 = [6, 7, 8]
li.extend(l1)
print(li)

s = "Rahul"
for i in  s:
  print(i)
li.extend(s)
print(li)
"""

#------------------Heterogenous lists------------------
# Different datatypes in a single lists
"""
li = [2, "Rahul", 1.3, True]
print(type(li[2]))
print(type(li[True]))

for i in li:
   print(type(i))
   print(i)
"""

#-----------------2D Lists---------------
"""
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]

li = [l1, l2, l3]
print(li)

# indexing
print(li[0])
print(li[0][0])
print(li[0][1])
print(li[0][2])
print(li[1][0])
print(li[2][2])
"""

#---------------------Iteration in 2D List------------------------
"""
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]

li = [l1, l2, l3]
print(li)

for i in li:
  print(i)

for i in li:
  for j in i:
   print(j) 
"""

#-------------------List Comprehension--------------------
"""
for i in range (10):
   print(i ** 2)
l = []
for i in range(10):
   l.append(i)
print(l)

l = [i for i in range(20)]
s = [(i ** 2) for i in range(31)]
print(l)
print(s)
"""

#-------Find total population---------------
# access all the element of this list 
'''
li  = [ 4, 6, 5, 8, 9, 3, 2, 4, 5, 4, 3, 2, 3, 4]

population = 0
for i in li:
   # sum them up
   population += i
print(population)
'''
#====================Tuples====================
"""
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets[2] = "Rahul"
print(type(planets))
print(planets)

t = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
print(type(t))

#-----------------Indexing------------------------
print(t[0])
print(t[-1])

#-----------------Slicing---------------------
print(t[0:3])

#t[2] = "Rahul"
#print(t)

"""
#-------------Creating A Tuples---------------
    # Non empty tuple
"""
t = (
      ("Rahul", 23),
      ("Rohit", 24),
      ("Kartik", 25)
)
print(t)
print(type(t))
print(t[0])
"""       
      # Empty Tuple

"""
tu = ()
print(tu)

t1 = tuple("Rahul")
print(t1)
"""

#-----------------Muability-----------------
"""
t = (2, 3, 4)

i = ([2, 3, 4, 5], "Rahul")
print(type(i))
print(i[0])
i [0][0] = 9
print(i)
"""

#------Tuple unpacking------------
"""
a = 3
b = 4
c = 5
d = 6
print(a,b,c,d)

a,b = 9,8
print(a, b)
print(a,b,c,d)

t = 5, 6, 7, 10
a,b,c,d = t
print(a,b,c,d)
# This process is known as unpacking
"""

#-----------Tuple Operation---------------
      # 1. count()
"""
t = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(type(t))
print(t.count(11))
print(t.count(5))
"""

      # 2. index()
"""
l = [(1, 3, 5, 7, 9, 11), "Tuple", (2, 4, 6, 8, 10, 12)]
print(l[0:5])
print(l[2:4])

t = (1, 2, 4, 5, 6, 8,)
print(t.index(5))
print(t.index(1))
"""

      # 3. iteration
"""
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(len(t))

for i in t:
   print(i ** 2)
"""

      # 4. concagenation   (+ , *)
"""
t = ( 1, 2, 3, 4, 5)
t1 = (6, 7, 8, 9 , 10)
t2 = t + t1
t3 = t2 * 2
print(t2)
print(t3)
"""

# tuple to a list  and list to a  tuple
"""
t = (1, 2, 3, 4, 5)
lst = list(t)
print(type(lst))
t = tuple(lst)
print(type(t))
"""

#===============Dictionary==================

#--------Creating a Dictionary---------------

"""
d = {}
print(type(d))
print(d)

fruits = {
   "Apple" : 120,
   "Banana" : 60,
   "Mango" : 80
}
print(type(fruits))
print(fruits)

# zip

name = ["Santra", "Orenge", "watermelome"]
price = [120, 60, 80]
fruit = dict(zip(name, price))
print(type(fruit))
print(fruit)
print(len(fruit))
"""

#-----------Accessing Data in Dictionary----------------

"""
fruits = {
   "Apple" : 120,
   "Banana" : 60,
   "Mango" : 80
}
print(fruits["Apple"])
print(fruits["Mango"])
'''print(fruits[60]) it shows a error for geting the key from value used a items() methos.
print(fruits[120])
'''

 # items()
value_to_find = 60
for fruit, price in fruits.items():
    if price == value_to_find:
        print(fruit)
"""

#----------Updating a Dictionary------------
          #    2 ways
"""
fruits = {
   "Apple" : 120,
   "Banana" : 60,
   "Mango" : 80
}
fruits["Mango"] = {"1kg" : 80, "2kg" : 170}
print(fruits)

# 1).update with new value
fruits["Guava"] = 90
print(fruits)

# 2).update
new = {"Graphs" : 120, "Oranges" : 70, "Berry" : 140}
fruits.update(new)
print(fruits)
"""


#-------------Deleting a Data-----------------

"""
fruits = {
   "Apple" : 120,
   "Banana" : 60,
   "Mango" : 80
}

# Citizenship check
print("Apple" in fruits)
print("Guava" in fruits)


#  dict.pop(key)

'''fruits.pop("Apple")
print(fruits)'''

print(fruits)


# dict.popitem()  delete from last
'''fruits.popitem()
print(fruits)
'''
print(fruits)


# dict.clear()
'''
fruits.clear()
print(fruits)
'''

# del dict
'''
del fruits
print(fruits)
'''
"""

#-----------Iteration in Dictionary----------------

"""
fruits = {
   "Apple" : 120,
   "Banana" : 60,
   "Mango" : 80,
   "Grapes" : 120
}
'''
 for i in fruits :
   print(i)

for i in fruits:
   print(i, fruits[i])
'''

# using dict.iteam()
for key, value in fruits.items():
   print(key, value)
"""

#-----------------More Dictionary Methods----------------
"""
fruits = {
   "Apple" : 120,
   "Banana" : 60,
   "Mango" : 80,
   "Grapes" : 120
}
# 1.keys() return all the keys

print("Keys:", fruits.keys())

# 2.values() return all the values

print("Values:", fruits.values())

# 3.items() retrn all the items

print("Items:", fruits.items())
"""

# -------------Challenge:Find Frequency of Characters in a String-----------------
  # take an input and find the freq of each letter and return the lete and their freq

'''
name = input()
for i in name :
   print(i)
freq = {}
for i in name:
   # check for presence
   if i not in freq:
      freq[i] = 1
   # if present increment the freq by factor of 1
   else:
      freq[i] += 1
print(freq)
'''

#==============Stes=================
 # ceating empty set
'''
s = {}
print(type(s))

s = set()
print(type(s))

# Non empty set
s = {1, 2, 3, 1, 2, 4, 5, 1 ,2}
print(s)

s = set("rahul")
print(type(s))
print(s)

# Iteration
for i in s:
    print(i)
'''

#----------------Updating and deleting a set--------------
 # add: For single element
 # update(iterable)
'''
s = {1, 2, 3, 3, 5, 5, 6}
print(s)
s.add(8)
print(s)

# update
name = "Kartik"
s.update(name)
print(s)

#deleting an element
s.pop()
s.pop()
print(s)

#remove
s.remove("K")
'''

#----------------Intersection---------------
'''
python = {"Iron man", "Hulk", "Spidy", "Kartik", "Harry potter"}
java = {"Iron man", "Harry potter", "Ant man"}
print(python.intersection(java))
print(java.intersection(python))
'''

#--------------Union----------------

'''
python = {"Iron man", "Hulk", "Spidy", "Kartik", "Harry potter"}
java = {"Iron man", "Harry potter", "Ant man"}
print(python.union(java))
'''

#----------Difference----------------

'''
python = {"Iron man", "Hulk", "Spidy", "Kartik", "Harry potter"}
java = {"Iron man", "Harry potter", "Ant man"}
print(python.difference(java))
print(java.difference(python))
'''

# Challenge : Count number of unique elements in a sentence

''''
sent = "be the change you wish to see in the world"
lst = sent.split()
print(lst)

s = set(lst)
print(s)

# Final code 

sent = "be the change you wish to see in the world"

# unique word list 
lst = sent.split()

# convert into set
s = set(lst)
print(s)
'''



#===============Functions==================

#-----------Defining A Function--------------------


'''
def greet ():
    # This is body of the function 
    # Docstrings
    """
       This function greets everyone when it is called 
    """
    print("Hey, have a good day.")   
print(greet)

# calling a funtion
greet()


# Docstrings
print(greet.__doc__)
'''


# parameters

''''
def greet (name):
    print("Hey, have a good day.", name)
greet("Ashish")  

def add(a,b):
   c = a + b 
   print(a,b)
   print(c)
add(2,3) 
'''

'''
# Return
def add(a,b):
   c = a + b 
   print(a,b)
   return(c)

d = add(2,3)
print(d, type(d))


#   Code after return statement dosen't get execute


def func():
   print("Before return")
   return "Kartik"
   print("After return")
func()

a = func()

print(a)
'''

#  Returning multiple values
'''
def intro(name, age, hobby):
    return name, age, hobby

c, d, e = intro("Ashish", 25, "Swimming")
print(c, d, e)

c = intro("Ashish", 25, "Swimming")
print(c, type(c))

a, b = 2, 3
print(a, b)
'''

# Scope of a variable

'''
# a can be used anywhere in the program
a = 10

def func():
      print(a)

func()
print(a)


# global or local variables

a = 10

def func():
      a = 5      # a is a local variable inside in function 
      print(a)

func()
print(a)



a = 10

def func():
      global a
      a = 78
      print(a)

print(a)
func()
print(a)
'''

# Lambda Function 

'''
def add(a, b):
    return a + b
print(add(3, 4))

print((lambda a, b : a + b)(5, 6))

func = lambda a, b : a + b
print(type(func))

print(func(9, 10))



# Example of grater than or less than 

def larger(a, b):
   if a > b:
      return a 
   else:
      return b

print(larger(9, 5))
    
print((lambda x, y : x if x > y else y)(7, 5))

large = lambda x, y : x if x > y else y
print(large(4, 2))

'''


#  Challenge: 1st
'''
def even(li):
     for i in li:
          # check for even elements 
          if i % 2 ==0:
               print(i, end=" ")
lst = [1, 2, 4, 3, 5, 6]
print(even(lst))

'''

#  Challenge: 2nd
"""
def uniq(li): # ------- 1St way
    s =set(li)
    print(s)

list = [1,2,3,1,2,4]
print(uniq(list))


lst = [1,2,3,1,2,4]
def unique(li):
    
    new = []
    for i in li:
         if i not in new:
             new.append(i)
    return new
print(unique(lst))

"""

# Argument Types

# 1) Positional Arguments
'''
def intro(name, hobby): 
    print("Hey my name is", name)
    print("And my hobby is", hobby)
intro(" Ashish", "Swimming")
'''

# 2) Default Arguments
"""
def intro(name, hobby = "None"): 
    print("Hey my name is", name)
    print("And my hobby is", hobby)
intro(" Ashish",)

def inm(name, hobby = "Reading"): 
    print("Hey my name is", name)
    print("And my hobby is", hobby)
inm(" Ashish","Swimming")
"""

# 3) Defaul follows non-default
'''
def inm(name = "Kartik", hobby): 
    print("Hey my name is", name)
    print("And my hobby is", hobby)
inm(" Ashish","Swimming")
'''

# 4) Arbitrary Arguments
# 5) Keyword Arguments


#================OOPS IN PYTHON==================

# class and object
# class
""" class Name: """
'''
class Car:
    pass 

# object
honda = Car()
print(type(honda))
'''

# Class Constructor
'''
class Human:
   #  I want some property to be with every human objects

#    def __init__(self):
#       print("This will always print")
# ashish = Human()
# print(type(ashish))
# print(ashish)

    def __init__(self, name, age, hobby):
        self.name = name
        self.age= age
        self.hobby = hobby

ashish = Human("Kartik", 20, "Swimming")
print(ashish.name)
print(ashish.age)
print(ashish.hobby)
'''
"""
# Methods
class Human:

   # constructor
   def __init__(self, name, age, hobby):
        self.name = name
        self.age= age
        self.hobby = hobby

# methods

   def greet(self):
        print(f"Hey my name is {self.name}. Good mornig!!")

ashish = Human("Kartik", 20, "Swimming")
ashish.greet()

"""


# Class Variables
'''
class Human:
    
   #  class variables
    population = 0
    data = []

    def __init__(self, name, age):
    
      self.name = name
      self.age = age

      Human.population += 1
      Human.data.append(self.name)

    #methods
    def greet(self):
        print(f"Hey my name is {self.name}. Good morning!!. And your age is {self.age}")

ashish = Human("Kartik", 20)
print(ashish.name)
print(Human.population)

kartik = Human("Ashish", 19)
print(kartik.name)
print(Human.population)

print(Human.data)
'''


#   Adding more methods in class
'''
class Human:
    
   #  class variables
    population = 0
    data = []

    def __init__(self, name, age, alive = True):
    
      self.name = name
      self.age = age
      self.alive = alive

      Human.population += 1
      Human.data.append(self.name)

    #methods
    def greet(self):
        print(f"Hey my name is {self.name}. Good morning!!. And your age is {self.age}")

    def dead(self):
       if self.alive:    
         print(self.name, "is no more now.")
         Human.population -= 1
         self.alive= False
       else: 
          print("This person is already dead")

    def child(self, number):
       Human.population += number
       

h1 = Human("H1",70)
h2 = Human("H2", 60)

'''

# Inheritance code





























