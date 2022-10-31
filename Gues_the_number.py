import random

num_range = int(input("Enter range from 1 you would want to guess: "))
random_number = random.randint(1, num_range)
guess = int(input("Guess a Number withing the range you choosed: "))

while guess != random_number :
    if guess < random_number:
        print("Ohh sorry {guess} is too low try gain!")
        
    elif guess > random_number:
        print("Sorry Guess again {guess} is too high")
    guess = int(input("Guess again: "))
    
print("Congratulation you guessed the Number")
