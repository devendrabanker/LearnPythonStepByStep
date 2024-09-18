#Goal: This program is to print alternate pattern of symbols in rectangle shape
#Input : Number 1 (How many symbols in a row), Number 2 (How many rows)
#output: alternate pattern of symbols in rectangle shape

#Input : Number 1: 6, Number 2: 4
#Output Example:
    # * * * * * *
    # $ $ $ $ $ $
    # * * * * * *
    # $ $ $ $ $ $

Number1 = int (input ("Enter Number 1 (how many stars in one row):  "))
Number2 = int (input ("Enter Number 2 (how many rows):  "))

for rowsCount in range(Number2):

    #print(f"RowsCount = {rowsCount}")

    remainder = (rowsCount+1)%2


    if remainder == 0:    #This is Even row
        for starsCountInARow in range(Number1):
            print("$ ", end="")
        print("")   
    else: #This is odd row
        for starsCountInARow in range(Number1):
            print("* ", end="")
        print("")    

# 1: * * * * * * 
# 2: * * * * * *  => Ar row 2: $ $ $ => Even rows => Even/odd logic
# 3: * * * * * * 
# 4: * * * * * * 

# $ $ $ $ $ $ 
# * * * * * * 
# $ $ $ $ $ $ 
# * * * * * * 