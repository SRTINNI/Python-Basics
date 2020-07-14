# To create a global variable inside a function, use the global keyword.
# If you use the global keyword, the variable belongs to the global scope

def mfunc():
  global x1
  x1 = "nice"

mfunc()

print("world is " + x1)
# To change the value of a global variable inside a function,
# refer to the variable by using the global keyword
x2 = "awesome"

def myfunc():
  global x2
  x2 = "fantastic"
myfunc()

print("world is " + x2)

