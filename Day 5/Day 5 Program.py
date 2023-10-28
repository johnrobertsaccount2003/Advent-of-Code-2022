f = open("Day 5 Input.txt", "r")

fileinput = f.read().split("\n\n")

f.close()

# This is a stack
class Tower:
    def __init__(self):
        self.items = []
        self.hold = []

    def add(self, item):
        self.items.append(item)

    def pop(self):
        removed = self.items[-1]
        del self.items[-1]
        return removed

    def add_multi(self, item):
        self.hold.append(item)

    def finish_add_multi(self):
        self.items += self.hold[::-1]
        self.hold = []

#Day 1

structures = fileinput[0].splitlines()
del structures[-1]
structures = structures[::-1]
#Gets the input until "1   2   3" etc and cuts off that line
#Flips the towers so the item on the ground is the 1st one to be added to the stack


ins = fileinput[1].splitlines()

towers = []

for i in range(9):
    towers.append(Tower()) #Makes the 9 tower objects

for lines in structures:
    for i in range(0, len(lines), 4):
        if lines[i + 1] != " ": #If there actually an object here
            towers[i // 4].add(lines[i + 1])


for instruction in ins:
    parts = instruction.split(" ")
    #This completes the instruction by popping and add as the instruction says
    for i in range(int(parts[1])):
        towers[int(parts[5]) - 1].add(towers[int(parts[3]) - 1].pop())


for i in towers:
    print(i.pop(), end="")

print("")
        

#Day 2

towers = []

for i in range(9):
    towers.append(Tower()) #Makes the 9 tower objects

for lines in structures:
    for i in range(0, len(lines), 4):
        if lines[i + 1] != " ": #If there actually an object here
            towers[i // 4].add(lines[i + 1])


for instruction in ins:
    parts = instruction.split(" ")
    #This completes the instruction by popping and add as the instruction says
    for i in range(int(parts[1])):
        towers[int(parts[5]) - 1].add_multi(towers[int(parts[3]) - 1].pop())
    towers[int(parts[5]) - 1].finish_add_multi()

for i in towers:
    print(i.pop(), end="")

print("")



