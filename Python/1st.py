#print("Hello")
#x = int(1)
#print(type(x))
#y = float(1)
#print(y)
#z = str("1")
#print(type(z))

# print a 5 number character
#a = "Hello, World!"
#print(a[5])

# Print a lenth of a string
#a = "Hello, World!"
#print(len(a))


# true or false gives if a wast word is present or not in given string using in keyword
#txt = "India is a wast people country"
#print("wast" in txt)

#txt = "India is a wast people country"
#print("wass" in txt)

# See 
#txt = "India is a wast people country"
#if "wast" in txt:
#    print("Yes 'wast' word are present")
#print(len(txt))
#print(txt[6])


# Using Not
#txt = "India is a wast people country"
#print("wast" not in txt)

#txt = "India is a wast people country"
#print("wass" not in txt)

#txt = "India is a wast people country"
#if "wass" not in txt:
 #   print("Wass word are not present in above string")



# String Sclycing
#b = "Hello, World!"
#print(b[2:11])
#print(len(b[2:11]))


#b = "Hello, World!"
#print(b[:5])

#b = "Hello, World!"
#print(b[4:])

#b = "Hello, World!"
#print(b[-5:-2])

#---------------------------------------------------------------------------------------------

# Modifyed String
#a = "Hello, World!"
#print(a.upper())

#a = "HELLO, WORLD!"
#print(a.lower())

#The strip() method removes any whitespace from the beginning or the end
#a = "      HELLO, WORLD!"
#print(a)
#print(a.strip())

# The replace() method replaces a string with another string:
#a = "HELLO, WORLD!"
#print(a.replace("HELLO","GOOD BEY"))

# The split() method returns a list where the text between the specified separator becomes the list items.
#a = "Hello, World!, good, bey"
#print(a.split(",")) # returns ['Hello', ' World!']

#a = "Hello, World!, good, bey"
#print(type(a.split(",")))
#print(len(a.split(",")))


#----------------------------------------------------------------------------------------------------

# String Concatenation

#a = "Jay"
#b = "Hind"
#c = a + b
#print(c)

#Space betwenn Jay Hind Using ""
#a = "Jay"
#b = "Hind"
#c = a +" "+ b
#print(c)

# -------------------------------------Python - Format - Strings---------------------------------------

#age = 36
#txt = "My name is John, I am " + age
#print(txt)

#vote = 18
#txt = f"You age are {vote} so, basically you can eligibale for voting"
#print(txt)

#A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
#vote = 18
#txt = f"You age are {vote:.2f} so, basically you can eligibale for voting"
#print(txt) # Display the price with 2 decimals:

#math = 18
#txt = f"multiplcation is, {18 * 2}"
#txt1 = f"addition is, {18 + 2}"
#print(txt) 
#print(txt1)

#============Boolean==============

#x = "Hello"
#y = 15

#print(type(bool(x)))
#print(bool(y))

x = 200
print(isinstance(x, int))   # chech valuve is intiger or not