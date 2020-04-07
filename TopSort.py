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
        if dgraph == None:
            print("No directed graph provided")
            return
        stack = list()
        visited = list()
        stack.append(start)
        visited.append(start)
        while len(stack) > 0:
            current = stack.pop()
            for i in current.neighbors:
                if i not in visited:
                    visited.append(i)
                    stack.append(i)
        return visited

    #Helper Methods
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
