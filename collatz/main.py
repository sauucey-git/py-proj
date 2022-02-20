# Simple program that prins Collatz sequence
def run(n):
    try:
        n = int(n)
    except ValueError:
        print("Invalid value!")
        quit()
        
    counter = 0
    print(f"{counter}: {n}")
    
    while n != 1:     
        if n % 2 == 0:
            n /= 2
            counter += 1
            print(f"{counter}: {int(n)}")
        elif n % 2 != 0:
            n = n * 3 + 1
            counter += 1
            print(f"{counter}: {int(n)}")
            
    print(f"TOTAL STEPS: {counter}")
    

run(7474)
