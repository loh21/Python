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

#excercises
#1. Write a script that adds 15 and 30 and divides the sum by 2. Print out the answer.
a = 15
b = 30

print((a+b)/2)
#2. Initialize two variables and use arithmetic operators to add, subtract, multiply, divide, and find the remainder.
c = 45
d = 15

print(c+d)
print(c-d)
print(c*d)
print(c/d)
print(c%d)
#3. Create a variable called name and store your name in it as a string.
name = "Alan"

#4. Create three variables in one line and assign each one a different food item.
food1, food2, food3 = "cheese", "tomato", "pizza dough"

#5. Print out "Hello" ten times using arithmetic operators.
print("Hello" * 10 )

#6. Set your name and age variables in one line with multiple assignment
myName, myAge = "Alan", 25

#7. Create two strings and then create a third variable combining both of the two original strings.
str1 = "james"
str2 = "smith"
combo1 = str1 + " " + str2
print(combo1)

#8. Create a string and print the fourth letter of the word.
word1 = "greetings"
print(word1[3])

#9. Create a string and print the letters from index 0 to 5.
print(word1[0:5])

#10. Create a variable and print all the letters from the first index until the end.
print(word1[0:])

