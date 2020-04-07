
class GridNode:
    def __init__(self,x,y,value):
        self.value = value
        self.x = x
        self.y = y
        self.neighbors = list()

class GridGraph:
    def __init__(self):
        self.grid = list()

    def addGridNode(self,x,y,nodeVal):
        if len(self.grid)-1 < y:
            for i in range(len(self.grid),y+1):
                self.grid.append([])
        if len(self.grid[y])-1 < x:
            for i in range(len(self.grid[y]),x+1):
                self.grid[y].append(None)
        self.grid[y][x] = GridNode(x,y,nodeVal)


    def addUndirectedEdge(self,first,second):
        if first == None or second == None:
            #print("One of the nodes is null")
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
        #else:
            #print("Given nodes are not neighbors")

    def removeUnDirectedEdge(self,first,second):
        if first == None or second == None:
            print("One of the nodes is null")
            return
        if second in first.neighbors and first in second.neighbors:
            first.neighbors.remove(second)
            second.neighbors.remove(first)

    def getNeighboringNodes(self,node):
        result = list()
        if len(self.grid[node.y])-1 >= node.x+1:
            result.append(self.grid[node.y][node.x+1])
        if node.x-1 >= 0:
            result.append(self.grid[node.y][node.x-1])
        if len(self.grid)-1 >= node.y+1:
            result.append(self.grid[node.y+1][node.x])
        if node.y-1 >= 0:
            result.append(self.grid[node.y-1][node.x])            
        return result

    def getAllNodes(self):
        return self.grid

    def printGridNode(self,node):
        if node is None:
            print(node)
        else:
            print("(",node.x,",",node.y,")")

    def printGrid(self):
        for i in self.grid:
            for j in i:
                self.printGridNode(j)
