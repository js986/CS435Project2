from GridGraph import *
import random

def createRandomGridGraph(n):
    graph = GridGraph()
    for y in range(0,n):
        for x in range(0,n):
            node = GridNode(x,y,0)
            graph.nodes.append(node)
    """
    for m in graph.nodes:
        adj = graph.getNeighboringNodes(node)
        for i in adj:
            if i not in m.neighbors:
                rng = random.randint(1,100)
                if rng%2 == 0:
                    graph.addUndirectedEdge(node,i)
    """
    return graph

def astar(sourceNode,destNode):
    path = list()
    distances = dict()
    current = sourceNode
    dict[current] = findManhattanDistance(sourceNode,destNode)
    while current != destNode:
        path.append(current)
        #for i in current.neighbors:
        #    if i not in path:
        #        if i not in distances or distances[i] >


    return

def findManhattanDistance(p1,p2):
    return abs(p1.x - p2.x) + abs(p1.y + p2.y)

graph = createRandomGridGraph(100)
for i in graph.getAllNodes():
    graph.printGridNode(i)

print(len(graph.nodes))
