f = open("Day 4 Input.txt", "r")

fileinput = f.read()

f.close()


#Day 1

assignments = fileinput.splitlines()

total = 0

for i in assignments:
    assignment = i.split(",")

    assignment_one_ints = (int(assignment[0].split("-")[0]), int(assignment[0].split("-")[1]))

    assignment_two_ints = (int(assignment[1].split("-")[0]), int(assignment[1].split("-")[1]))

    assignment = [assignment_one_ints, assignment_two_ints]

    assignment.sort(key = lambda x: x[0] * 10000 + x[1])


    if assignment[0][0] == assignment[1][0]:
        total += 1

    elif assignment[1][1] <= assignment[0][1]:
        total += 1


    
print(total)    

    
#Day 2




total = 0

for i in assignments:
    assignment = i.split(",")

    assignment_one_ints = (int(assignment[0].split("-")[0]), int(assignment[0].split("-")[1]))

    assignment_two_ints = (int(assignment[1].split("-")[0]), int(assignment[1].split("-")[1]))

    assignment = [assignment_one_ints, assignment_two_ints]

    assignment.sort(key = lambda x: x[0] * 10000 + x[1])

    if assignment[0][1] >= assignment[1][0]:
        total += 1


    
print(total)    

