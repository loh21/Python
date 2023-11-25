my_name = input('Please tell me your name: ')

name_length = len(my_name)

print(f"Hello {my_name}! Your name is {name_length} characters long")

s = 'what is you name'
print (s.split())

n = ['a', 'b', 'c']
print("-".join(n))

a = [1, 2, 3, 4]
b = [4, 5, 6, 7]

#c= []
#for a_elem, b_elem in zip(a, b):
#    c.append(a_elem + b_elem)


def add_arrays(x, y):
    z= []
    for x_elem, y_elem in zip(x, y):
        z.append(x_elem + y_elem)
    #return z
    print(z)    
    
add_arrays(a, b)