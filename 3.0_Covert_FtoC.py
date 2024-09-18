#Goal: This program is to convert temperature from fahrenheit to celsius
#Input: Temperature in fahrenheit
#Equation: (77°F − 32) × 5/9 = 25°C
#output: Temperature in Celsius

#Input Example:  Temperature in fahrenheit = 77
#Output Expectation: Temperature in Celsius = 25

TemperatureInFahrenheit = float(input("Enter Temperature in fahrenheit: "))

TemperatureInCelsius = (TemperatureInFahrenheit - 32) * (5/9)

print(f"TemperatureInCelsius = {TemperatureInCelsius} for TemperatureInFahrenheit = {TemperatureInFahrenheit}")

