import math
import pickle
import time


class SearchProblem:
    def __init__(self, goal, model, auxheur = []):
        self.graph = model
        self.goal = goal[0]
        self.heur = auxheur

    def search(self, init, limitexp = 2000, limitdepth = 10, tickets = [math.inf,math.inf,math.inf]):
        path = []

        currentnode = init[0]
        neighbours = self.graph[currentnode]

        self.BFS(currentnode, self.goal);

        return path

    def BFS(self, s, goal):
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print (s, end = " ")
            if s == goal:
                break

##            self.graph[s].sort(key = self.takeSecond, reverse = True)

            for i in self.graph[s]:
                if visited[i[1]] == False:
                    queue.append(i[1])
                    visited[i[1]] = True

    ##def takeSecond(self, elem):
    ##    return elem[1]
