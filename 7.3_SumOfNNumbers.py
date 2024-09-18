#Goal: This program is to calculate sum until entered number N
#Input: Number 
#Output: Sum until that number

Number = int(input("Enter Number: "))

SumVariable = 0

for index in range(Number):
    print(f"Number = {index+1}")    
    SumVariable = SumVariable + (index+1)

print(f"Sum Until the number = {SumVariable} for Number = {Number}")