from collections import deque

class MinHeap:
    def __init__(self):
        self.heap = deque()

    def insert(self,data):
        self.heap.append(data)
        nodepos = len(self.heap)-1
        if (nodepos > 0):
            parentpos = int((nodepos-1)/2)
            while nodepos > 0 and self.heap[parentpos][1] > self.heap[nodepos][1]:
                self.swap(parentpos,nodepos)
                nodepos = parentpos
                parentpos = int((nodepos-1)/2)

    def swap(self,firstpos, secondpos):
        if firstpos in range(0,len(self.heap)) and secondpos in range(0,len(self.heap)):
            temp = self.heap[firstpos]
            self.heap[firstpos] = self.heap[secondpos]
            self.heap[secondpos] = temp

    def findSmallestChild(self,pos):
        leftPos = pos*2+1
        rightPos = pos*2+2
        if leftPos < len(self.heap) and rightPos < len(self.heap):
            return leftPos if self.heap[leftPos][1] < self.heap[rightPos][1] else rightPos
        elif leftPos < len(self.heap):
            return leftPos
        else:
            return -10;

    def remove(self, data):
        if len(self.heap) == 0:
            return
        self.swap(data,len(self.heap)-1)
        self.heap.pop()
        minChildPos = self.findSmallestChild(data)
        while data < len(self.heap)-1 and self.heap[data][1] > self.heap[minChildPos][1] and minChildPos != -10:
            self.swap(data,minChildPos)
            data = minChildPos
            minChildPos = self.findSmallestChild(data)

    def getMin(self):
        min = self.heap[0]
        return min

    def extractMin(self):
        min = self.getMin()
        self.remove(0)
        return min
