#Write a function count_vowels(string) to return the number of vowels in a given string.
def count_vowels(string):
    vowel='k'
    count=0
    for ch in string.casefold():
       if ch in vowel:
           count+=1
    return(count)
name=input("Enter your name:")
print(count_vowels(name))
    
