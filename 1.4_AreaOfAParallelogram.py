#Goal: This program is to calculate area of a parallelogram
#Input: 1. Base 2. Height
#Output: Area of a parallelogram

#Input Example: Base = 10 Height = 20
#Outpt Expectation : 200

Base = float(input("Enter Base: "))
Height = float(input("Enter Height"))

AreaOfAParallelogram = Base * Height

print(f" AreaOfAParallelogram = {AreaOfAParallelogram} for Base = {Base} and Height = {Height}")