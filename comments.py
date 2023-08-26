# Comments in Python are used to explain and clarify code. Comments are ignored by the Python interpreter and are only meant to be read by humans.
# In Python, you can create a single-line comment using the # symbol. 
# Anything after the # symbol on that line is considered a comment and is ignored by Python. For example:

# This is a comment in Python
print("Hello, world!")


def greet(name: str) -> None:
    """This function greets the person passed in as a parameter."""
    print("Hello, " + name + ". How are you?")


"""
This is a multi-line comment in Python.
It is often used as a docstring to document functions and modules.
"""
greet("Steve")
