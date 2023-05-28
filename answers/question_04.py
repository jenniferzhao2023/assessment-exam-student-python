"""
Create a function that takes an integer and returns True if it's divisible by 100, otherwise return False.

Examples:
    divisible(1) ➞ False

    divisible(1000) ➞ True

    divisible(100) ➞ True

"""
def divisible(integer):
    if integer < 100:
        return False
    else:
        if integer % 100 == 0:
            return True
        else:
            False


print(divisible(1))

print(divisible(1000)) 

print(divisible(100))