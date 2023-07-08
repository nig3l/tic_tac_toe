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

 # Extracting the first and last letters of the beast and dish

    beast_start = beast[0]
    beast_end = beast[-1]
    dish_start = dish[0]
    dish_end = dish[-1]
    
    # Check if the first and last letters match

    if beast_start == dish_start and beast_end == dish_end:
        return True
    else:
        return False

# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence.
# You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. 
# Be careful, there shouldn't be a space at the beginning or the end of the sentence!

def smash(words):
    # join the words with spaces " " 
    sent = " ".join(words)
    return sent

# Given a random non-negative number, 
# you have to return the digits of this number within an array in reverse order.

def digitize(n):
    # Convert the number to a string, reverse it, and convert each character back to an integer

    digits = [int(d) for d in str(n)][::-1]
    return digits

# When provided with a number between 0-9, return it in words.
# Input :: 1
# Output :: "One".

def switch_it_up(number):
     # Dictionary mapping numbers to words
    number_words = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    
    # Return the word for the given number
    return number_words[number]



    



