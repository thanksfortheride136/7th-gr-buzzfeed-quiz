tech_class = 0
art_class = 0
math_class = 0
theatre_class = 0

print("Welcome to Your Favorite Class Quiz")
print("====================================")
print("====================================")
print()
print("Question 1:")
question1 = input("Are you more creative, logical, dramatic or technical: ")

if question1 == "technical":
    tech_class += 1
elif question1 == "creative":
    art_class += 1
elif question1 == "logical":
    math_class += 1
elif question1 == "dramatic":
    theatre_class += 1
else:
    print("That is not an option, question skipped.")

if tech_class >= art_class and tech_class >= math_class and tech_class >= theatre_class:
    print("Your favorite class is Tech Class!")

elif art_class >= tech_class and art_class >= math_class and art_class >= theatre_class:
    print("Your favorite class is Art Class!")

elif math_class >= tech_class and math_class >= art_class and math_class >= theatre_class:
    print("Your favorite class is Math Class!")

else:
    print("Your favorite class is Theatre Class!")
    
