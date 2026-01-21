# https://school.programmers.co.kr/learn/courses/30/lessons/214295
# 미로 주행 테스트

def solution(n, m, tests):
    answer = 0

    grid = []
    for i in range(m+1):
        line = []
        for j in range(n+1):
            line.append(0)
        grid.append(line)

    posval = 0
    for t in tests:
        coord = reachable(n, m, t[0], t[1], t[2])

        if t[3] == 1:
            posval += 1

        for c in coord:
            xp = c[0]
            yp = c[1]
            
            if t[3] == 0:                
                grid[yp][xp] = -1
            else:
                grid[yp][xp] += 1

    for i in range(m + 1):
        for j in range(n + 1):
            if grid[i][j] == posval:
                answer += 1
    
    return answer

def reachable(n, m, x, y, l):
    res = []

    for i in range(-l, l+1):
        lp = l - abs(i)
        for j in range(-lp, lp+1):
            xpos = x + i
            ypos = y + j
            if 0 <= xpos and xpos <= n and 0 <= ypos and ypos <= m:
                res.append([xpos, ypos])                
    
    return res


n = 300
m = 100
test = [[123, 28, 124, 1], [183, 22, 34, 0], [188, 81, 116, 1], [167, 53, 33, 0], [125, 55, 20, 0]]

print(solution(n, m, test))
