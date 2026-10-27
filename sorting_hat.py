print("Welcome to the Hogwarts Sorting Hat!")

trait = input("What best describes you?").lower()

if trait == "brave":
    print("You belong in Gryffindor!")

elif trait == "intelligent":
    print("You belong in Ravenclaw!")

elif trait == "loyal":
    print("You belong in Hufflepuff!")

elif trait == "ambitious":
    print("You belong in Slytherin!")

elif trait == "evil":
    print("You belong to the Death Eaters!")

else:
    print("The sorting Hat is confused.")

brave = input("Are you brave? ").lower()
intelligent = input("Are you intelligent? ").lower()

if brave == "yes" and intelligent == "yes":
    print("You could belong in Gryffindor or Ravenclaw!")

trait = input("What best describes you? ").lower()

if trait == "brave" or trait == "daring":
    print("You belong in Gryffindor!")