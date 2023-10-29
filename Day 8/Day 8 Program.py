f = open("Day 8 Input.txt", "r")

fileinput = f.read()

f.close()


#Day 1

grid = fileinput.splitlines()

grid = list(map(list, grid))

seen = []

for y in grid:
    temp = []
    for x in y:
        temp.append(False)
    seen.append(temp)


for y in range(len(grid)):
    highest = -1
    for x in range(len(grid[y])):
        if int(grid[y][x]) > highest:
            seen[y][x] = True
            highest = int(grid[y][x])

for y in range(len(grid)):
    highest = -1
    for x in range(len(grid[y]) - 1, -1, -1):
        if int(grid[y][x]) > highest:
            seen[y][x] = True
            highest = int(grid[y][x])

for x in range(len(grid[0])):
    highest = -1
    for y in range(len(grid)):
        if int(grid[y][x]) > highest:
            seen[y][x] = True
            highest = int(grid[y][x])

for x in range(len(grid[0])):
    highest = -1
    for y in range(len(grid) - 1, -1, -1):
        if int(grid[y][x]) > highest:
            seen[y][x] = True
            highest = int(grid[y][x])

total = 0

for i in seen:
    for j in i:
        if j:
            total += 1

print(total)


#Day 2

highest_score = 0

for i in range(len(grid)):
    grid[i] = list(map(int, grid[i]))

for y in range(len(grid)):
    for x in range(len(grid[0])):
        scenic_score = 1


        moving_x = x
        current_view = grid[y][x]
        temp_mult = 0

        while moving_x <= len(grid[0]) - 2:
            moving_x += 1
            if grid[y][moving_x] < current_view:
                temp_mult += 1
            else:
                temp_mult += 1
                break
        scenic_score *= temp_mult
        
  
        moving_x = x
        current_view = grid[y][x]
        temp_mult = 0
        while moving_x >= 1:
            moving_x -= 1
            if grid[y][moving_x] < current_view:
                temp_mult += 1
            else:
                temp_mult += 1
                break
        scenic_score *= temp_mult


        moving_y = y
        current_view = grid[y][x]
        temp_mult = 0
        while moving_y <= len(grid) - 2:
            moving_y += 1
            if grid[moving_y][x] < current_view:
                temp_mult += 1
            else:
                temp_mult += 1
                break
        scenic_score *= temp_mult

        moving_y = y
        current_view = grid[y][x]
        temp_mult = 0
        while moving_y >= 1:
            moving_y -= 1
            if grid[moving_y][x] < current_view:
                temp_mult += 1
            else:
                temp_mult += 1
                break


        scenic_score *= temp_mult

        highest_score = max(highest_score, scenic_score)

print(highest_score)









