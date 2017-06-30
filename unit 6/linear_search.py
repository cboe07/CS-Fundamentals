# def linear_search(array, target):
# 	for i in range(len(array)):
# 		if array[i] == target:
# 			return True

# 	return False

# my_array = [1,2,3,4]

# # print(linear_search(my_array, 2))
# # print(linear_search(my_array, 5))
# # print(linear_search(my_array, 4))


# def linear_search_recursive(array, target, current_index):
# 	if current_index == len(array):
# 		return False
# 	if array[current_index] == target:
# 		return True



# 	current_index =+ 1
# 	# print(current_index)
# 	return linear_search_recursive(array, target, current_index)

# 	# Base Case -Return under certain condition
# 	# Call function again with slightly altered params, 

# print(linear_search_recursive(my_array,2,0))




def binary_search(array, target):
    left = array[0]
    right = len(array)

    while left < right:
    	mid = left + (right - left) / 2
        value = array[mid]

        if target == value:
            return mid

        elif target > value:
            if left == mid:   
                break        
            left = mid

        elif target < value:
            right = mid

    return False


print(binary_search([1,5,8,10],2))

def binary_search_recursive(array, target, left_index, right_index):
	left_index = 0
	right_index = len(array)

	mid = left_index + (right_index- min) / 2

	if mid==len(array):
	    return False

	elif array[mid] == target:
	    return mid

	elif right_index == left_index:
	    return False

	elif array[mid] < target:
	    return binary_search - recursive(array, target, min, mid - 1)

	elif array[mid] < target:
	    return binary_search - recursive(array, target, mid + 1, max)
	else:

    return mid








