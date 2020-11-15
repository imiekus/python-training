print("Please insert amount of kilometers.")
kms = input()
miles = float(kms)/1.60934  # convert from string to float and divide
miles = round(miles, 2)  # round
print(f"{kms}km is {miles}mi.")

# how round works:
# round(what you want to round, how many decimal points)
