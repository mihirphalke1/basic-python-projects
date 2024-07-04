import random

print("Welcome to number guessing game!")
print("I am thinking of a number between 1 to 100. ")
difficulty=input("Choose the difficulty of the game. Type 'easy' or 'hard': ").lower()      #let user decide diffuculty and choose number of chances accrodingly

chances=0
if difficulty=="easy":
    chances=10
    print(f"You have {chances} guesses left.")
else:
    chances=5
    print(f"You have {chances} guesses left.")

random_number=random.randint(1,100)         #choose a random number from 1 to 100

while chances!=0:
    guess=int(input("Enter your guess: "))
    if guess > random_number:
        print("Too high")
        chances-=1
        print(f"You have {chances} guesses left.")
    elif guess < random_number:
        print("Too low")
        chances-=1
        print(f"You have {chances} guesses left.")
    else:
        print("Correct guess!")
        chances=0
