'''
Kenyonde Game Implementation
Instruction: The user is given three trials to guess the correct secret number
'''

import random

# Generate a random secret number
secret_number = random.randint(1, 9)

counter = 0
while counter < 3:
    number = int(input("Please guess a number between 1 and 9: "))
    counter = counter + 1
    if number == secret_number:
        print("You are a Genius")
        break
    else:
        if counter < 3:
            print("Try Again!")
    
else:    
    print("Looser")

        
