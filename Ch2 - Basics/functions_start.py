#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#
# TODO: define a basic function
def func1():
    print("I am a function")


# TODO: function that takes arguments
def func2(arg1, arg2):
    print(arg1, "", arg2)

func2(10, 20)
print(func2(10,20))

# TODO: function that returns a value
def cube(x):
    return x*x*x
print(cube(3))

# TODO: function with default value for an argument
def power(num, x=1):
    result = 1;
    for i in range(x):
        result = result * num
    return result    

print(power(2))
print(power(2,3))

### if called with names doesnt have to be in the right order
print(power(x=3,num=2))

# TODO: function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

print(multi_add(4,5,10,4))
## =23
print(multi_add(,5,10,4,10))
## = 33





##function called directly - printed string
func1()

##function is being called inside print statment
## prints string and prints 'none' as there is no return value of function
print(func1())

#function isn't being executed as no parentheses
#just printing the value of the function definition itsself which represents the function object we've defined 
print(func1)


