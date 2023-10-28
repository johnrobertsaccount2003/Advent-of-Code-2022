f = open("Day 1 Input.txt", "r")

fileinput = f.read()

f.close()


#Day 1


biggest_elf = 0

elves = fileinput.split("\n\n")

for i in range(len(elves)):
    elves[i] = list(map(int, elves[i].splitlines()))


for i in elves:
    biggest_elf = max(biggest_elf, sum(i))

print(biggest_elf)



#Day 2



elves.sort(reverse = True, key = lambda x: sum(x))
biggest_3 = sum(elves[0]) + sum(elves[1]) + sum(elves[2])

print(biggest_3)
