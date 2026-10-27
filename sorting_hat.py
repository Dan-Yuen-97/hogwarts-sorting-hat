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

not TRUE = FALSE
not FALSE = TRUE

tired = False
trait = input("What best describes you? ").lower()

if (trait == "brave" or trait == "daring") and not tired:
    print("You belong in Gryffindor!")

bravery = int(input("how brave are you on a scale of 1-10? "))
loyalty = int(input("how loyal are you on a scale of 1-10? "))

if bravery >= 7 and loyalty >= 5:
    print("You could belong in Gryffindor or Hufflepuff!")