house = input("Which house do you support? ").lower()

if house == "gryffindor":
    points = input("How many points does Gryffindor have? ")
    points = int(points)

    if points > 100:
        print("Gryffindor is doing brilliantly!")
