import copy
from functools import lru_cache

f = open("Day 16 Input.txt", "r")

fileinput = f.read()

f.close()


#Day 1


lines = fileinput.splitlines()


valves = {}
matrix = {}
nodes = set()


for i in lines:
    words = []
    words = i.split(" ")
    if "valves" in i:
        connections = i.split("valves ")[1].split(", ")
    else:
        connections = i.split("valve ")[1].split(", ")
    valves[words[1]] = (int(words[4].split("=")[1][:-1]), connections)
    matrix[words[1]] = {words[1]: 0}




for i in valves:
    dist = 0
    while len(matrix[i]) < len(lines):
        dist += 1
        locations = set()
        for valve in matrix[i]:
            for j in valves[valve][1]:
                locations.add(j)

        for location in locations:
            if location not in matrix[i]:
                matrix[i][location] = dist



for i in list(matrix.keys()):
    if i != "AA" and valves[i][0] == 0:
        del matrix[i]
    else:
        for j in list(matrix.keys()):
            if j != "AA" and valves[j][0] == 0:
                del matrix[i][j]

for i in matrix:
    nodes.add(i)

nodes2 = copy.deepcopy(nodes)

def calc_score(node, time, current_score, unused_nodes):
    score = current_score
    for i in unused_nodes:
        if matrix[node][i] < time - 1 and i in unused_nodes:
            nodes_with_removed = unused_nodes.copy()
            nodes_with_removed.discard(i)
            score = max(score, calc_score(i, time - matrix[node][i] - 1, current_score + ((time - 1 - matrix[node][i]) * valves[i][0]), nodes_with_removed))
    return score


####print(calc_score("AA", 30, 0, nodes))
print("look here!!!!")
print(calc_score("AA", 26, 0, nodes))

#Day 2

print(valves)

print("\n\n")

for i in matrix:
    print(i, matrix[i])

print("\n\n")

print(len(nodes2))

cache = {}




def with_elephant(human, elephant, score, unused_nodes, time, hb, eb, move):
    
    score_copy = score
    c = 0
    for i in unused_nodes: #For human movement
        c += 1
        if time == 26:
            print(c, i)
        if matrix[human][i] < time - 1 and i != "AA":
            dist = matrix[human][i]
            time_loss = dist + 1
            score_loop = score
            nodes_with_removed = unused_nodes.copy()
            nodes_with_removed.discard(i)

            to_be_added = ((time + hb) - time_loss) * valves[i][0]
            new_human_bonus = max(0, hb - time_loss - eb)
            new_elephant_bonus = max(0, time_loss - hb)
            if new_human_bonus > 0:
                new_time = time
            else:
                new_time = (time + hb) - time_loss
            with_moves = with_elephant(i, elephant, score_loop + to_be_added, nodes_with_removed, new_time, new_human_bonus, new_elephant_bonus, "Human")
            score_copy = max(score_copy, with_moves)


    for i in unused_nodes: #For elephant movement
        c += 1
        if time == 26:
            print(c, i)
        if matrix[elephant][i] < time - 1 and i != "AA":
            dist = matrix[elephant][i]
            time_loss = dist + 1
            score_loop = score
            nodes_with_removed = unused_nodes.copy()
            nodes_with_removed.discard(i)
            to_be_added = ((time + eb) - time_loss) * valves[i][0]
            new_human_bonus = max(0, time_loss - eb)
            new_elephant_bonus = max(0, eb - time_loss - hb)
            if new_elephant_bonus > 0:
                new_time = time
            else:
                new_time = (time + eb) - time_loss
            with_moves = with_elephant(human, i, score_loop + to_be_added, nodes_with_removed, new_time, new_human_bonus, new_elephant_bonus, "Elephant")
            score_copy = max(score_copy, with_moves)




    return score_copy




print(with_elephant("AA", "AA", 0, nodes2, 26, 0, 0, "None"))


