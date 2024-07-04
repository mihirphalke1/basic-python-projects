import random
print("Welcome to hangman!")

word_list = ["aardvark", "baboon", "camel"]
a=random.choice(word_list)                          #choose a random word from wordlist

word=[]
for i in a:                                         #create a list with underscores equal to the number of underscores
    word+="_"

gameEnd=False
lives=6

while not gameEnd:
    x=input("Guess the word!: ").lower()            #take user's guess
    found=False                                     #flag
    for i in range(len(a)):                         
        if a[i]==x:                                 #check if letters of random word are equal to the guess
            word[i]=x                               #if yes, set flag to found and set that index of word equal to the guessed letter
            found=True
    if not found:                                   #if guess is wrong, decrease one life and print remaining lives.
        lives-=1
        print(f"You have {lives} lives left.")
    print(word)  

    if "_" not in word:                             #if no more underscores are left, it means that the word is correctly guessed
        gameEnd=True
        print("Correct guess, You win!")

    if lives==0:                                    #if lives end, stop the game
        print("You lose!")
        gameEnd=True
        