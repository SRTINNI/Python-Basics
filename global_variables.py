# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
#
# Global variables can be used by everyone, both inside of functions and outside.
x = 'cool'
def o_func() :
    print('World is '+x)

o_func()

# Create a variable inside a function, with the same name as the global variable

x1 = 'amazing'
def mfunc() :
    x1 = 'wow'
    print('World is '+x1)
mfunc()
print('World is '+ x1)