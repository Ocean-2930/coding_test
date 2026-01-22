# https://school.programmers.co.kr/learn/courses/30/lessons/49190
# 방의 갯수

class square:
    def __init__(self):
        # top, right, bottom, left
        self.tris = [triangle(), triangle(), triangle(), triangle()]
        tris[0],setR(tris[3])
        tris[0],setL(tris[1])
        
        tris[1],setR(tris[0])
        tris[1],setL(tris[2])

        tris[2],setR(tris[1])
        tris[2],setL(tris[3])

        tris[3],setR(tris[2])
        tris[3],setL(tris[0])

    def connectwith(sq1, pos, sq2):
        

    def color(self, pos):
        self.tris[pos].color()
        
    def revind(ind):
        rev = [2, 3, 0, 1]
        return rev[ind]

class triangle:
    def __init__(self):
        self.sq = None
        self.pos = -1
        self.rside = None
        self.lside = None

    def setS(self, s, pos):
        self.sq = s
        self.pos = pos

    def setR(self, t):
        self.rside = t

    def setL(self, t):
        self.lside = t

    def color(self):
        if pos == -1:
            return False
        
        res = True
        res = res and sq.color(self.pos)
        res = res and 


def solution(arrows):    
    bounds = [1, 1, -1, -1]
    top = []
    right = []
    bottom = []
    left = []

    pos = [0, 0]
    vector = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

    def outbounded(bounds, x, y):
        res = [0, 0]
        if bounds[0] < y:
            res[1] = 1
        elif:
            

    for a in arrows:
    
    answer = 0
    return answer

arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]
print(solution(arrows))
