# Simple program that checks if a given string is a palindrome

def isPalindrome(word) -> bool:
    log = open("log.txt", "a")
    
    # Checking if param is a string
    try:
        word = word.lower()
    except AttributeError:
        print("Please enter a word!")
        quit()
    
    # Checking if the reverse is the same as the normal word
    if word[::-1] == word:
        log.write(f"Is a palindrome: {word}\n")
        log.close()
        return True
    else:
        log.write(f"Is not a palindrome: {word}\n")
        log.close()
        return False
    
    
print(isPalindrome("madam"))
