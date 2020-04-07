
class GridNode:
    def __init__(self,x,y,value):
        self.x = x
        self.y = y
        self.value = value
        self.neighbors = list()

class GridGraph:
    def __init__(self):
        self.nodes = list()

    def addGridNode(self,x,y,nodeVal):
        node = GridNode(x,y,value)
        self.nodes.append(node)

    def addUndirectedEdge(self,first,second):
        if first == None or second == None:
            print("One of the nodes is null")
            return
        if first in second.neighbors and second in first.neighbors:
            #print("Nodes already share an edge")
            return
        if abs(first.x - second.x) == 1 and first.y == second.y:
            first.neighbors.append(second)
            second.neighbors.append(first)
        elif abs(first.y - second.y) == 1 and first.x == second.x:
            first.neighbors.append(second)
            second.neighbors.append(first)
        else:
            print("Given nodes are not neighbors")

    def removeUnDirectedEdge(self,first,second):
        if first == None or second == None:
            print("One of the nodes is null")
            return
        if second in first.neighbors and first in second.neighbors:
            first.neighbors.remove(second)
            second.neighbors.remove(first)

    def getNeighboringNodes(self,node):
        result = list()
        for i in self.nodes:
            if abs(i.x - node.x) == 1 and i.y == node.y:
                result.append(i)
            elif abs(i.y - node.y) == 1 and i.x == node.x:
                result.append(i)
        return result

    def getAllNodes(self):
        return self.nodes

    def printGridNode(self,node):
        print("(",node.x,",",node.y,")")
