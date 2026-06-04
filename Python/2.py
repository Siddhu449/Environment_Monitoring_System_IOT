#  creating a string 
str1 = "This is a string. "  # also used a """"hii"""" or 'apna'.

# Escape sequence character
# str2 = "This is a string.\n Hello my name is Kartik "
# print(str2)

#  String concatenation

# st1 = "Ashish"
# st2 = "Redij"
# final_str = st1 +" "+st2
# print(len(final_str))


# Length os string 

# str1 = "Apna College"
# print(len(str1))

#  String Indexing
# 0 ------------- to 1 

# str = "Apna College"
# ch = str[0]
# print(ch)


# String slicing 
# Accsessing part of a 

# pass 2 index starting and ending index 

# str = "apna college"
# print(str[1:4])
# print(str[:5])
# print(str[5:12]) 
# print(str[5:len(str)]) 

# Negative index 

# str = "apple"
# print(str[-3:-1])
# print(str[-4:-1])

# String Function

# 1 .endwith("er.")       :--- Returns true if string ends with subtr
# 2 .capitalize() :---- Capitalizes 1st character+
# 3 .replace(old, new)  :--- Replace all occurrences of old with new
# 4 .find(word) :--- Returns 1st index occurences
# 5 .count("am") :--- Counts thw occurrence of substr in string

# 1

# str = "I am studying python from ApnaCollege"
# print(str.endswith("ege"))
# print(str.endswith("apple"))

# # 2

# str = "I am studying python from ApnaCollege"
# print(str.capitalize())


# # 3

# str = "I am studying python from ApnaCollege"
# print(str.replace("python", "java"))

# # 4

# str = "I am studying python from ApnaCollege"
# print(str.find("o"))

# # 5

# str = "I am studying python from ApnaCollege"
# print(str.count("from"))
# print(str.count("o"))


# Prcatice Quetions:---------
# Q1) WAP to input user's first name & print its length.
"""
name = input("Enter the users name: ")
print("Length of your name is", len(name))
"""

# Q2 ) Write a program to find a occurrence of '$' in a string
"""
str = "Hii, $Im the $ symbol $99.99"
print(str.count("$"))
"""

# ============== Conditional Statements ===============

# syntax == if-elif-else 

'''
light = input("Enter the traffic light color: ")

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")
else: 
    print("light is broken")
'''

# Q1) Grade students based on marks
'''
marks = int(input("Enter the marks: "))

if(marks >= 90):
    print("Grade of the student is A")
elif((marks > 90) and (marks >= 80)):
    print("Grade of the student is B")
elif((marks > 80) and (marks >= 70)):
    print("Grade of the student is C")
else:
    print("Grade of the student is D")
'''

# Nestign 
'''
age = int(input("Enter the age: "))
if(age >= 18):
    if(age>=65):
        print("Cannot drive")
    else: 
        print("Can drive")
else:
    print("Cannot drive")
'''

# Practice Quetions

# Q1 write a program if a number enetrd by the user odd or even.
'''
num = int(input("Enter the number: "))
if(num%2== 0):
    print("Number is even")
else:
    print("Number is odd")
'''
# Q2 Write a program to find gratest of 3 numbers entered by the user.a = int(input("Enter the frist number: "))
'''
a = int(input("Enter the frist number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if (a>b) and (a>c):
    print("Greatest number is",a)
elif (b>a) and (b>c):
    print("Greatest number is",b)
else:
    print("Greatest number is",c)
'''
# Q3 Write a program to check if a number is a multiple of 7 or not.
'''
num = int(input("Enter the number: "))

if (num % 7 == 0):
    print("Number is multiple of 7")
else:
    print("Number is not multiple of 7")
'''