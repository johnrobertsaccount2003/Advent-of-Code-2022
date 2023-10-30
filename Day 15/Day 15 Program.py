f = open("Day 15 Input.txt", "r")

fileinput = f.read()

f.close()


#Part 1


sensor_info = fileinput.splitlines()

sensors = {}

impossible_sections = []

for i in sensor_info:
    words = i.split(" ")
    sensors[(int(words[2][2:-1]), int(words[3][2:-1]))] = (int(words[-2][2:-1]), int(words[-1][2:]))
    

for i in sensors:
    distance = abs(sensors[i][0] - i[0]) + abs(sensors[i][1] - i[1])

    x_spread = max(0, distance - abs(2000000 - i[1]))


    if x_spread > 0:

        impossible_sections.append([i[0] - x_spread, i[0] + x_spread])




total = 0

impossible_sections.sort(key = lambda x : x[0])





for section in range(len(impossible_sections)):

    to_add = impossible_sections[section][1] - impossible_sections[section][0]
    remove_from_add = 0

    for i in range(section - 1, -1, -1):
        if impossible_sections[i][1] > impossible_sections[section][0]:            remove_from_add = max(remove_from_add, impossible_sections[i][1] - impossible_sections[section][0])

    total += max(0, to_add - remove_from_add)


print(total)


#Part 2

for y in range(4000001):


    impossible_sections = []

    for i in sensors:
        distance = abs(sensors[i][0] - i[0]) + abs(sensors[i][1] - i[1])

        x_spread = max(0, distance - abs(y - i[1]))


        if x_spread > 0:

            impossible_sections.append([i[0] - x_spread, i[0] + x_spread])




    total = 0

    impossible_sections.sort(key = lambda x : x[0])




    for section in range(len(impossible_sections)):
        if impossible_sections[section][0] < 0:
            impossible_sections[section][0] = 0
        if impossible_sections[section][1] > 4000000:
            impossible_sections[section][1] = 4000000
        
        to_add = impossible_sections[section][1] - impossible_sections[section][0]
        remove_from_add = 0

        for i in range(section - 1, -1, -1):
            if impossible_sections[i][1] > impossible_sections[section][0]:
                remove_from_add = max(remove_from_add, impossible_sections[i][1] - impossible_sections[section][0])
        total += max(0, to_add - remove_from_add)




    if total < 4000000:

        break

print(total, impossible_sections)

for x in range(4000001):
    fail = False
    for i in impossible_sections:
        if x >= i[0] and x <= i[1]:
            fail = True
            continue
    if not fail:
        print(x, y, x*4000000 + y)

    


