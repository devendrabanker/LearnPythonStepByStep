#Goal: This program is to identify Given year is leap year or not

#Input: Any year (Whole number) => Integer => int
#Output: Given year <TBD> is leap year or not

#Input example1: 2020
#Output Expectation : Given year 2020 is leap year

#Input example2: 2021/2022/2023
#Output Expectation : Given year 2020 is not leap year

year = int(input("Enter year: "))
remainder = year%4
if remainder == 0:
    print(f"Given year {year} is leap year")
else:
    print(f"Given year {year} is Not leap year")