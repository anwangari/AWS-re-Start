'''
Kenyonde Game Implementation
'''

import random

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

        