age = input("How old are you: ")

if age:
    age = int(age)
    if age >= 16 and age < 18:
        print("You can have driving license but need to drive with your parent")
    elif age >= 18:
        print("You can drive")
    else:
        print("You can't drive, you're too young!")
else:
    print("Please enter your age")
