import random
import Graph
import GraphSearch
import DirectedGraph
import sys
def createRandomUnweightedGraphIter(n):
    rng = 0
    graph = Graph.Graph()
    for i in range(0,n):
        node = Graph.GraphNode(i)
        graph.verticies.append(node)
        rng = random.randint(0,len(graph.verticies)-1)
        if len(graph.verticies) > 1:
            graph.addUndirectedEdge(node,graph.verticies[rng])
    return graph

def createLinkedList(n):
    graph = Graph.Graph()
    for i in range(0,n):
        num = random.randint(0,100000)
        graph.addNode(num)
        if i > 0:
            graph.addUndirectedEdge(graph.verticies[-1],graph.verticies[-2])
    return graph

def BFTRecLinkedList(graph):
    gs = GraphSearch.GraphSearch()
    gs.BFTRec(graph)

def BFTIterLinkedList(graph):
    gs = GraphSearch.GraphSearch()
    gs.BFTIter(graph)



BFTIterLinkedList(createLinkedList(10000))
