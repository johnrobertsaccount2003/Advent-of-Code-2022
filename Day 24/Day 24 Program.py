f = open("Day 24 Input.txt", "r")

fileinput = f.read()

f.close()


#Part 1 and Part 2

grid = fileinput.splitlines()


places = set()
start = (1, 0)
places.add(start)
winds = set()

height = len(grid)
width = len(grid[0])

end = ((len(grid[0]) - 2), len(grid) - 1)

moves = ((-1, 0), (1, 0), (0, 0), (0, -1), (0, 1))


def move_winds(winds):
    new_winds = set()

    for i in winds:
        new_pos = list(i)
        if i[2] == ">":
            new_pos[0] += 1
        elif i[2] == "<":
            new_pos[0] -= 1
        elif i[2] == "v":
            new_pos[1] += 1    
        elif i[2] == "^":
            new_pos[1] -= 1
        else:
            assert False

        if new_pos[0] == 0:
            new_pos[0] = width - 2
        elif new_pos[0] == width - 1:
            new_pos[0] = 1
        elif new_pos[1] == 0:
            new_pos[1] = height - 2
        elif new_pos[1] == height - 1:
            new_pos[1] = 1

        new_winds.add(tuple(new_pos))

    winds = new_winds

    return winds

def move_player(winds, places):
    places_copy = set()

    for place in places:

        for move in moves:
            to_check = (place[0] + move[0], place[1] + move[1])
            if ((to_check[0] > 0 and to_check[0] < width - 1 and to_check[1] > 0 and to_check[1] < height - 1)) or to_check == end or to_check == start:
                wind_check = True
                for direction in "<>^v":
                    if (to_check[0], to_check[1], direction) in winds:
                        wind_check = False

                if to_check not in places_copy and wind_check:
                    places_copy.add(to_check)


    places = places_copy

    return places

def get_max(start, end, winds):
    time = 0

    places = set()
    places.add(start)
    while end not in places:
        time += 1
        winds = move_winds(winds)
        places = move_player(winds, places)

    return winds, time

winds = set()

for y, i in enumerate(grid):
    for x, j in enumerate(i):
        if j in "<>^v":
            winds.add((x, y, j))



winds, time = get_max(start, end, winds)
winds, time2 = get_max(end, start, winds)
winds, time3 = get_max(start, end, winds)

print(time)
print(time + time2 + time3)



