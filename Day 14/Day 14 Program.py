f = open("Day 14 Input.txt", "r")

fileinput = f.read()

f.close()


#Part 1 and Part 2


walls = fileinput.splitlines()

blocks = set()
moving_sand = (500, 0)




for i in walls:
    corners = i.split(" -> ")
    edges = []
    for j in corners:
        x, y = j.split(",")
        blocks.add((int(x), int(y)))
        edges.append([int(x), int(y)])
    for k in range(len(edges) - 1):
        first = edges[k]
        second = edges[k + 1]

        copy = [int(first[0]), int(first[1]), int(second[0]), int(second[1])]


        if first[0] > second[0]:
            while copy[2] <= copy[0]:
                blocks.add((int(copy[2]), int(copy[3])))
                copy[2] += 1
        elif first[0] < second[0]:
            while copy[2] >= copy[0]:
                blocks.add((int(copy[2]), int(copy[3])))
                copy[2] -= 1
        elif first[1] > second[1]:
            while copy[3] <= copy[1]:
                blocks.add((int(copy[2]), int(copy[3])))
                copy[3] += 1
        elif first[1] < second[1]:
            while copy[3] >= copy[1]:
                blocks.add((int(copy[2]), int(copy[3])))
                copy[3] -= 1
        else:
            print("error")



added = 0


while moving_sand[1] < 500:

    #print(moving_sand)
    #for i in blocks:
    #    print(i, end = " ")
    #print("")
    if (moving_sand[0], moving_sand[1]+1) in blocks:
        if (moving_sand[0]-1, moving_sand[1]+1) in blocks:
            if (moving_sand[0]+1, moving_sand[1]+1) in blocks:
                if moving_sand in blocks:
                    assert(1 == 0)
                blocks.add(moving_sand)

                added += 1
                moving_sand = (500, 0)
            else:
                moving_sand = (moving_sand[0]+1, moving_sand[1]+1)
        else:
            moving_sand = (moving_sand[0]-1, moving_sand[1]+1)

        


    else:
        moving_sand = (moving_sand[0], moving_sand[1]+1)


print(added)


                
#Day 2


walls = fileinput.splitlines()

blocks = set()
moving_sand = (500, 0)



max_y = 0
all_points = fileinput.split()
for i in all_points:
    if "," in i:
        x, y = i.split(",")
        max_y = max(max_y, int(y) + 2)

walls.append("%d,%d -> %d,%d" % (500 - max_y * 2, max_y, 500 + max_y * 2, max_y))



for i in walls:
    corners = i.split(" -> ")
    edges = []
    for j in corners:
        x, y = j.split(",")
        blocks.add((int(x), int(y)))
        edges.append([int(x), int(y)])
    for k in range(len(edges) - 1):
        first = edges[k]
        second = edges[k + 1]

        copy = [int(first[0]), int(first[1]), int(second[0]), int(second[1])]


        if first[0] > second[0]:
            while copy[2] <= copy[0]:
                blocks.add((int(copy[2]), int(copy[3])))
                copy[2] += 1
        elif first[0] < second[0]:
            while copy[2] >= copy[0]:
                blocks.add((int(copy[2]), int(copy[3])))
                copy[2] -= 1
        elif first[1] > second[1]:
            while copy[3] <= copy[1]:
                blocks.add((int(copy[2]), int(copy[3])))
                copy[3] += 1
        elif first[1] < second[1]:
            while copy[3] >= copy[1]:
                blocks.add((int(copy[2]), int(copy[3])))
                copy[3] -= 1
        else:
            print("error")



added = 0


while moving_sand[1] < 500:
    if moving_sand == (500, 0) and (500, 0) in blocks:
        break
    #print(moving_sand)
    #for i in blocks:
    #    print(i, end = " ")
    #print("")
    if (moving_sand[0], moving_sand[1]+1) in blocks:
        if (moving_sand[0]-1, moving_sand[1]+1) in blocks:
            if (moving_sand[0]+1, moving_sand[1]+1) in blocks:
                if moving_sand in blocks:
                    assert(1 == 0)
                blocks.add(moving_sand)

                added += 1
                moving_sand = (500, 0)
            else:
                moving_sand = (moving_sand[0]+1, moving_sand[1]+1)
        else:
            moving_sand = (moving_sand[0]-1, moving_sand[1]+1)

        


    else:
        moving_sand = (moving_sand[0], moving_sand[1]+1)


print(added)

