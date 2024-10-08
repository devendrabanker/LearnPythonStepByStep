#Goal: This program is to calculate area of a Right Circular Cone

#Input: 1. Radius 2. Height
#Equation: Pi * r * (r+ squareroot(h2 + r2))
#Output : AreaOfARightCircularCone

#Input Example: 1. Radius 10, 2. Height = 5
# Output Expectation : 665.4
import math

Radius = float(input("Enter Radius: "))
Height = float(input("Enter Height: "))

AreaOfARightCircularCone = 3.14 * Radius * (Radius + math.sqrt(Height * Height + Radius*Radius))  #pow(Height,2)

print(f"AreaOfARightCircularCone = {AreaOfARightCircularCone} for Radius = {Radius} and Height = {Height}")
