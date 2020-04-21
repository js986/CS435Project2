from Graph import GraphNode
import WeightedGraph
import random
import MinHeap
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
    minheap = MinHeap.MinHeap()
    distances = dict()
    distances[start] = 0
    current = start
    minheap.insert([start,0])
    while len(minheap.heap) > 0:
        current = minheap.extractMin()[0]
        for node in current.neighbors:
            if node[0] not in distances or distances[node[0]] > node[1]:
                distances[node[0]] = distances[current] + node[1]
                minheap.insert([node[0],distances[current] + node[1]])

    return distances


#Helper Functions


graph = createLinkedList(50)
print(dijkstras(graph.verticies[0]))
