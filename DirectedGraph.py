from Graph import GraphNode


class DirectedGraph:
    def __init__(self):
        self.verticies = list()

    def addNode(self,nodeVal):
        node = GraphNode(nodeVal)
        self.verticies.append(node)

    def addDirectedEdge(self,first,second):
        if first == None or second == None:
            print("One of the nodes is null")
            return
        first.neighbors.append(second)

    def removeDirectedEdge(self,first,second):
        if first == None or second == None:
            print("One of the nodes is null")
            return
        first.neighbors.remove(second)

    def getAllNodes(self):
        return self.verticies
