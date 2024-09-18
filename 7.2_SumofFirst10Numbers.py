#Goal: This program is to calculate sum of 10 numbers
#Input: first 10 numbers
#Output: 1+2+3+4+5+6+7+8+9+10 => 55

sumVariable = 0

for number in range(1,11):
    sumVariable = sumVariable + number
    print(f"sumVariable = {sumVariable} CurrentNumber = {number}")
   #1= 0 1
   # 3 = 1 + 2
   # 6 = 3 + 3

print(f"sumVariable = {sumVariable}")
   
   