"""
Language: Python
Kata: Calculate average
Kyu: 8
Description: Write a function which calculates the average of the numbers in a given array.
URL: https://www.codewars.com/kata/57a2013acf1fa5bfc4000921

"""

# Solution


def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0
