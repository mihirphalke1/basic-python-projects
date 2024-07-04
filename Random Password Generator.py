import random
import os

off=False

while not off:

    print("Welcome to random password generator!")
    #Take details of number of letters, symbols and numbers required in the password
    x=int(input("How many letters would you like in your password? "))
    y=int(input("How many symbols would you like in your password? "))
    z=int(input("How many numbers would you like in your password? "))


    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
               'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
               'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*', '+']

    l=[]
    #using for loop and iterating through the list of letter, numbers and symbols to select a random letter of password using random 
    # module and appending to a list L.
    for letter in range(1, x+1):                
        l.append(random.choice(letters))
    for symbol in range(1,y+1):
        l.append(random.choice(symbols))
    for number in range(1,z+1):
        l.append(random.choice(numbers))

    random.shuffle(l)   #shuffling the letters, symbols and numbers
    p="".join(l)        #joining the shuffled list elements to password
    print(f"Your random password is: {p}")

    c=input("Do you want to generate another random password? Type 'yes' or 'no': ").lower()
    if c=="no":
        off=True
        print("Thank you!")
    elif c=="yes":
        os.system('clear')