# Guess the number game (computer)
import random

def guessNumber():
    tries = 5
    loss_counter = 0
    win_counter = 0
    num = random.randint(1, 15)
    log = open("log.txt", "a")
    
    while tries > 0:
        i = random.randint(1, 15)
        if i != num:
            tries -= 1
            print(i)
        else:
            break
        
    # After the while loop
    if i == num:
        log.write("Castigat\n")
        print(f"{i} <<< Ai castigat!")
    else:
        log.write("Pierdut\n")
        print("Ai pierdut!")
        
    log.close()
    
    # Reading data from logs and making a win/loss counter    
    log = open("log.txt", "r")
    wins = open("wins.txt", "w")
    
    stats = log.readlines()
    
    loss_counter = stats.count("Pierdut\n")
    win_counter = stats.count("Castigat\n")
    
    wins.writelines([f"Pierdute: {loss_counter}\n", f"Castigate: {win_counter}\n"])
    
    wins.close()
    log.close()
    
    
guessNumber()
