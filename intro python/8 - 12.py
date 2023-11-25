#lesson 5 Lists

shopping_list = ['apple', 'banana', 'orange', 'chorizo']

#index is off by 1 apple is index 0
#slicing doesn't count end range
print(shopping_list[0:2])

#adding items to list

shopping_list.append('cheese')
shopping_list[0] = 'cherries'
del shopping_list[1]

#length
print(len(shopping_list))

shopping_list2 = ['bread', 'jam', 'pb']

print(shopping_list + shopping_list2)
print(shopping_list2 * 2)

list_num = [1,32,5,88]
print(max(list_num))
print(min(list_num))


#lesson 6 Dictionaries

students = {'bob': 12, 'rachel': 13, 'emily': 14}

students['rachel'] = 14

del students['emily']

print(students)
print(students['rachel'])
print(len(students))

#keep keys unique

#lesson 7 Tuples

#tuples are immutable they cannot be modified 

tup = ('oranges', 'apple', 'bananas')
#tup[0] = "cherries" gives error
print(tup)

#reasons for tuples, consistent guarentee data does not change, saftey protect global vairables that shouldn't be changed

print(tup[0])
print(tup[0:2])

tup2 = (12, 14)
tup3 = tup + tup2
print(tup3)