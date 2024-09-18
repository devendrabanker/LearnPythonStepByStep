#Goal: This program is to print pattern of stars in rectangle shape
#Input: Number1 (how many stars in one row), Number2 (how many rows)
#Ouput: Pattern of Stars in rectangle shape

#Input Example: Number 1: 7, Number 2: 5
#Output Expectation: 
    # *******
    # *******
    # *******
    # *******
    # *******
    #CTRL + / => This will comment all the lines


Number1 = int (input ("Enter Number 1 (how many stars in one row):  "))
Number2 = int (input ("Enter Number 2 (how many rows):  "))

#Printing one row of stars

for rowsCount in range(Number2):
    for starsCountInARow in range(Number1):
        print("* ", end="")
    print("")    




    





