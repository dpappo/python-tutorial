# functions can be saved to variables, and then called
# length_of_string = len("hello world")
# print(length_of_string)

# functions are defined with the def keyword
def say_hi(name):
    print("Hi", name)


say_hi("Dan")

# function variables are scoped; the next line produces a NameError, since it's not defined
# print(name)

name = "John"

# functions require the same number of parameters they are defined this; the next line will produce a TypeError because it is missing the name argument
# say_hi()

# functions can take in multiple parameters
# default values are set with the equal sign


def welcome(name="John", location="this tutorial"):
    print("Hi", name, "welcome to", location)


# by default, the first argument is mapped to the first parameter; this is called positional parameters
welcome("Dan")

# but this can be overridden using the equal sign
welcome(location="nowhere")

# this means that argument order doesn't particularly matter, as long as the parameter name is supplied
welcome(location="your new home", name="Sally")
