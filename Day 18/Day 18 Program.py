f = open("Day 18 Input.txt", "r")

fileinput = f.read()

f.close()


#Day 1

cubes = fileinput.splitlines()

edges = []

def find_edge(pa, pb, pc, px, py, pz, a, b, c, x, y, z):
    temp = [(pa + a, pb + b, pc + c), (px + x, py + y, pz + z)]
    temp.sort()
    return temp
    

for i in cubes:
    points = i.split(",")
    points[0], points[1], points[2] = float(points[0]), float(points[1]), float(points[2])

    edges.append(find_edge(points[0], points[1], points[2], points[0], points[1], points[2], 0.5, 0.5, 0.5, 0.5, -0.5, -0.5))
    edges.append(find_edge(points[0], points[1], points[2], points[0], points[1], points[2], 0.5, 0.5, 0.5, -0.5, 0.5, -0.5))
    edges.append(find_edge(points[0], points[1], points[2], points[0], points[1], points[2], 0.5, 0.5, 0.5, -0.5, -0.5, 0.5))

    edges.append(find_edge(points[0], points[1], points[2], points[0], points[1], points[2], -0.5, -0.5, -0.5, 0.5, 0.5, -0.5))
    edges.append(find_edge(points[0], points[1], points[2], points[0], points[1], points[2], -0.5, -0.5, -0.5, 0.5, -0.5, 0.5))
    edges.append(find_edge(points[0], points[1], points[2], points[0], points[1], points[2], -0.5, -0.5, -0.5, -0.5, 0.5, 0.5))


total = 0

for i in edges:
    if edges.count(i) == 1:
        total += 1

print(total)


#Day 2

not_encased = 0

for i in range(0, len(edges), 6):
    encased = True
    for j in range(i, i + 6):
        if edges.count(i) == 1:
        



