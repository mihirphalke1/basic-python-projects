print("Welcome to Caesar Cipher!")

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

"""take the user text and shift in the text,iterate through each letter of text,if it is an alphabet,access its index in the alphabet list
Set the iterated word equal to an element in alphabet list with index (orignal index of world +/- shift) and find its remainder 
when divided by 26"""

def encrypt(text, shift):
    encryted_text=""
    for i in text:
        if i.isalpha():
            x=alphabets.index(i)
            i=alphabets[(x+shift)%26]
            encryted_text+=i
        else:
            encryted_text+=i
    print(encryted_text)

def decrypt(text, shift):
    decrypted_text=""
    for j in text:
        if j.isalpha():
            y=alphabets.index(j)
            j=alphabets[(y-shift)%26]
            decrypted_text+=j
        else:
            decrypted_text+=j
    print(decrypted_text)

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
             'x', 'y', 'z']

end=False
while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()            #take user input of text and shift
    shift = int(input("Type the shift number:\n"))

    if direction =='encode':
        encrypt(text, shift)
    elif direction=='decode':
        decrypt(text, shift)
    else:
        print("Invalid Input")

    restart = input("Do you want to continue? Type 'yes' to continue and 'no' to end the program!\n")
    if restart=="no":
        end=True                                            #ask if user wants to continue
        print("Thank you for using Caesar Cipher!")




