"""
Given two strings, create a function that returns the total number of unique characters from the combined string.

Examples:
    count_unique_chars("apple", "play") ➞ 5
    "appleplay" has 5 unique characters:  "a", "e", "l", "p", "y"

    count_unique_chars("sore", "zebra") ➞ 7

    count_unique_chars("a", "soup") ➞ 5

Notes:
 - Careful with empty strings
 - All characters will be lowercase.

"""

def count_unique_chars(string_1, string_2):
    string = (string_1 + string_2).lower()
    if len(string) == 0:
        return 0
    if len(string) > 0:
        return len(set(string))
          

print(count_unique_chars("apple", "play"))
print(count_unique_chars("sore", "zebra"))
print(count_unique_chars("a", "soup"))
print(count_unique_chars("", "soup"))
print(count_unique_chars("", ""))
print(count_unique_chars("APple", "play"))
