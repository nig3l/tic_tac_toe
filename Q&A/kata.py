# Complete the square sum function so that it squares each number,
# passed into it and then sums the results together.

def square_sum(numbers):
    return(x**2 for x in numbers)

# Create a function that takes an integer as an argument 
# and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
    
# You get an array of numbers, return the sum of all of the positives ones.
def positive_sum(arr):
    return sum(x for x in arr if x > 0)


# Your task is to make two functions 
# ( max and min, or maximum and minimum, etc., depending on the language ) 
# that receive a list of integers as input, 
# and return the largest and lowest number in that list, 
# respectively.

def minimum(arr):
    return min(arr)   

def maximum(arr):
    return max(arr)
   

# Build a function that returns an array of integers from n to 1 where n>0.

def reverse_seq(n):
    return list(range(n, 0, -1))  # note to self range(start , stop, step)

# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

def double_char(s):
    return ''.join(char * 2 for char in s)

# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

# Array can contain numbers or strings. X can be either.

# Return true if the array contains the value, false if not.

def check(seq, elem):
    return elem in seq



# All of the animals are having a feast! Each animal is bringing one dish. 
# There is just one rule: the dish must start and end with the same letters as the animal's name. 
# For example, the great blue heron is bringing garlic naan and the chickadee is bringing chocolate cake.

# Write a function feast that takes the animal's name and dish as arguments and returns true or false 
# to indicate whether the beast is allowed to bring the dish to the feast.

# Assume that beast and dish are always lowercase strings, and that each has at least two letters. 
# beast and dish may contain hyphens and spaces, but these will not appear at the beginning or end of the string. 
# They will not contain numerals.


def feast(beast, dish):
 # Extract the first and last letters of the beast and dish
    beast_start = beast[0]
    beast_end = beast[-1]
    dish_start = dish[0]
    dish_end = dish[-1]
    
    # Check if the first and last letters match
    if beast_start == dish_start and beast_end == dish_end:
        return True
    else:
        return False


    



