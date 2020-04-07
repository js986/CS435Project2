from GridGraph import GridGraph
import random
import sys

def createRandomGridGraph(n):
    graph = GridGraph()
    for y in range(0,n):
        for x in range(0,n):
            graph.addGridNode(x,y,0)

            adj = graph.getNeighboringNodes(graph.grid[y][x])
            for i in adj:
                rng = random.randint(1,100)
                if rng%2 == 0:
                    graph.addUndirectedEdge(graph.grid[y][x],i)

    return graph

def astar(sourceNode,destNode):
    path = list()
    distances = dict()
    current = sourceNode
    print(sourceNode.x, ",", sourceNode.y)
    distances[current] = findManhattanDistance(sourceNode,destNode)
    while current != destNode and current != None:
        path.append(current)
        #GridGraph().printGridNode(current)
        if len(current.neighbors) == 0:
            break
        for i in current.neighbors:
            if i not in path:
                distances[i] = findManhattanDistance(i,destNode)
        minvalue = sys.maxsize
        for j in distances.keys():
            if j not in path:
                if distances[j] < minvalue:
                    minvalue = distances[j]
                    current = j
        if current == path[-1]:
            break
    return path

def findManhattanDistance(p1,p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

graph = createRandomGridGraph(5)
"""
for i in graph.grid[0]:
    for j in i.neighbors:
        graph.printGridNode(j)
    print('\n')
"""
p = astar(graph.grid[0][0],graph.grid[4][4])
for i in p:
    graph.printGridNode(i)