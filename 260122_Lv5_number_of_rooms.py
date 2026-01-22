# https://school.programmers.co.kr/learn/courses/30/lessons/49190
# 방의 갯수

class triangle:
    def __init__(self):
        self.sq = None
        self.pos = -1
        self.rside = None
        self.lside = None
        self.colored = False
        self.result = True

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
        
        if colored:
            return self.result

        self.colored = True
        
        res = True
        if rside != None:
            res = res and rside.color()
        if lside != None:
            res = res and lside.color()

        if sq != None:
            res = res and sq.color(pos)
            self.result = res
            return res

        self.result = False
        return False

class square:
    def __init__(self):
        # top, right, bottom, left
        self.sqrs = [None, None, None, None]
        
        # top, right, bottom, left, /, \
        self.tris = []
        for _ in range(4):
            self.tris.append(triangle())
        self.tris[0].setR(self.tris[3])
        self.tris[0].setL(self.tris[1])
        
        self.tris[1].setR(self.tris[0])
        self.tris[1].setL(self.tris[2])

        self.tris[2].setR(self.tris[1])
        self.tris[2].setL(self.tris[3])

        self.tris[3].setR(self.tris[2])
        self.tris[3].setL(self.tris[0])

    def connectwith(sq1, pos, sq2):
        sq1.tris[pos].setS(sq2, square.revind(pos))
        sq1.sqrs[pos] = sq2
        sq2.tris[square.revind(pos)].setS(sq1, pos)
        sq2.sqrs[square.revind(pos)] = sq1

    def divide(self, k):
        try:
            self.tris[k].sq = None
        except IndexError:
            if k == 4:
                self.tris[0].setL(None)
                self.tris[1].setR(None)
                self.tris[2].setL(None)
                self.tris[3].setR(None)
            elif k == 5:
                self.tris[0].setR(None)
                self.tris[1].setL(None)
                self.tris[2].setR(None)
                self.tris[3].setL(None)

    def trycolor(self):
        res = 0
        for t in self.tris:
            if t.colored:
                continue
            res += 1 if t.color() else 0
        return res

        
    def color(self, pos):
        return self.tris[square.revind(pos)].color()
        
    def revind(ind):
        rev = [2, 3, 0, 1]
        return rev[ind]

def solution(arrows):    
    bounds = [1, 1,-1, -1]
    s00 = square()
    s01 = square()
    s10 = square()
    s11 = square()
    
    square.connectwith(s00, 1, s01)    
    square.connectwith(s10, 0, s00)   
    square.connectwith(s10, 1, s11)    
    square.connectwith(s01, 2, s11)
    
    top = [s00, s01]
    right = [s01, s11]
    bottom = [s11, s10]
    left = [s10, s00]
    squares = [s00, s01, s10, s11]

    current = s00
    pos = [0, 0]
    vector = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

    def outbounded(bounds, x, y):
        res = [0, 0]
        if bounds[1] < x + 1:
            res[0] = 1
        elif x - 1 < bounds[3]:
            res[0] = -1

        if bounds[0] < y + 1:
            res[1] = 1
        elif y - 1 < bounds[2]:
            res[1] = -1

        return res[0], res[1]

    def stackover(l, tar, r, d1, d2):
        newlist = []
        for ind, s in enumerate(tar):
            newsquare = square()
            if ind == 0:
                l.append(newsquare)
            else:
                print("hello")
                square.connectwith(newsquare, d1, newlist[-1])
            square.connectwith(newsquare, d2, s)
            if ind == len(tar)-1:
                r.insert(0, newsquare)
            newlist.append(newsquare)
        tar = newlist
            
    for a in arrows:
        pos[0] += vector[a][0]
        pos[1] += vector[a][1]
        
        bx, by = outbounded(bounds, pos[0], pos[1])
        print(f"{a} > {pos[0]}, {pos[1]} / extend to {bx}, {by}")
        
        buff = current
        if by == 1:
            stackover(left, top, right, 3, 2)
            bounds[0] += 1
            current = current.sqrs[0]
        elif by == -1:
            stackover(right, bottom, left, 1, 0)
            bounds[2] += 1
            current = current.sqrs[2]
        if bx == 1:
            stackover(top, right, bottom, 0, 3)
            bounds[1] += 1
            current = current.sqrs[1]
        elif bx == -1:
            stackover(bottom, left, top, 2, 1)
            bounds[3] += 1
            current = current.sqrs[3]
            
        if a == 0:
            buff.divide(1)
            buff.sqrs[1].divide(3)
        elif a == 1:
            buff.sqrs[1].divide(4)
        elif a == 2:
            buff.sqrs[1].divide(2)
            buff.sqrs[1].sqrs[3].divide(0)
        elif a == 3:
            buff.sqrs[1].sqrs[3].divide(5)
        elif a == 4:
            buff.sqrs[2].divide(1)
            buff.sqrs[2].sqrs[1].divide(3)
        elif a == 5:
            buff.sqrs[2].divide(4)
        elif a == 6:
            buff.divide(2)
            buff.sqrs[2].divide(0)
        elif a == 7:
            buff.divide(5)
    
    answer = 0
    for s in left:
        sbuff = s
        while sbuff.sqrs[1] != None:
            answer += sbuff.trycolor()
            sbuff = sbuff.sqrs[1]
    return answer

arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]
print(solution(arrows))
