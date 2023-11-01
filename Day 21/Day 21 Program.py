from sympy import *

f = open("Day 21 Input.txt", "r")

fileinput = f.read()

f.close()


#Day 1

monkeys = fileinput.splitlines()

instructions = {}

finished = {}

for i in monkeys:
    temp = i.split(" ")
    if i[6] not in map(str, range(10)):
        equation = """finished[\"""" + temp[1] + "\"]" + temp[2] + "finished[\"" + temp[3] + "\"]"
    else:
        equation = i.split(" ")[1]
        finished[temp[0][:-1]] = equation

    instructions[temp[0][:-1]] = equation

while True:
    for i in monkeys:
        temp = i.split(" ")
        temp[0] = temp[0][:-1]
        try:
            finished[temp[0]] = eval(instructions[temp[0]])
        except Exception as e:
            #print(instructions[temp[0]])
            #print(e)
            pass
    if "root" in finished:
        print(int(finished["root"]))
        break



#Day 2

monkeys = fileinput.splitlines()

instructions = {}

finished = {}

for i in monkeys:
    temp = i.split(" ")
    if "root" in temp[0]:
        conjoined = ""
        for j in temp[2]:
            if j not in ("+-/*"):
                conjoined += j
            else:
                conjoined += "="
        temp[2] = conjoined
    #print(temp)
    if "humn" in temp[0]:
        temp[1] = "x"
        x = symbols("x")
        #print(temp)
    if i[6] not in map(str, range(10)):
        equation = """finished[\"""" + temp[1] + "\"] " + temp[2] + " finished[\"" + temp[3] + "\"]"
    else:
        equation = temp[1]
        finished[temp[0][:-1]] = equation

    instructions[temp[0][:-1]] = equation

while True:
    for i in monkeys:
        temp = i.split(" ")
        temp[0] = temp[0][:-1]
        try:
            get = instructions[temp[0]]
            bits = get.split(" ")
            finished[temp[0]] = "(%s)%s(%s)" % (eval(bits[0]), bits[1], eval(bits[2]))
        except Exception as e:
            pass
    if "root" in finished:
        parts = finished["root"].split("=")
        answer = eval("solveset(Eq(%s, %s), x)" % (parts[0], parts[1]))
        for i in answer:
            print(int(i))
        break



