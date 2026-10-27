house = input("Which house do you support? ").lower()

if house == "gryffindor":
    points = input("How many points does Gryffindor have? ")
    points = int(points)

    if points > 100:
        print("Gryffindor is doing brilliantly!")

trait = input("What best describes you? ").lower()

if trait == "brave":
    house = "Gryffindor"
else:
    house = "Unknown"  

print(house)