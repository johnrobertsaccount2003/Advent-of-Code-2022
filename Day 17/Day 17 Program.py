f = open("Day 17 Input.txt", "r")

fileinput = f.read()

f.close()


#Day 1

if fileinput.endswith("\n"):
    fileinput = fileinput[:-1]

settled = set()


rocks = (((2, 0), (3, 0), (4, 0), (5, 0)), ((3, 0), (2, 1), (3, 1), (4, 1), (3, 2)), ((2, 0), (3, 0), (4, 0), (4, 1), (4, 2)), ((2, 0), (2, 1), (2, 2), (2, 3)), ((2, 0), (2, 1), (3, 0), (3, 1)))




height = 0

current = -1

for number in range(2022):
    drop_height = height + 3
    block = rocks[number % len(rocks)]
    positions = []
    for i in block:
        positions.append([i[0], i[1] + drop_height])

    while True:
        
        current += 1
        direction = fileinput[current % len(fileinput)]
        new_positions = []
        fail = False
        for i in positions:
            if direction == "<":
                new_position = [i[0] - 1, i[1]]
            elif direction == ">":
                new_position = [i[0] + 1, i[1]]
            else:
                print(direction)
                print("error")
            if tuple(new_position) in settled or new_position[0] < 0 or new_position[0] > 6:
                fail = True
            new_positions.append(new_position)
        if not fail:
            positions = new_positions


        new_positions = []

        fail = False
        for i in positions:
            new_position = (i[0], i[1] - 1)
            if new_position in settled or new_position[1] < 0:
                fail = True
            new_positions.append(new_position)
        if not fail:
            positions = new_positions

        else:
            for i in positions:
                settled.add(tuple(i))
                height = max(height, i[1] + 1)
            break



       
print(height)         

    

#Day 2

if fileinput.endswith("\n"):
    fileinput = fileinput[:-1]

settled = set()


rocks = (((2, 0), (3, 0), (4, 0), (5, 0)), ((3, 0), (2, 1), (3, 1), (4, 1), (3, 2)), ((2, 0), (3, 0), (4, 0), (4, 1), (4, 2)), ((2, 0), (2, 1), (2, 2), (2, 3)), ((2, 0), (2, 1), (3, 0), (3, 1)))








height = 0

current = -1

for number in range(100000):
    drop_height = height + 3
    block = rocks[number % len(rocks)]
    positions = []
    for i in block:
        positions.append([i[0], i[1] + drop_height])

    while True:
        
        current += 1
        direction = fileinput[current % len(fileinput)]
        new_positions = []
        fail = False
        for i in positions:
            if direction == "<":
                new_position = [i[0] - 1, i[1]]
            elif direction == ">":
                new_position = [i[0] + 1, i[1]]
            else:
                print(direction)
                print("error")
            if tuple(new_position) in settled or new_position[0] < 0 or new_position[0] > 6:
                fail = True
            new_positions.append(new_position)
        if not fail:
            positions = new_positions


        new_positions = []

        fail = False
        for i in positions:
            new_position = (i[0], i[1] - 1)
            if new_position in settled or new_position[1] < 0:
                fail = True
            new_positions.append(new_position)
        if not fail:
            positions = new_positions

        else:
            for i in positions:
                settled.add(tuple(i))
                height = max(height, i[1] + 1)
            break

cycle_find = set()


for y in range(10000, 11250):
    for x in range(7):
        if (x, y) in settled:
            cycle_find.add((x, y))


current = 10

cycle_points = [10000]

while True:
    current += 1
    fail = False
    for i in cycle_find:
        if (i[0], i[1] + current) not in settled:
            fail = True
            break

    if not fail:
        cycle_points.append(current)
        if len(cycle_points) == 3:
            break

cycle_rocks = len(cycle_find)

before_cycle = 0



for y in range(0, 10000):
    for x in range(7):
        if (x, y) in settled:
            before_cycle += 1

in_cycle = 0



for y in range(cycle_points[1], cycle_points[2]):
    for x in range(7):
        if (x, y) in settled:
            in_cycle += 1



total_rocks = int(22 / 5 * 1000000000000)

to_go = total_rocks - before_cycle


       
cycle = cycle_points[2] - cycle_points[1]

cycles = to_go // in_cycle

at_end = to_go % in_cycle

end_of_cycles = at_end

to_be_added = 0

y = 10000

while end_of_cycles > 0:
    to_be_added += 1
    for x in range(7):
        if (x, y) in settled:
            end_of_cycles -= 1
    y += 1

print(cycles * cycle + 10000 + to_be_added)



