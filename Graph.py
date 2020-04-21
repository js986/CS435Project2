import collections

class GraphNode:
    def __init__(self,data):
        self.data = data
        self.neighbors = list()
        self.visited = False



class Graph:
    def __init__(self):
        self.verticies = list()

    def addNode(self,nodeVal):
        node = GraphNode(nodeVal)
        self.verticies.append(node)

    def addUndirectedEdge(self,node1,node2):
        if (node1 is None or node2 is None):
            return
        if node1 in node2.neighbors or node2 in node1.neighbors:
            return
        node1.neighbors.append(node2)
        if node1 == node2:
            return
        node2.neighbors.append(node1)

    def removeUndirectedEdge(self,node1,node2):
        if (node1 is None or node2 is None):
            return
        node1.neighbors.remove(node2)
        node2.neighbors.remove(node1)
    def getAllNodes(self):
        return self.verticies
