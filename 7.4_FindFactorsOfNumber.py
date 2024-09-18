#Goal: This program is to find factors of a given number
#Input: number
#Output: factors of number

#Input Example: 10
#Output Expectations: 1,2,5,10

Number = int(input("Enter number: "))

for factorNumber in range(1,Number+1):
   # print(f"Loop factor Number = {factorNumber}")
    remainder = Number % factorNumber
    if remainder == 0:
        print(f"Real factor number = {factorNumber}")
