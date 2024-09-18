
#Goal: This program is to calcuate area of a hexagon

#Input: a: side
#Equation = 3 * squareroot(3) / 2 * square(a)
#Output: AreaOfAHexagon = <> for a:side = <>

#Input Example: a:side = 10
#Output Expectation : ~259.807

import math

a = float(input("Enter side: "))

AreaOfAHexagon = ((3 * math.sqrt(3)) / 2) * pow(a,2)

print(f"AreaOfAHexagon ={AreaOfAHexagon} for a:side = {a}")

