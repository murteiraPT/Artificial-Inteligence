import math
import pickle
import time


class Node:
    def __init__(self, index):
        self.index = index
        self.parent = None
        self.transport = None

class Agent:
    def __init__(self, graph):
        self.graph = graph

    def returnFormat(self, nodeLeft, nodeRight):
        solution = []

        while nodeLeft is not None:
            if nodeLeft.transport is not None:
                solution.insert(0, [[nodeLeft.transport],[nodeLeft.index]])
            else:
                solution.insert(0, [[], [nodeLeft.index]])
            nodeLeft = nodeLeft.parent

        while nodeRight.parent is not None:
            solution.append([[nodeRight.transport], [nodeRight.parent.index]])
            nodeRight = nodeRight.parent
        return solution

    def BFS(self, source, goal, tickets):
        queue = []
        queueEnd = []
        queue.append(source)
        target = Node(goal)
        queueEnd.append(target)

        bateram = False

        intersection = []
        listOfWays = []

        while queue or queueEnd:
            s = queue.pop(0)
            t = queueEnd.pop(0)

            # if s.index == t.index:
            #     intersection.append([s, t])
            #     bateram = True

            for i in self.graph[s.index]:
                newNode = Node(i[1])
                newNode.parent = s
                newNode.transport = i[0]
                queue.append(newNode)
            '''
            for a in queue:
                for b in queueEnd:
                    if a.index == b.index:
                        intersection.append([a,b])
                        bateram = True
            '''

            for j in self.graph[t.index]:
                newNode = Node(j[1])
                newNode.parent = t
                newNode.transport = j[0]
                queueEnd.append(newNode)

            for a in queue:
                for b in queueEnd:
                    if a.index == b.index:
                        intersection.append([a,b])
                        bateram = True

            if bateram:
                for i in intersection:
                    listOfWays.append(self.returnFormat(i[0], i[1]))

                '''
                print("LIST OF WAYS")
                for i in listOfWays:
                    print (i)
                '''
                '''
                for i in listOfWays:
                    taxi = 0
                    bus = 0
                    metro = 0
                    for j in range (1, len(i)):
                        if i[j][0][0] == 0: taxi +=1
                        if i[j][0][0] == 1: bus +=1
                        if i[j][0][0] == 2: metro +=1
                    if tickets[0]>taxi and tickets[1]>bus and tickets[2]>metro:
                        return i
                '''
                return listOfWays


class SearchProblem:
    def __init__(self, goal, model, auxheur = []):
        self.graph = model
        self.goal = goal[0]
        self.heur = auxheur

    def search(self, init, limitexp = 2000, limitdepth = 10, tickets = [math.inf,math.inf,math.inf], anyorder=False):
        path = []

        currentnode = Node(init[0])
        neighbours = self.graph[currentnode.index]
        path = self.BFS(currentnode, self.goal, tickets)
        return path
