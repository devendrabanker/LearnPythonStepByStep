#Goal: This program is to Calculate Volume of a Triangular prism
#inputs: a,b,c (sides), height
#Equation: 1/4 * h * squareroot(﹣a4+2(ab)2+2(ac)2﹣b4+2(bc)2﹣c4)
#Output: Volume of a Triangular prism

#Input Example: a:20, b:20, c:30 , h:40
#Ouput Expectation : 7937.25

import math

a = float(input("Enter a side: "))
b = float(input("Enter b side: "))
c = float(input("Enter c side: "))
h = float(input("Enter h side: "))

#﹣a4+2(ab)2+2(ac)2﹣b4+2(bc)2﹣c4

internalEquationPart1 = - pow(a,4) + 2 * pow((a*b),2) + 2*pow((a*c),2) - pow(b,4) + 2 * pow((b*c),2) - pow(c,4)

VolumeOfATriangularPrism = (1/4) * h * math.sqrt(internalEquationPart1)

print(f"VolumeOfATriangularPrism = {VolumeOfATriangularPrism} for a:{a} b:{b} c:{c} and h:{h} ")

