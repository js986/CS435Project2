import random
import DirectedGraph
import Graph
from TopSort import TopSort

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


#Testing
ordering = TopSort.Kahns(createRandomDAGIter(1000))
fun = TopSort.mDFS(createRandomDAGIter(1000))
for node in fun:
    print(node.data)
