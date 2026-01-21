# https://school.programmers.co.kr/learn/courses/30/lessons/77887?language=python3
#중력 작용

class Node:
    def __init__(self, val):
        self.pNode = None
        self.cNode = []
        self.value = val

    def setParent(self, node):
        self.pNode = node

    def addChildren(self, node):
        self.cNode.append(node)

    def treeValue(self):
        res = self.value
        for n in self.cNode:
            res += n.treeValue()
        return res

    def upward(self, val):
        if self.pNode == None:
            self.value = val
            return

        self.value = self.pNode.value
        self.pNode.upward(val)
        

def solution(values, edges, queries):
    answer = []

    nodes = []
    for k in values:
        nodes.append(Node(k))

    for e in edges:
        nodes[e[0]-1].addChildren(nodes[e[1]-1])
        nodes[e[1]-1].setParent(nodes[e[0]-1])

    for q in queries:
        if q[1] == -1:
            answer.append(nodes[q[0]-1].treeValue())
        else:
            nodes[q[0]-1].upward(q[1])
    
    return answer

values = [1,10,100,1000,10000]
edges = [[1,2],[1,3],[2,4],[2,5]]
queries = [[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[4,1000],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[2,1],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1]]


print(solution(values, edges, queries))
