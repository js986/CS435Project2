from Graph import GraphNode
import WeightedGraph
import random
import sys

def createRandomCompleteWeightedGraph(n):
    graph = WeightedGraph.WeightedGraph()
    for i in range(0,n):
        node = GraphNode(i)
        graph.verticies.append(node)
    for x in graph.verticies:
        for y in graph.verticies:
            rng = random.randint(0,sys.maxsize-1)
            if x != y:
                graph.addWeightedEdge(x,y,rng)
    return graph

def createLinkedList(n):
    graph = WeightedGraph.WeightedGraph()
    for i in range(0,n):
        node = GraphNode(i)
        if i > 0:
            graph.addWeightedEdge(graph.verticies[-1],node,1)
        graph.verticies.append(node)
    return graph

def dijkstras(start):
    distances = dict()
    paths = dict()
    visited = list()
    distances[start] = 0
    current = start
    while current not in visited:
        visited.append(current)
        for node in current.neighbors:
            if node[0] not in visited:
                if node[0] not in distances or distances[node[0]] > node[1]:
                    distances[node[0]] = distances[current] + node[1]
                    paths[node[0]] = current
        minvalue = sys.maxsize
        for distance in distances.keys():
            if distance not in visited:
                if distances[distance] < minvalue:
                    minvalue = distances[distance]
                    current = distance
    return distances

"""
graph = createRandomCompleteWeightedGraph(100)
lst = graph.getAllNodes()
counter = 0
for i in lst:
    counter+=1
    print(len(i.neighbors))
print(counter)
"""
"""
graph = createLinkedList(10)
lst = graph.getAllNodes()
for i in lst:
    print(len(i.neighbors))
"""

graph = createLinkedList(50)
print(dijkstras(graph.verticies[0]))
