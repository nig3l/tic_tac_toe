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

# The first century spans from the year 1 up to and including the year 100, 
# the second century - from the year 101 up to and including the year 200, etc.
# Given a year, return the century it is in.

def century(year):
    century = (year - 1) // 100 + 1
    return century


# In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

def square_digits(num):
    result = ""
    for digit in str(num):
        squared_digit = int(digit) ** 2
        result += str(squared_digit)
    return int(result)

# Write a function that removes the spaces from the string, then return the resultant string.

def rm_space(string):
    return string.replace(" ","")

# Nathan loves cycling.

# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

# You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.
import math
def litres(time):
    return math.floor(time*0.5)

# You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.

# Considering these factors, write a function that tells you if it is possible to get to the pump or not.

# Function should return true if it is possible and false if not

def zero_fuel(distance_to_pump, mpg, fuel_left):
    max_distance = mpg * fuel_left
    if max_distance >= distance_to_pump:
        return True
    else:
        return False
    

# In this kata you will create a function that takes a list of non-negative integers and strings 
# and returns a new list with the strings filtered out.

def filter_list(l):
    return [x for x in l if not isinstance(x, str)]


# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return sum(sentence.count(vowel) for vowel in vowels)

  
   
# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

def xo(s):
    count_x = 0
    count_o = 0
    for char in s.lower():
        if char == 'x':
            count_x += 1
        elif char == 'o':
            count_o += 1
    return count_x == count_o

# alternatively

def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
    


# Make a program that filters a list of strings and returns a list with only your friends name in it.

# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

def friend(x):
    return [name for name in x if len(name)==4]
    #Code

# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the average student in your class.

# You receive an array with your peers' test scores. Now calculate the average and compare your score!

# Return True if you're better, else False!

# Note:
# Your points are not included in the array of your class's points. 
# For calculating the average point you may add your point to the given array!
    
def better_than_average(class_points, your_points):
    total_scores = sum(class_points) + your_points
    average = total_scores / (len(class_points) + 1)  # Adding 1 for your score
    return your_points > average

# Timmy & Sarah think they are in love, but around where they live, 
# they will only know once they pick a flower each. 
# If one of the flowers has an even number of petals and 
# the other has an odd number of petals it means they are in love.

# Write a function that will take the number of petals of each flower 
# and return true if they are in love and false if they aren't.

def lovefunc( flower1, flower2 ):
    return flower1 % 2 != flower2 % 2

'''**********''' # You might know some pretty large perfect squares. But what about the NEXT one?

# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter.
# Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

# If the parameter is itself not a perfect square then -1 should be returned. 
# You may assume the parameter is non-negative.

import math

def find_next_square(sq):
    root = math.isqrt(sq)
    if root * root == sq:
        return (root + 1) ** 2
    else:
        return -1

# Write a function to split a string and convert it into an array of words.

def string_to_array(s):
    return s.split(' ')

# 
# Given a set of numbers, return the additive inverse of each. 
# Each positive becomes negatives, and the negatives become positives.

def invert(lst):
    return [-num for num in lst]



    



