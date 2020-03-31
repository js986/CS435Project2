import Graph
from collections import deque
class GraphSearch:
    def DFSRec(self,start,end):
        visited = list()
        self.DFShelper(start,end,visited)
        return visited

    def DFShelper(self,start,end,visited):
        visited.append(start)
        for i in start.neighbors:
            if i == end:
                visited.append(end)
                return visited
            elif i not in visited:
                self.DFShelper(i,end,visited)


    def DFSIter(self,start,end):
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
        if end not in visited:
            return None
        return visited

    def BFTRec(self,graph):
        queue = deque()
        visited = list()
        for i in graph.verticies:
            if i not in visited:
                visited.append(i)
                queue.append(i)
                self.BFTHelper(graph,queue,visited)
        return visited

    def BFTHelper(self,graph,queue,visited):
        if len(queue) == 0:
            return visited
        if len(graph.verticies) == len(visited):
            return visited
        current = queue.popleft()
        for node in current.neighbors:
            if node not in visited:
                visited.append(node)
                queue.append(node)
        self.BFTHelper(graph,queue,visited)
        return None

    def BFTIter(self,graph):
        q = deque()
        visited = list()
        for vertex in graph.verticies:
            if vertex not in visited:
                visited.append(vertex)
                q.append(vertex)
            while len(q) > 0:
                current = q.popleft()
                for node in current.neighbors:
                    if node not in visited:
                        visited.append(node)
                        q.append(node)
        return visited
