f = open("Day 11 Input.txt", "r")

fileinput = f.read()

f.close()


#Day 1


monkey_info = {}

monkeys = fileinput.split("\n\n")


for i in monkeys:
    info = i.splitlines()
    monkey_number = int(info[0].split(" ")[1][0])
    monkey_items = info[1].split(" ")
    monkey_items = monkey_items[4:]
    final_monkey_items = []
    for item in monkey_items:
        if item.endswith(","):
            item = item[:-1]
        final_monkey_items.append(int(item))
    operation = info[2].split(" ")
    if operation[-1] != "old":
        operation = (operation[-2], int(operation[-1]))
    else:
        operation = (operation[-2], operation[-1])

    divisible = int(info[3].split(" ")[-1])
    yes = int(info[4].split(" ")[-1])
    no = int(info[5].split(" ")[-1])

    monkey_info[monkey_number] = [final_monkey_items, operation, divisible, yes, no, 0] #0 is the number of inspections per monkey

    
for game_round in range(20):
    for monkey in range(8):
        info = monkey_info[monkey]
        for item in info[0]:
            monkey_info[monkey][-1] += 1
            if info[1][0] == "+":
                item += info[1][1]
            
            elif info[1][1] == "old":
                item *= item
            else:
                item *= info[1][1]
            item = item // 3
            if item % info[2] == 0:
                monkey_info[info[3]][0].append(item)
            else:
                monkey_info[info[4]][0].append(item)
        info[0] = []

results = list(monkey_info.values())
print(results)
results.sort(reverse = True, key = lambda x : x[-1])
    
            
print(results[0][-1] * results[1][-1])



#Day 2



monkey_info = {}

monkeys = fileinput.split("\n\n")


for i in monkeys:
    info = i.splitlines()
    monkey_number = int(info[0].split(" ")[1][0])
    monkey_items = info[1].split(" ")
    monkey_items = monkey_items[4:]
    final_monkey_items = []
    for item in monkey_items:
        if item.endswith(","):
            item = item[:-1]
        final_monkey_items.append(int(item))
    operation = info[2].split(" ")
    if operation[-1] != "old":
        operation = (operation[-2], int(operation[-1]))
    else:
        operation = (operation[-2], operation[-1])

    divisible = int(info[3].split(" ")[-1])
    yes = int(info[4].split(" ")[-1])
    no = int(info[5].split(" ")[-1])

    monkey_info[monkey_number] = [final_monkey_items, operation, divisible, yes, no, 0] #0 is the number of inspections per monkey

total_divisor = 1
for i in monkey_info:
    total_divisor *= monkey_info[i][2]

print(total_divisor)
    
for game_round in range(10000):
    for monkey in range(8):
        info = monkey_info[monkey]
        for item in info[0]:
            monkey_info[monkey][-1] += 1
            if info[1][0] == "+":
                item += info[1][1]
            
            elif info[1][1] == "old":
                item *= item
            else:
                item *= info[1][1]
            item %= total_divisor
            if item % info[2] == 0:
                monkey_info[info[3]][0].append(item)
            else:
                monkey_info[info[4]][0].append(item)
        info[0] = []

results = list(monkey_info.values())
print(results)
results.sort(reverse = True, key = lambda x : x[-1])
    
            
print(results[0][-1] * results[1][-1])

