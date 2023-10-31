f = open("Day 18 Input.txt", "r")

fileinput = f.read()

f.close()


#Day 1

cubes = fileinput.splitlines()



cube_points = set()



edges = set()


def find_edge(pa, pb, pc, px, py, pz, a, b, c, x, y, z):
    temp = [(pa + a, pb + b, pc + c), (px + x, py + y, pz + z)]
    temp.sort()
    return tuple(temp)

def test_edge(edge, edges):
    if edge in edges:
        return -1
    else:
        return 1
    
def test_edge_with_2(edge, edges1, edges2):
    if edge in edges:
        return -1
    elif edge in edges2:
        return 0
    else:
        return 1

def get_all_edges(pointsx, pointsy, pointsz):

    temp_edges = set()
    
    temp_edges.add(find_edge(pointsx, pointsy, pointsz, pointsx, pointsy, pointsz, 0.5, 0.5, 0.5, 0.5, -0.5, -0.5))

    
    temp_edges.add(find_edge(pointsx, pointsy, pointsz, pointsx, pointsy, pointsz, 0.5, 0.5, 0.5, -0.5, 0.5, -0.5))


    temp_edges.add(find_edge(pointsx, pointsy, pointsz, pointsx, pointsy, pointsz, 0.5, 0.5, 0.5, -0.5, -0.5, 0.5))


    temp_edges.add(find_edge(pointsx, pointsy, pointsz, pointsx, pointsy, pointsz, -0.5, -0.5, -0.5, 0.5, 0.5, -0.5))


    temp_edges.add(find_edge(pointsx, pointsy, pointsz, pointsx, pointsy, pointsz, -0.5, -0.5, -0.5, 0.5, -0.5, 0.5))


    temp_edges.add(find_edge(pointsx, pointsy, pointsz, pointsx, pointsy, pointsz, -0.5, -0.5, -0.5, -0.5, 0.5, 0.5))

    return temp_edges

total = 0

for i in cubes:
    points = i.split(",")
    points[0], points[1], points[2] = float(points[0]), float(points[1]), float(points[2])

    cube_points.add((points[0], points[1], points[2]))

    new_edges = get_all_edges(points[0], points[1], points[2])

    for edge in new_edges:
        total += test_edge(edge, edges)



    edges = edges.union(new_edges)


print(total)


#Day 2

def add_to_flood_fill(point, filled, fail_set):
    finished = False
    success = True
    flood_filled2 = filled.copy()
    new_flood_filled = set()
    if point in filled:
        return filled, True, fail_set
    if point in fail_set:
        return filled, False, fail_set
    flood_filled2.add(point)
    while not finished:
        finished = True
        new_flood_filled = set()
        for i in flood_filled2:
            new_possibility = (i[0] + 1, i[1], i[2])
            if new_possibility not in flood_filled2 and new_possibility not in cube_points:
                finished = False
                new_flood_filled.add(new_possibility)

            new_possibility = (i[0] - 1, i[1], i[2])
            if new_possibility not in flood_filled2 and new_possibility not in cube_points:
                finished = False
                new_flood_filled.add(new_possibility)


            new_possibility = (i[0], i[1] + 1, i[2])
            if new_possibility not in flood_filled2 and new_possibility not in cube_points:
                finished = False
                new_flood_filled.add(new_possibility)


            new_possibility = (i[0], i[1] - 1, i[2])
            if new_possibility not in flood_filled2 and new_possibility not in cube_points:
                finished = False
                new_flood_filled.add(new_possibility)


            new_possibility = (i[0], i[1], i[2] + 1)
            if new_possibility not in flood_filled2 and new_possibility not in cube_points:
                finished = False
                new_flood_filled.add(new_possibility)


            new_possibility = (i[0], i[1], i[2] - 1)
            if new_possibility not in flood_filled2 and new_possibility not in cube_points:
                finished = False
                new_flood_filled.add(new_possibility)

            if (i[0] not in range(1, 21) or i[1] not in range(1, 21) or i[2] not in range(1, 21)) or (i[0], i[1], i[2]) in fail_set:
                fail_set |= new_flood_filled - filled
                return flood_filled2, False, fail_set

        flood_filled2 |= new_flood_filled


    return flood_filled2, True, fail_set


flood_filled = set()

flood_filled_edges = set()

flood_filled, s, fails = add_to_flood_fill((10.0, 10.0, 10.0), flood_filled, set())

for i in cube_points:
    point = (i[0]+1, i[1], i[2])
    if point not in cube_points:
        filled, s, fails = add_to_flood_fill(point, flood_filled, fails)
        if s:
            flood_filled = filled
            
    point = (i[0]-1, i[1], i[2])        
    if point not in cube_points:
        filled, s, fails = add_to_flood_fill(point, flood_filled, fails)
        if s:
            flood_filled = filled
            
    point = (i[0], i[1]+1, i[2])
    if point not in cube_points:
        filled, s, fails = add_to_flood_fill(point, flood_filled, fails)
        if s:
            flood_filled = filled
            
    point = (i[0], i[1]-1, i[2])
    if point not in cube_points:
        filled, s, fails = add_to_flood_fill(point, flood_filled, fails)
        if s:
            flood_filled = filled
            
    point = (i[0], i[1], i[2]+1)
    if point not in cube_points:
        filled, s, fails = add_to_flood_fill(point, flood_filled, fails)
        if s:
            flood_filled = filled
            
    point = (i[0], i[1], i[2]-1)
    if point not in cube_points:
        filled, s, fails = add_to_flood_fill(point, flood_filled, fails)
        if s:
            flood_filled = filled



for i in flood_filled:
    temp_set = get_all_edges(i[0], i[1], i[2])

    flood_filled_edges |= temp_set
total = 0

edges = set()

to_be_removed = set()

for i in cubes:
    points = i.split(",")
    points[0], points[1], points[2] = float(points[0]), float(points[1]), float(points[2])

    new_edges = get_all_edges(points[0], points[1], points[2])

    for edge in new_edges:
        total += test_edge_with_2(edge, edges, flood_filled_edges)
        if test_edge(edge, edges) != 1:
            to_be_removed.add(edge)
        

    edges = edges.union(new_edges)


print(total)

