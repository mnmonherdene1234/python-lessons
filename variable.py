# In Python, a variable is a name that refers to a value stored in the computer's memory.
# Variables are used to store data, such as numbers, text, or other objects, and can be used in calculations or other operations.

# A variable is created the moment you first assign a value to it.
# In Python, you can assign a value to a variable using the = sign, like this:
x = 5
print(x)  # 5

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = "Hello, world!"
print(x)  # Hello, world!

# Now, x refers to a string instead of an integer.
# You can also assign multiple variables at once using a comma-separated list, like this:
x, y, z = 1, 2, 3
print(x, y, z)  # 1 2 3
# This assigns the value 1 to x, 2 to y, and 3 to z.
# Overall, variables are an essential part of programming in Python and allow you to store and manipulate data in your programs.

# Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
m = bool(3)   # m will be True

# Get the Type
# You can get the data type of a variable with the type() function.
x = 5
y = "John"
z = 5.99
m = True

print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>
print(type(z))  # <class 'float'>
print(type(m))  # <class 'bool'>

# Single or Double Quotes?
x = "John"
# is the same as
x = 'John'

# Case-Sensitive
# Variable names are case-sensitive.
a = 4
A = "Sally"
# A will not overwrite a

# Variable Names
# - A variable name must start with a letter or the underscore character
# - A variable name cannot start with a number
# - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# - Variable names are case-sensitive (age, Age and AGE are three different variables)
# - A variable name cannot be any of the Python keywords. For example: if, elif, else, for, while, do
# Valid variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Invalid variable names:
# 2myvar (variable name cannot start with a digit)
# my-var (variable name cannot contain hyphens)
# my var (variable name cannot contain spaces)

# Global variable:
# In Python, a global variable is a variable that is defined outside of any function or class,
# and can be accessed and modified from any part of the program.
a = "Global variable"

# Local variable:
# In Python, a local variable is a variable that is defined inside a function or method, and can only be accessed within that function or method.
def my_function():
    var = "Python"
    print(var)