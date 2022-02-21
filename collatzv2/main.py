import sys
import time

def run():
    log = open("log.txt", "a")
    
    for n in range(1, sys.maxsize ^ 2):
        o_n = n
        
        start = time.time()
        while n != 1:
            if n % 2 == 0:
                n /= 2
            elif n % 2 != 0:
                n = n * 3 + 1
                
            if end - start > 5:
                print("THIS NUMBER DOES NOT HAVE COLLATZ CONJECTURE!!!")
                quit()
                
        end = time.time()
        
        log.write(f"{o_n}\n")
        

run()
