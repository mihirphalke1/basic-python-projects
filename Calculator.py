def add(a,b):
    return a+b          


def subtract(a,b):
    return a-b


def multiply(a,b):
   return a*b


def divide(a,b):
    return a/b


#function to call particular operation function based on the input and store the result in a variable named answer.
def calculate(a,b, operation):
    if operation=="+":
        answer=add(a,b)

    elif operation=="-":
        answer=subtract(a,b)

    elif operation=="X":
        answer=multiply(a,b)

    elif operation=="/":
        answer=divide(a,b)
    else:
        print("Invalid operation!")
        answer=None

    return answer

def calculator():
    print("Welcome to calculator!")
    end=False
    a=float(input("Enter first number: "))

    while not end:
        operation=input("What operation do you want to perform? Type '+', '-', 'X', '/' : ")
        b=float(input("Enter second number: "))

        answer=calculate(a,b,operation)             #pass the parameters to calculate funtion

        if answer!=None:    
            print(f" {a} {operation} {b} = {answer}")
            x=input(" Type 'Yes' to continue calcuation or 'No' to start a new calculation: ").lower()
        if x=="no":
            end=True
            calculator()                            #if user wants to start new calculation, do recursion of calculator function 
        else:
            a=answer                                #else set the first number = answer from calculate funtion           
            
calculator()

