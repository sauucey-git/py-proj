# Simple program that finds the next perfect square
from math import sqrt

def nextPerfectSquare(n) -> int:
    log = open("log.txt", "a")
    
    if n > 214748399:
        print("Enter a smaller number.")
        quit()
    
    for i in range(n, 2147483647):
        if ((round(sqrt(i)) * round(sqrt(i))) == i) and (i > n):
            log.write(f"Perfect square {i} bigger than {n}\n")
            log.close()
            return i
        
        
print(nextPerfectSquare(885))
    