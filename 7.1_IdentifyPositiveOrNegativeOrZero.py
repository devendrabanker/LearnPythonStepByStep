#Goal: This program is to find out if entered number is positive, negative or zero
#Input: Number (Whole)
#Output: Positive/Negative/Zero

#Input Example: 345
#output : Positive

#Input Example: -45
#output : Negative 

#Input Example: 0
#output : Zero

Number = int(input("Enter Number: "))

if Number > 0:
    print(f"Number {Number} is Positive")
elif Number < 0:
    print(f"Number {Number} is Negative")
else:
    print(f"Number {Number} is Zero")    
    
