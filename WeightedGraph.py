from Graph import GraphNode
class WeightedGraph:
    def __init__(self):
        self.verticies = list()

    def addNode(self,nodeVal):
        node = DirectedGraph(nodeVal)
        self.verticies.append(node)

    def addWeightedEdge(self,first,second, edgeWeight):
        if first == None or second == None:
            print("One of the nodes is null")
            return
        first.neighbors.append([second,edgeWeight])

    def removeDirectedEdge(self,first,second):
        if first == None or second == None:
            print("One of the nodes is null")
            return
        for i in first.neighbors:
            if second in i:
                neighbors.remove(i)

    def getAllNodes(self):
        return self.verticies
