"""
Language: Python
Kata: You only need one - Beginner
Kyu: 8
Description: You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.
a can contain numbers or strings. x can be either.
Return true if the array contains the value, false if not. 
URL: https://www.codewars.com/kata/57cc975ed542d3148f00015b

"""

# Solution

def check(seq, elem):
    return elem in seq