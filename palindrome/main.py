# Simple program that checks if a given string is a palindrome
from typing import Type


def isPalindrome(word) -> bool:
    log = open("log.txt", "a")
    
    try:
        word = word.lower()
    except AttributeError:
        print("Please enter a word!")
        quit()
    
    if word[::-1] == word:
        log.write(f"Is a palindrome: {word}\n")
        log.close()
        return True
    else:
        log.write(f"Is not a palindrome: {word}\n")
        log.close()
        return False
    
    
print(isPalindrome("malayalam"))
