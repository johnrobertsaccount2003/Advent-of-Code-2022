from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.graph import Graph
from pathfinding.core.node import Node
from pathfinding.finder.a_star import AStarFinder
from pathfinding.finder.dijkstra import DijkstraFinder
import networkx as nx

f = open("Day 12 Input.txt", "r")

fileinput = f.read().splitlines()

f.close()


#Day 1

start = (0, 0)
end = (2, 1)
edges = set()

a_nodes = set()

for y in range(len(fileinput)):
    for x in range(len(fileinput[0])):
        value = ord(fileinput[y][x])
        if value == ord("a"):
            a_nodes.add(y * 10000 + x)
        if fileinput[y][x] == "S":
            value = ord("a")
            start = (y, x)
        if fileinput[y][x] == "E":
            value = ord("z")
            end = (y, x)
        if x + 1 < len(fileinput[0]):
            to_go_to = ord(fileinput[y][x + 1])
            if to_go_to == ord("E"):
                to_go_to = ord("z")
            if value - to_go_to >= -1:
                edges.add(((y, x), (y, x + 1)))
        if x - 1 >= 0:
            to_go_to = ord(fileinput[y][x - 1])
            if to_go_to == ord("E"):
                to_go_to = ord("z")
            if value - to_go_to >= -1:
                edges.add(((y, x), (y, x - 1)))
        if y + 1 < len(fileinput):
            to_go_to = ord(fileinput[y + 1][x])
            if to_go_to == ord("E"):
                to_go_to = ord("z")
            if value - to_go_to >= -1:
                edges.add(((y, x), (y + 1, x)))
        if y - 1 >= 0:
            to_go_to = ord(fileinput[y - 1][x])
            if to_go_to == ord("E"):
                to_go_to = ord("z")
            if value - to_go_to >= -1:
                edges.add(((y, x), (y - 1, x)))

edges = list(edges)

print(edges)

nodes = set()

G = nx.DiGraph()


for i in range(len(edges)):
    nodes.add(edges[i][0][0] * 10000 + edges[i][0][1])
    nodes.add(edges[i][1][0] * 10000 + edges[i][1][1])


    edges[i] = (edges[i][0][0] * 10000 + edges[i][0][1], edges[i][1][0] * 10000 + edges[i][1][1])

for i in nodes:
    G.add_node(i)




G.add_edges_from(edges)



start_value = start[0] * 10000 + start[1]
end_value = end[0] * 10000 + end[1]

returns = nx.dijkstra_path(G, start_value, end_value)

print(returns, len(returns))
for i in range(len(returns)):
    print(i, returns[i])

##graph = Graph(edges=edges, bi_directional = False)
##finder = DijkstraFinder()
##start_value = start[1] * 10000 + start[0]
##end_value = end[0] * 10000 + end[1]
##print(start_value, end_value)
##path, runs = finder.find_path(graph.node(start_value), graph.node(end_value), graph)
##
##print(len(path))

#Day 2

path = nx.single_target_shortest_path(G, end_value)

mini = 999999
for i in path:
    print(i, len(path[i]), i in a_nodes)
    if len(path[i]) < mini and i in a_nodes:
        mini = len(path[i])
        print(path[i], i, mini)

print(mini - 1)
