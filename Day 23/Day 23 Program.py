f = open("Day 23 Input.txt", "r")

fileinput = f.read()

f.close()


#Day 1

elflines = fileinput.splitlines()

elves = set()

for y, i in enumerate(elflines):
    for x, j in enumerate(i):
        if j == "#":
            elves.add((x, y))

moves = [[(-1, -1), (0, -1), (1, -1)], [(-1, 1), (0, 1), (1, 1)], [(-1, 1), (-1, 0), (-1, -1)], [(1, -1), (1, 0), (1, 1)]]

el = list(elves)
el.sort()
#print(el)


for _ in range(10):
    proposals = set()
    not_these = set()
    stills = set()
    flops = set()
    full_list = {}
    elf_copy = elves.copy()
    for i in elves:
        x = i[0]
        y = i[1]
        #print(x, y)
        big_fail = True
        for move_list in moves:
            for move in move_list:
                if (x+move[0], y+move[1]) in elves:
                    big_fail = False
        if not big_fail:
            big_fail = True
            for move in moves:
                success = True
                for checking in move:
                    if (x+checking[0], y+checking[1]) in elves:
                        success = False
                    else:
                        #print("t, ", x, y, (x+checking[0], y+checking[1]))
                        #print("w", checking, (x+checking[0], y+checking[1]))
                        pass
                if success:
                    big_fail = False
                    to_move = move[1]
                    if (x+to_move[0], y+to_move[1]) in proposals:
                        not_these.add((x+to_move[0], y+to_move[1]))
                        stills.add((x, y))
                        to_still = full_list[(x+to_move[0], y+to_move[1])]
                        stills.add(to_still)
                    else:
                        proposals.add((x+to_move[0], y+to_move[1]))
                        full_list[(x+to_move[0], y+to_move[1])] = (x, y)
                    break
            if big_fail:
                stills.add((x, y))
        else:
            stills.add((x, y))

    flops = (proposals - not_these)
    elves = (proposals - not_these) | stills

    move_copy = moves[0]

    del moves[0]
    moves.append(move_copy)

el = list(elves)
el.sort()
print(el)


maxx = -99999999
maxy = -99999999
minx = 999999999
miny = 999999999

for i in el:
    maxx = max(maxx, i[0])
    minx = min(minx, i[0])
    maxy = max(maxy, i[1])
    miny = min(miny, i[1])
    
width = maxx - minx + 1
height = maxy - miny + 1

total = width * height - len(elves)

print(total)


#Day 2


elves = set()

for y, i in enumerate(elflines):
    for x, j in enumerate(i):
        if j == "#":
            elves.add((x, y))

moves = [[(-1, -1), (0, -1), (1, -1)], [(-1, 1), (0, 1), (1, 1)], [(-1, 1), (-1, 0), (-1, -1)], [(1, -1), (1, 0), (1, 1)]]

el = list(elves)
el.sort()
#print(el)

count = 0

while True:
    count += 1
    proposals = set()
    not_these = set()
    stills = set()
    flops = set()
    full_list = {}
    elf_copy = elves.copy()
    for i in elves:
        x = i[0]
        y = i[1]
        #print(x, y)
        big_fail = True
        for move_list in moves:
            for move in move_list:
                if (x+move[0], y+move[1]) in elves:
                    big_fail = False
        if not big_fail:
            big_fail = True
            for move in moves:
                success = True
                for checking in move:
                    if (x+checking[0], y+checking[1]) in elves:
                        success = False
                    else:
                        #print("t, ", x, y, (x+checking[0], y+checking[1]))
                        #print("w", checking, (x+checking[0], y+checking[1]))
                        pass
                if success:
                    big_fail = False
                    to_move = move[1]
                    if (x+to_move[0], y+to_move[1]) in proposals:
                        not_these.add((x+to_move[0], y+to_move[1]))
                        stills.add((x, y))
                        to_still = full_list[(x+to_move[0], y+to_move[1])]
                        stills.add(to_still)
                    else:
                        proposals.add((x+to_move[0], y+to_move[1]))
                        full_list[(x+to_move[0], y+to_move[1])] = (x, y)
                    break
            if big_fail:
                stills.add((x, y))
        else:
            stills.add((x, y))

    flops = (proposals - not_these)
    elves = (proposals - not_these) | stills

    move_copy = moves[0]

    del moves[0]
    moves.append(move_copy)

    if elf_copy == elves:
        break

print(count)


