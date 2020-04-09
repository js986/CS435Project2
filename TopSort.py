from DirectedGraph import DirectedGraph
from collections import deque
class TopSort:
    def Kahns(dgraph):
        if dgraph == None:
            print("No directed graph provided")
            return
        inDegrees = list()
        for node in dgraph.verticies:
            inDegrees.append(TopSort.findInDegree(dgraph,node))
        queue = deque()
        ordering = list()
        for i in range(0,len(inDegrees)):
            if inDegrees[i] == 0:
                queue.append(dgraph.verticies[i])
        while len(queue) > 0:
            current = queue[0]
            ordering.append(current)
            for j in current.neighbors:
                indx = dgraph.verticies.index(j)
                inDegrees[indx]-=1
                if inDegrees[indx] == 0:
                    queue.append(j)
            queue.popleft()
        return ordering



    def mDFS(dgraph):
        stack = list()
        for vertex in dgraph.verticies:
            TopSort.mDFShelper(vertex,stack)
        stack.reverse()
        return stack

    #Helper Methods
    def mDFShelper(current,stack):
        current.visited = True
        for i in current.neighbors:
            if i.visited == False:
                TopSort.mDFShelper(i,stack)
        stack.append(current)

    def findInDegree(graph,node):
        if node not in graph.verticies:
            print("Given node is not in graph")
            return -1
        inDegree = 0
        for i in graph.verticies:
            if i == node:
                continue
            if node in i.neighbors:
                inDegree+=1
        return inDegree
