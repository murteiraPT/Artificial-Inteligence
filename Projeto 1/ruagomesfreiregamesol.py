import math
import pickle
import time


class Node:
    def __init__(self, index):
        self.index = index
        self.parent = None
        self.transport = None
    
class SearchProblem:
    def __init__(self, goal, model, auxheur = []):
        self.graph = model
        self.goal = goal[0]
        self.heur = auxheur
    
    def returnFormat(self, node):
        solution = []

        while node is not None:
            if node.transport is not None:
                solution.insert(0, [[node.transport],[node.index]]) 
            else:
                solution.insert(0, [[], [node.index]])
            node = node.parent 

        print("solution: ", solution)
        return solution

    def search(self, init, limitexp = 2000, limitdepth = 10, tickets = [math.inf,math.inf,math.inf], anyorder=False):
        path = []

        currentnode = Node(init[0])
        print(currentnode.index)
        neighbours = self.graph[currentnode.index]
        path = self.BFS(currentnode, self.goal)
        return path

    def BFS(self, s, goal):
        queue = []
        queue.append(s)
        visited = []
        visited.append(s)

        while queue:
            s = queue.pop(0)
            if s.index == goal:
                return self.returnFormat(s)

            for i in self.graph[s.index]:
                newNode = Node(i[1])
                newNode.parent = s
                newNode.transport = i[0]
                queue.append(newNode)



 
  
