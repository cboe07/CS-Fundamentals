def my_hash_function(value):
    first_letter = value[0]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet.index(first_letter)



print(my_hash_function("abe"))
print (my_hash_function("carrot"))



def my_hash_function(phone_number):
    return phone_number[0] + phone_number[1] + phone_number[2]


print(my_hash_function("7708863306"))


def is_palindrome(word):
    word_length = len(word)
    for i in range(word_length/2):
        if word[i] == word[-1-i]:
            return True
    return False
       
print (is_palindrome('racecar'))
print (is_palindrome('abcba'))
print (is_palindrome('today'))