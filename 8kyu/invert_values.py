"""
Language: Python
Kata: Invert values
Kyu: 8
Description: Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
URL: https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad

"""

# Solution


def invert(lst):
    result = []
    for num in lst:
        result.append(num * -1)
    return result
