#Goal: This program is to print table for a given Number
#Input: 16
#Output: Table for <number> is 
# 16x1=16
#16x2 = 32
#....
#16x10 = 160

tableNumber= int(input("Enter table number:"))

for index in range(10):
    print(f"{tableNumber} x {index+1} = {tableNumber * (index+1) }")