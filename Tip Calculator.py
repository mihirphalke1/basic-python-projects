print("Welcome to tip calculator!")
bill=float(input("Enter the amount of bill: Rs "))                              #taking input of bill
tip=int(input("How much tip you want to give? (in %): "))                       #taking input of tip
people=int(input("How many people do you want to split the bill with? "))       #taking input of number of people

x= (bill + (0.01*tip*bill))/people           #calculating tip per person by adding tip % to to bill and dividing by number of people!
bill_per_person = round(x,2)
print(f"Split of each person is Rs.{bill_per_person}.")