f = open("Day 10 Input.txt", "r")

fileinput = f.read()

f.close()



#Days 1 and 2



text = ""

to_execute = [[] for i in range(1)]

x = 1

total = 0

instructions = fileinput.splitlines()

cycle = 0

current = 0

while current < len(instructions) or not all(map(lambda x: len(x) == 0, to_execute)):
    if current < len(instructions):
        i = instructions[current]

    cycle += 1

    if abs(((cycle - 1) % 40) - x) <= 1:
        text += "#"

    else:
        text += "."
    

    if (cycle - 20) % 40 == 0:
        total += cycle * x

    
    if all(map(lambda x: len(x) == 0, to_execute)): #If to_execute is completely empty
        if i.startswith("addx"):

            to_execute[0].append(("addx", int(i.split(" ")[1])))
        current += 1
            


    else:

        if to_execute[0][0][0] == "addx":
            x += to_execute[0][0][1]


        for i in range(len(to_execute) - 1):
            to_execute[i] = to_execute[i + 1]

        to_execute[-1] = []



current_outputting = 0

while current_outputting < len(text):
    print(text[current_outputting], end = "")
    current_outputting += 1
    if current_outputting % 40 == 0:
        print("")


    
print(total)






