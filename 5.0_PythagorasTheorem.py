#Goal: This program is to solve Pythagoras theorem
#Input: a, b
#Ouput: c
#Formula/theorem => a2 + b2=c2

#Input Example 1: a =3, b = 4 
#Output Expectation : c = 9 + 16 = 25 => squareroot(25) => 5

#Input example 2: a =6, b =8
#Output Expectation: c = 36 + 64 = 100 => squareroot(100) => 10
import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))

#temp = a*a + b*b
c = math.sqrt(a*a + b*b)

print(f"c = {c} for a={a} and b={b}")