from Graph import GraphNode


class DirectedGraph:
    def __init__(self):
        self.verticies = list()

    def addNode(self,nodeVal):
        node = DirectedGraph(nodeVal)
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
        for i in self.verticies:
            print(i.data)
        return self.verticies
