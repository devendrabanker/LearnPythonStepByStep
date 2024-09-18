#Goal: This program is to identify whether given number is even or odd
#Input: Number (Whole number)
#Output: Given number <TBD> is Even/Odd
#Logic: if number is divisible (remainder is zero for /2) then it is even, otherwise it is odd

#Input example 1: 23
#Output Expectation: Given number <23> is odd

#Input example 2: 26578
#Output Expectation: Given number <26578> is even

Number = int(input("Enter Number"))
remainder = Number%2
if remainder == 0 :
    print(f"Given number {Number} is even")
else:
    print(f"Given number {Number} is odd")

    
    
