#lesson 1 introduction

print("hello world!")

#lesson 2 Variables and Multiple assignment

age = 20
sentence = "my name is Alan"

sarah, bob, mike = 16, 21, 17
#sarah = bob = mike = 17 
#if two variables with the same name are in the code python takes the lower down variable so print bob would be 17

print(sentence)
print(bob)

name, age = "Alan", 25
print(name, age)

#lesson 3 Arithmetic operators
# + - * / %(modulo)

age1 = 12
age2 = 18

print(age1 % age2) # = 12 because there is 12 left over because it cannot be divded equally

#strings

sent1 = "today is a beautiful day"
print(sent1)

first_name = "Alan"
last_name = "Jeffery"
print(first_name + " " + last_name)
print(first_name * 10)

#slicing
sent = "Alan was playing basketball"
print(sent[0:6])

#lesson 4 Placeholders

n4me = "jake"
sentence = "%s is 15 years old"

print(sentence % n4me)

sent2ph = "%s %s was the president of the US"

print(sent2ph % ("Steve", "Jobs"))

#%s is place holder for string %d is for integers

#Format strings

nam3 = "steve"
print(f"Hello, {nam3}")

x = 10
y = 20
print(f"The sum of x and y is {x+y}")


