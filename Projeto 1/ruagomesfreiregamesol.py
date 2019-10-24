import math
import pickle
import time
from itertools import combinations


class Node:
    def __init__(self, index):
        self.index = index
        self.parent = None
        self.transport = None

class Agent:
    def __init__(self, graph, goal):
        self.graph = graph
        self.goal = goal
        self.init = None

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

    def BFS(self):
        queue = []
        queueEnd = []
        source = Node(self.init)
        queue.append(source)
        target = Node(self.goal)
        queueEnd.append(target)

        bateram = False

        intersection = []
        listOfWays = []

        numberOfFounded = 0

        counter = 0
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
                for i in intersection[counter:]:
                    counter+=1
                    myList = self.returnFormat(i[0], i[1])
                    listOfWays.append(myList)
                    if len(myList) > numberOfFounded:
                        numberOfFounded = len(myList)

            if numberOfFounded > 5:
                return listOfWays


class SearchProblem:
    def __init__(self, goal, model, auxheur = []):
        self.graph = model
        self.heur = auxheur
        self.agents = []
        for i in range(len(goal)):
            self.agents.append(Agent(self.graph, goal[i]))

    def prettyPrint(self, i, j, k):
        output = []





    def resolveListOfWays(self, listOfWays, tickets):
        '''
        for i in listOfWays:
        '''
        taxi = 0
        bus = 0
        metro = 0

        for j in range (1, len(listOfWays)):

            if [j][0] == 0: taxi +=1
            if [j][0] == 1: bus +=1
            if [j][0] == 2: metro +=1
        if tickets[0]>taxi and tickets[1]>bus and tickets[2]>metro:
            return listOfWays


    def verifyCombination(self, i, j, k, tickets):
        if not len(i) == len(j) == len(k):
            return False

        for x in range(1, len(i)):
            if not (i[x][1] != j[x][1] != k[x][1]):
                return False

        '''
        taxi = 0
        bus = 0
        metro = 0
        for x in range (1, len(i)):


        for j in range (1, len(i)):
            if i[j][0][0] == 0: taxi +=1
            if i[j][0][0] == 1: bus +=1
            if i[j][0][0] == 2: metro +=1
        if tickets[0]>taxi and tickets[1]>bus and tickets[2]>metro:
            return i
        '''

        return True

    def search(self, init, limitexp = 2000, limitdepth = 10, tickets = [math.inf,math.inf,math.inf], anyorder=False):
        listOfWays = []
        for i in range(len(init)):
            self.agents[i].init = init[i]
        for i in self.agents:
            listOfWays.append(i.BFS())

        if len(listOfWays) == 1:
            for i in listOfWays[0]:
                tmp = self.resolveListOfWays(i, tickets)
                if tmp is not None:
                    return tmp
        else:
            for i in listOfWays[0]:
                for j in listOfWays[1]:
                    for k in listOfWays[2]:
                        if self.verifyCombination(i, j, k, tickets):
                            print(i)
                            print(j)
                            print(k)
                            return self.prettyPrint(i, j, k)

        #comb = combinations([listOfWays[0], listOfWays[1], listOfWays[2]], 3)

        #DEBUG START
        for i in listOfWays:
            print("Agente Numero X:  ", len(i))
            for j in i:
                print (j)
        #DEBUG END

        return 0
        #return resolveListOfWays(listOfWays)
