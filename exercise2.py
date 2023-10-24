#1. Create a list of names and print the second item.
list1 = ['steve', 'jeff', 'lewis']
print(list1[1])

#2. Create a list of sports and then replace the second item with another sport.
Slist = ['basketball', 'football', 'baseball']
Slist[1] = 'tennis'
print(Slist)

#3. Create a list containing numbers and delete the fifth number from the array.
Nlist = [12,56,1,64,9]
del Nlist[4]
print(Nlist)

#4. Create two lists of numbers and merge them.
nlist1 = [1,2,3]
nlist2 = [4,5,6]

no = nlist1+nlist2
print(no)

#5. Create a list of numbers and find the length, minimum, and maximum.
numList = [153, 11, 6, 88, 90]
print(len(numList))
print(min(numList))
print(max(numList))

#6. Create a dictionary of students and scores and print out a student’s score.
scores = {'steve': 44, 'amy': 70, 'randal': 50}
print(scores['steve'])

#7. Create a dictionary with the key being names and values being ages and then delete the second key/value pair.
age = {'steve': 18, 'amy': 17, 'randal': 14}
del age['amy']
print(age)

#8. Create a dictionary of names and ages and then print out all the keys and values
print(age)

#9. Create a tuple of your favorite movies
movTup = ('toy story1', 'toy story2', 'toy story3', 'toy story4')

#10. Create a tuple and print all the items from the first to third index.
print(movTup[0:4])