#Goal: This program is to find out if given number is prime or not
#Input: Number (Whole number)
#Ouput : Number is prime/Not prime

#Input Example: 13
#Output Expectation : 13 is prime

#Input Example: 15
#Output Expectation : 15 is not a prime

Number = int (input("Enter number: "))

factorFound = False

for factorNumber in range(2, Number):
    remainder = Number % factorNumber
    if remainder == 0:
        factorFound = True

if factorFound == False:
    print(f"{Number} is prime")
else:
    print(f"{Number} is not prime")
        
        
