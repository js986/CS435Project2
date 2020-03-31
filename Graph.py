import collections

class GraphNode:
    def __init__(self,data):
        self.data = data
        self.neighbors = list()
        self.visited = False

    def setVisited(self):
        self.visited = True


class Graph:
    def __init__(self):
        self.verticies = list()

    def addNode(nodeVal):
        node = Graph(nodeVal)
        self.verticies.append(node)

    def addUndirectedEdge(self,node1,node2):
        if (node1 is None or node2 is None):
            print("One of the nodes does not exist")
            return
        node1.neighbors.append(node2)
        node2.neighbors.append(node1)

    def removeUndirectedEdge(self,node1,node2):
        if (node1 is None or node2 is None):
            print("One of the nodes does not exist")
            return
        node1.neighbors.remove(node2)
        node2.neighbors.remove(node1)
    def getAllNodes(self):
        for i in self.verticies:
            print(i.data)
        return self.verticies
