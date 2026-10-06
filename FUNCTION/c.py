# Write a function is_palindrome(string) to check whether a string is palindrome or not. Return True if it is palindrome, otherwise return False.

"""def is_palindrome(word):
    word=word.lower()
    return word==word[::-1]
xt=input("Enter a string:")
print(is_palindrome(xt))"""


# Write a function is_palindrome(string) that checks whether a string is a palindrome without considering uppercase and lowercase differences.
def is_palindrome(string):
    string = string.lower()
    return string.casefold()==string.casefold()[::-1]


xt = input("Enter a string:")
print(is_palindrome(xt))
