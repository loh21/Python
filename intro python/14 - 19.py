#lesson 8 conditional statement

if 5 > 3:
    print('hello')

if 5 > 6:
    print('true')
else:
    print('false')

#relational operators
# > < >= <= == !=

#elif else if

age = 17
if age <= 15:
    print('younger than 16')
elif age == 16:
    print('you are 16')
elif age == 17:
    print('you are 17')
else:
    print('you are older than 16')

if age < 13:
    print('you are a child')
elif age >= 13 and age <= 18:
    print('you are a teenager')
else:
    print('you are an adult')

if 5 > 3 or 2 < 1:
    print('hello')

#lesson 9 For loops

list1 = ['apple', 'banana', 'cherry']
tup1 = (2,6,11)

for item in tup1:
    print(item)

for i in range(0, 10, 2): #does not include end index, 3rd number is increment number
    print(i)

for i in range(0, 5):
    for j in range(0, 3):
        print(i*j)

#lesson 10 While loops

c = 0
while c < 5:
    c = c + 1
    if c == 3:
        break
    print(c)

#control statements - break(stops loop), continue(skips and moves on), pass(place holder)

#lesson 11 Try and Except, usewful in situations when exceptions may be raised

try:
    if name > 3:
        print("hello")
except:
    print('an error was detected')

#lesson 12 Functions (code reuse and compactness)

def helloWorld():
    print("hello world!")

def greeting(name):
    print('hi ' + name + '!')

greeting('Alan')

def add(num1, num2):
    return num1 + num2

sum = add(10, 15)
print(sum)
#return passes back result to where function was called from

#lesson 13 built-in python functions

#absolute abs

#bool bool

#dir dir

#help

#exec - eval

#str, int, float