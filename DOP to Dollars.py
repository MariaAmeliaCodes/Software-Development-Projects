#Maria Amelia Gonzalez Estrella
#Currency converter
money = input("What do you want to convert? The options are:\ndollars to dominican pesos\ndominican pesos to dollars\n")

#Converts Dollars to Dominican pesos
if (money == "dollars to dominican pesos"):
    dollars = int(input("How many dollars do you want to convert? "))
    dop = dollars / 0.018
    print(f"{dollars} dollars are equivalent to {dop} dominican pesos.")

#Converts Dominican pesos to Dollars
elif (money == "dominican pesos to dollars"):
    dop = int(input("How many dominican pesos do you want to convert? "))
    dollars = dop * 0.018
    print(f"{dop} dominican pesos are equivalent to {dollars} dollars.")

else:
    print("That option is not available.")