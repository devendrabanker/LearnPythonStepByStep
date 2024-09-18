#Goal: This program is to calculate area of a trapezoid
#Input: a (base), b(base), height
#Equation: (a+b)/2 * height
#Output: Area of trapezoid

#Input Example: a = 10, b =50, h = 20
#Output : 600

a = float(input("Enter a: "))
b = float(input("Enter b: "))
h = float(input("Enter h: "))

AreaOfATrapezoid = ((a + b) / 2) * h

print(f" AreaOfATrapezoid = {AreaOfATrapezoid} for a={a}, b={b}, h={h}")
