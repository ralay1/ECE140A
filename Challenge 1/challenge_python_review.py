import math

#1
def print_squares():
    '''
    prints out all integer squares from 1 to 10
    '''
    for i in range(10):
        to_sqr = i+1
        print(to_sqr*to_sqr)

#2
def average(num_list):
    '''
    Returns the average of a list of numbers. Returns None if the wrong datatype is detected.
    I checked to see if the input was a list then checked to see if only integers are in the list.
    I also checked if the length of the list was 0 to return 0.
    '''
    if not isinstance(num_list, list):
        return None
    for i in num_list:
        if not isinstance(i, int):
            return None
    if len(num_list) == 0:
        return 0
    
    the_sum = 0
    for i in num_list:
        the_sum += i
    return the_sum / len(num_list)

'''
if __name__ == '__main__':
    print(average([3,4,5,6]))
    print(average([-2.3,45,0.111,11/6]))
    print(average([])) # Returns 0
    print(average([1.0,1.0,-math.inf]))
    print(average([1, 3.14, "h"]))
    print(average("hello?"))
'''
   
#3
def is_prime(an_int):
    '''
    Takes in a positive integer and returns True if the number is prime and False otherwise. 
    Assume that the input will be valid (i.e. a positive integer).
    '''
    for i in range(2, int(an_int/2)+1):
        if an_int % i == 0:
            return False
    return True


def prime_100():
    '''
    Returns the first 100 prime numbers.
    I checked to see if the number (n) was divisible by any number from 2 to n/2 + 1. 1 is not a prime number
    '''
    p_count = 0
    output = list()
    for i in range(2, 9999):
        if len(output) == 100:
            return output
        if is_prime(i):
            output.append(i)

#4
def count_letters(a_word):
    '''
    Counts the number of occurrences of each letter in a string. The return type is a dictionary.
    '''
    abcz = "abcedfghijklmnopqrstuvwxyz" #all the letters of the alphabet
    abc_dict = dict()
    for i in abcz:
        abc_dict[i] = 0 #setup dictionary
    for i in a_word.lower(): # lowercase and loop through
        if i in abc_dict.keys():
            abc_dict[i] = abc_dict[i] + 1
    return abc_dict

'''
if __name__ == '__main__':
    print(count_letters("The quick brown fox jumps over the lazy dog."))
    print(count_letters("Web serving with FastAPI!"))
'''

#5
def filter_strings(str_list):
    '''
    Takes in a list of strings as its input and returns a new list with all the strings that contain at 
    least one vowel (a, e, i, o, u) and are at least 5 characters long.
    '''
    output = list()
    flag = False # flag used to determine passing or failing the conditions
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    for word in str_list:
        if len(word) < 5: # check that length >= 5
            continue
        for v in vowel_list:
            if v in word:
                flag = True
        if flag == True: # if vowel in word append to output list
            output.append(word)
        flag = False
    return output

'''
if __name__ == '__main__':
    print(filter_strings(['hi', 'bob', 'bobert', 'zzzzzz', 'zeezee']))
'''

#6
def is_palindrome(num):
    '''
    Determines whether the number is a palindrome (i.e. it reads the same forward and backward). 
    '''
    num_str = str(num)
    n = len(num_str)
    half = num_str[0:int(n/2)]
    index = 0
    for h in half: # check matching front half
        if h != num_str[index]:
            return False
        index += 1
    index = n-1
    for h in half: # check matching back half
        if h != num_str[index]:
            return False
        index -= 1
    return True



if __name__ == '__main__':
    #2
    print(average([3,4,5,6]))
    print(average([-2.3,45,0.111,11/6]))
    print(average([])) # Returns 0
    print(average([1.0,1.0,-math.inf]))
    print(average([1, 3.14, "h"]))
    print(average("hello?"))
    #4
    print(count_letters("The quick brown fox jumps over the lazy dog."))
    print(count_letters("Web serving with FastAPI!"))
    #5
    print(filter_strings(['hi', 'bob', 'bobert', 'zzzzzz', 'zeezee']))
    #6
    print(is_palindrome(1234567.7654321))
    print(is_palindrome(-0.123))

