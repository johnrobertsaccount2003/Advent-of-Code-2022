f = open("Day 22 Input.txt", "r")

fileinput = f.read()

f.close()


#Day 1


parts = fileinput.split("\n\n")


building = parts[0]
instructions = parts[1]

instructions = "N" + instructions

new = []

builder = ""
built = []
letter = True
for i in range(len(instructions)):
    if instructions[i] in "0123456789":
        if letter:
            builder = instructions[i]
            letter = False
        else:
            builder += instructions[i]
            letter = False
    else:
        if builder != "":
            built.append(builder)
        letter = True
        built.append(instructions[i])
        builder = ""

built.append(builder)

building = building.splitlines()

maximum = 0
for i in building:
    maximum = max(maximum, len(i))

for i in range(len(building)):
    building[i] += " " * (maximum - len(building[i]))


building = list(map(list, building))

direction = "right"

left = {"right": "up", "up": "left", "left": "down", "down": "right"}
right = {"right": "down", "up": "right", "left": "up", "down": "left"}

first = True

place = [0, 0]

while building[place[1]][place[0]] != ".":                    
    place[0] += 1
                        

for i in range(0, len(built), 2):
    #print(built, i, i+1)
    turn = built[i]
    number = int(built[i+1])

    if not first:

        if turn == "L":
            direction = left[direction]
        elif turn == "R":
            direction = right[direction]
        else:
            assert 1 == 2

    

    else:
        first = False

    #print(direction)

    backup = place

    while number > 0:
        number -= 1
        to_check = place

        if direction == "up":
            #to_check[1] -= 1
            movement = (0, -1)
        elif direction == "down":
            #to_check[1] += 1
            movement = (0, 1)
        elif direction == "right":
            #to_check[0] += 1
            movement = (1, 0)
        elif direction == "left":
            #to_check[0] -= 1
            movement = (-1, 0)
    

        to_check = [to_check[0] + movement[0], to_check[1] + movement[1]]
        to_check[0] %= len(building[0])
        to_check[1] %= len(building)

        #print("".join(building[to_check[1]]))

        #print(building[to_check[1]][to_check[0]])

        if building[to_check[1]][to_check[0]] == ".":
            place = to_check
            backup = place
        elif building[to_check[1]][to_check[0]] == "#":
            place = backup
            break
        elif building[to_check[1]][to_check[0]] == " ":
            number += 1
            place = to_check
        else:
            assert 1 == 0


        #print(place)


total = 0
total += (place[1] + 1) * 1000
total += (place[0] + 1) * 4
if direction == "right":
    pass
elif direction == "down":
    total += 1
elif direction == "left":
    total += 2
elif direction == "up":
    total += 3
else:
    assert False

print(total)





