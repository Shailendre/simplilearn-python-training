
#functions
def example():
    print("example")

# paramaters
# giving default parameters values
def addition(a = 0,b = 0):
    return a + b

# will be called be default values in method definition
print(addition())
# passing with variable name
print(addition(b=10,a=10))


# global nad local variable

x = 10

def example2():
    # cannot modify the global variable within method/local scope
    # but can add "global" as hacky way to do modify the variable
    # not recommended
    global x
    x += 1
    print(x)
    # consdier that to be "final" in java.
    # but is still available within the scope of the methos
    z = 9 + x
    #print(z)
    return z

print("-------------")
# consider this global scope
# so global var. x can be reassigned.
x = example2()
print("-------------")
print("The new value for global variable x:", x)
