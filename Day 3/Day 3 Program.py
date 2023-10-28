f = open("Day 3 Input.txt", "r")

fileinput = f.read()

f.close()


#Day 1

rucksacks = fileinput.splitlines()

total = 0

for i in rucksacks:
    half_point = len(i) // 2

    first_compartment = i[:half_point]
    second_compartment = i[half_point:]

    copy = list(set(first_compartment).intersection(set(second_compartment)))[0]

    if ord(copy) < 93:
        total += ord(copy) - 38 #ord(A) is 65 so this makes it add 27 for A to 52 for Z

    else:
        total += ord(copy) - 96 #ord(a) is 97 so this makes it add 1 for a to 26 for z
print(total)



#Day 2




total = 0

for i in range(0, len(rucksacks), 3):
    copy = list(set(rucksacks[i]).intersection(set(rucksacks[i+1]).intersection(set(rucksacks[i+2]))))[0]

    if ord(copy) < 93:
        total += ord(copy) - 38 #ord(A) is 65 so this makes it add 27 for A to 52 for Z

    else:
        total += ord(copy) - 96 #ord(a) is 97 so this makes it add 1 for a to 26 for z


print(total)


