#Factoral
#Daniel Jolly
loop = ("Y")
while loop == "Y":
    counter = 1
    factorals = []
    opening_number = int(input("Enter a number:"))
    end_digit = opening_number + 1

    while counter < end_digit:
        factorals.append(counter)
        counter = counter + 1
    print (factorals)
    import operator
    import functools
    total = functools.reduce(operator.mul, (factorals), 1)
    print (total)

    loop = input("Would you like to enter another number? Y or N:").upper()
else:
    print("Bye Bye")
