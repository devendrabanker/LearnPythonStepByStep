#Goal: This program is to calculate volume of a cone
#Input: Radius, height
#Equation = Pi * r2 * h/3
#Ouput: VolumeOfACone

#Input Example: Radius = 20, Height = 10
#Ouput = 4188.79

Radius = float(input("Enter Radius: "))
Height = float(input("Enter Height: "))

VolumeOfACone = (3.14 * Radius * Radius) * (Height/3)

print(f"VolumeOfACone = {VolumeOfACone} for Radius = {Radius} Height = {Height}")

