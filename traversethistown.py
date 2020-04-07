import random
import Graph
import GraphSearch
import DirectedGraph
from TopSort import TopSort
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
    num = random.randint(0,100000)
    graph = Graph.Graph()
    node = Graph.GraphNode(num)
    graph.verticies.append(node)
    for i in range(1,n):
        num = random.randint(0,100000)
        node = Graph.GraphNode(num)
        graph.verticies.append(node)
        graph.addUndirectedEdge(node,graph.verticies[-2])
    return graph

def BFTRecLinkedList(graph):
    gs = GraphSearch.GraphSearch()
    gs.BFTRec(graph)

def BFTIterLinkedList(graph):
    gs = GraphSearch.GraphSearch()
    gs.BFTIter(graph)

def createRandomDAGIter(n):
    rng = 0
    graph = DirectedGraph.DirectedGraph()
    for i in range(0,n):
        node = Graph.GraphNode(i)
        graph.verticies.append(node)
        rng = random.randint(0,len(graph.verticies)-1)
        if len(graph.verticies) > 1 and rng != node.data:
            graph.addDirectedEdge(node,graph.verticies[rng])
    return graph



ordering = TopSort.Kahns(createRandomDAGIter(1000))
for i in ordering:
    if (ordering.count(i) > 1):
        print("AHHHHHH")
#g = createRandomUnweightedGraphIter(2000)
#gs = GraphSearch.GraphSearch()
#h = gs.BFTRec(g)
#v = GraphSearch.GraphSearch.BFTIter(g)
#print(len(h))
#for i in h:
#    print(i.data)
#BFTRecLinkedList(createLinkedList(10000))
BFTIterLinkedList(createLinkedList(10000))
