

# def bubble_sort(array):
# 	count = 0
# 	counter = len(array)
# 	for i in range(0,len(array)):
# 		sort = False;
# 		for j in range(0,len(array)-1):
# 			temp = 0;
# 			if (array[j] > array [j + 1]):
# 				temp = array[j];
# 				array[j] = array[j+1]
# 				array[j+1] = temp
# 				sort = True
# 			if(sort == False):
# 				break;
# 			else:
# 				count = count + 1
# 			counter = counter - 1
# 	return array


# input_arrays = [
#     [],
#     [9, 8, 7, 6, 5, 4, 3, 2, 1],
#     [1, 2, 3, 4],
#     [4, 6, 1, 3, 7, 8, 4, 3, 4],
#     [1],
#     [1, 3, 2]
# ]

# for array in input_arrays:
#     print("")
#     print(" Input: " + str(array))
#     sorted_array = bubble_sort(array)
#     print("Output: " + str(sorted_array))







# CORRECT

# def bubble_sort(my_array):
#     array_length = len(my_array)
#     total_number_of_passes = array_length

#     for i in range(0, total_number_of_passes):
#         for j in range(0, array_length):
#             if j == array_length - 1:
#                 continue

#             if my_array[j] > my_array[j + 1]:

#                 temp = my_array[j]
#                 my_array[j] = my_array[j + 1]
#                 my_array[j + 1] = temp

#     return my_array

# input_arrays = [
#     [],
#     [9, 8, 7, 6, 5, 4, 3, 2, 1],
#     [1, 2, 3, 4],
#     [4, 6, 1, 3, 7, 8, 4, 3, 4],
#     [1],
#     [1, 3, 2]
# ]

# for array in input_arrays:
#     print("")
#     print(" Input: " + str(array))
#     sorted_array = bubble_sort(array)
#     print("Output: " + str(sorted_array))




# #################################################

# # Sum of multiples of 3 and 5 from 1 to 1000

# sum_one = 0
# sum_two = 0
# for i in range(0,10000000):
# 	if i % 3 == 0:
# 		sum_one += i
# 	elif i % 5 == 0:
# 		sum_two += i

# print sum_one
# print sum_two

# sum_three = sum_one + sum_two

# print sum_three




#  # MORE EFFICIENT


#  divide 100/3 = 33.   so n =33

#  n*[(n(n+1))/2]   = n*(1+2+3+4+5+6...)

# [(n(n+1))/2] = (1+2+3+4+5+6...)



# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

# import datetime

# def run_program():
#     MAX = 25000000
#     sum = 0

#     for i in range(1, MAX):
#         if i % 3 == 0 or i % 5 == 0:
#             sum = sum + i

#     print("The sum of all the multiples of 3 or 5 below " + str(MAX) + " is " + str(sum) + ".")

# start_time = datetime.datetime.now()
# run_program()
# end_time = datetime.datetime.now()
# duration = end_time - start_time
# print("This program ran in " + str(duration))

# # If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# # get 3, 5, 6 and 9. The sum of these multiples is 23.
# #
# # Find the sum of all the multiples of 3 or 5 below 1000.

# import datetime

# def sum_divisible_by(number, max):
#     sum = 0
#     i = number
#     while i < max:
#         sum = sum + i
#         i = i + number
#     return sum

# def run_program():
#     MAX = 50000000
#     sum = sum_divisible_by(3, MAX) + sum_divisible_by(5, MAX) - sum_divisible_by(15, MAX)
#     print("The sum of all the multiples of 3 or 5 below " + str(MAX) + " is " + str(sum) + ".")

# start_time = datetime.datetime.now()
# run_program()
# end_time = datetime.datetime.now()
# duration = end_time - start_time
# print("This program ran in " + str(duration))


#  # If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# # get 3, 5, 6 and 9. The sum of these multiples is 23.
# #
# # Find the sum of all the multiples of 3 or 5 below 1000.

# import datetime

# def sum_divisible_by(number, max):
#     p = int(max / number)
#     sum = number * (p * (p + 1)) / 2
#     return int(sum)

# def run_program():
#     MAX = 50000000
#     sum = sum_divisible_by(3, MAX) + sum_divisible_by(5, MAX) - sum_divisible_by(15, MAX)
#     print("The sum of all the multiples of 3 or 5 below " + str(MAX) + " is " + str(sum) + ".")

# start_time = datetime.datetime.now()
# run_program()
# end_time = datetime.datetime.now()
# duration = end_time - start_time
# print("This program ran in " + str(duration))



def power(a,b):
    total = 1
    counter = 0
    while counter < b:
        total = total * a
        counter += 1
    return total

print power(5,3)


def multiply(a,b):
    total = 0
    counter = 0
    while counter < b:
        total += a
        counter += 1
    return total

print multiply(5,3)


def recursion(a, b):
    if b == 0: 
        return ("NaNNaNNaN")
    elif a < b:
        return (0, a)
    else:
        (x, y) = recursion (a - b, b)
        return (x+1, y)

print recursion(5,3)





