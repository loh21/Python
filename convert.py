#example

weight_in_ounces = 6

def ounces_to_grams(weight):
    new_weight = weight * 28.3495
    return new_weight

weight_in_ounces = 6

weight_in_grams = ounces_to_grams(weight_in_ounces)

print(f"{weight_in_grams} g")

#exercise 1


my_num = 10

def double(my_num):
    numx2 = my_num * 2
    return numx2

doubled = double(my_num)

print(doubled)

#exercise 2

my_list = [5, 7, 34, 5, 3, 545]

def big(my_list):
    big_numbers = []
    for num in my_list:
        if num > 10:
            big_numbers.append(num)

    return big_numbers

large_numbers = big(my_list)

print(large_numbers)