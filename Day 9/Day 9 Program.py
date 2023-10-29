f = open("Day 9 Input.txt", "r")

fileinput = f.read()

f.close()


#Day 1


locations = set()



head = [0, 0]
tail = [0, 0]

locations.add(tuple(tail))

instructions = fileinput.splitlines()


for instruction in instructions:
    parts = instruction.split(" ")
    for i in range(int(parts[1])):
        if parts[0] == "R":
            head[0] += 1
        elif parts[0] == "L":
            head[0] -= 1
        elif parts[0] == "U":
            head[1] += 1
        else:
            head[1] -= 1

        if (abs(head[0] - tail[0]) >= 2 and abs(head[1] - tail[1]) >= 1) or (abs(head[0] - tail[0]) >= 1 and abs(head[1] - tail[1]) >= 2):
            if tail[0] < head[0]:
                tail[0] += 1
            else:
                tail[0] -= 1
            if tail[1] < head[1]:
                tail[1] += 1
            else:
                tail[1] -= 1

        elif (abs(head[0] - tail[0])) >= 2:
            if tail[0] < head[0]:
                tail[0] += 1
            else:
                tail[0] -= 1          

        elif (abs(head[1] - tail[1])) >= 2:
            if tail[1] < head[1]:
                tail[1] += 1
            else:
                tail[1] -= 1  

        locations.add(tuple(tail))


print(len(locations))

#Day 2

rope = [[0, 0] for i in range(10)]

locations = set()

locations.add(tuple(rope[-1]))

instructions = fileinput.splitlines()


for instruction in instructions:
    parts = instruction.split(" ")
    for i in range(int(parts[1])):
        if parts[0] == "R":
            rope[0][0] += 1
        elif parts[0] == "L":
            rope[0][0] -= 1
        elif parts[0] == "U":
            rope[0][1] += 1
        else:
            rope[0][1] -= 1

        for j in range(len(rope) - 1):

            if (abs(rope[j][0] - rope[j+1][0]) >= 2 and abs(rope[j][1] - rope[j+1][1]) >= 1) or (abs(rope[j][0] - rope[j+1][0]) >= 1 and abs(rope[j][1] - rope[j+1][1]) >= 2):
                if rope[j+1][0] < rope[j][0]:
                    rope[j+1][0] += 1
                else:
                    rope[j+1][0] -= 1
                if rope[j+1][1] < rope[j][1]:
                    rope[j+1][1] += 1
                else:
                    rope[j+1][1] -= 1

            elif (abs(rope[j][0] - rope[j+1][0])) >= 2:
                if rope[j+1][0] < rope[j][0]:
                    rope[j+1][0] += 1
                else:
                    rope[j+1][0] -= 1          

            elif (abs(rope[j][1] - rope[j+1][1])) >= 2:
                if rope[j+1][1] < rope[j][1]:
                    rope[j+1][1] += 1
                else:
                    rope[j+1][1] -= 1   

        locations.add(tuple(rope[-1]))



print(len(locations))

