''' Python supports the usual logical conditions from mathematics.
An "if statement" is written by using the if keyword. '''
# if statement
x = 4
y = 44
if x < y:
    print('y is greater than x')

''' Python relies on indentation (whitespace at the beginning of a line) to 
define scope in the code. Other programming languages often use curly-brackets 
for this purpose.'''
# if statement without indentation will raise an error
'''
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error
'''
# elif
''' The elif keyword is pythons way of saying 
"if the previous conditions were not true, then try this condition".'''

x1 = 44
y1 = 44
if x1 > y1:
  print("y1 is greater than x1")
elif x1 == y1:
  print("x1 and y1 are equal")



