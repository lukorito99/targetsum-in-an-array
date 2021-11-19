""" function 'canSum(targetSum,num)' that takes in a targetSum and an array of numbers
as arguments

function returns boolean indiacting whether or not it's possible to generate the targetSum
using numbers from array

An element of the array can be used as many times as needed

All input numbers are nonnegative"""


# recursively

def sum(targetSum, num):  #time complexity O(num**targetSum)-exponetial
    if targetSum == 0:
        return True

    if targetSum < 0:
        return False

    for i in num:
        x = targetSum - i
        if sum(x, num) == True:
            return True

    return False


# memoize sum

def dynamic_sum(targetSum,num,memo=dict()):

    if targetSum in memo:
        return memo[targetSum]

    #base case
    if targetSum == 0:
        return True

    #invalid
    if targetSum < 0:
        return False

    for i in num:
        x = targetSum - i
        if dynamic_sum(x, num,memo) == True:
            memo[x]=True
            return True


    memo[targetSum] = True
    return False



