#Goal: This program is to print entered name 50 times
#Input : Name
#Input2: How many times we want to print
#Output: 
#1. Name
#2. Name
#Name
#Name
#Name
#Name
#Name
#Name
#Name
#10. Name


#Input Example: Devendra
#Output: 10 time Devendra

name = input("Enter name: ")
Count = int(input("Enter how many times to print: "))

for index in range(Count):
    print(f"Index = {index+1} {name}")
   # print(f"Index = {index}")


