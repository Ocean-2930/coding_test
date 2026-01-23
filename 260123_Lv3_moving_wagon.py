# https://school.programmers.co.kr/learn/courses/30/lessons/250134
# 수레 움직이기



def routeA(maze, route, x, y, l):
    try:
        if maze[x][y] == 5:
            return
    except:
        return

    if route[x][y] != -1 and route[x][y] <= l:
        return

    route[x][y] = l

    if maze[x][y] == 3:
        return

    routeA(maze, route, x + 1, y, l + 1)
    routeA(maze, route, x + 1, y, l + 1)
    routeA(maze, route, x, y + 1, l + 1)
    routeA(maze, route, x, y - 1, l + 1)

def routeB(maze, his, route, x, y, l):
    try:
        if maze[x][y] == 5:
            return
    except:
        return

    if his[x][y] == l:
        return

    if route[x][y] != -1 and route[x][y] <= l:
        return
    
    route[x][y] = l

    if maze[x][y] == 4:
        return

    routeB(maze, his, route, x + 1, y, l + 1)
    routeB(maze, his, route, x - 1, y, l + 1)
    routeB(maze, his, route, x, y + 1, l + 1)
    routeB(maze, his, route, x, y - 1, l + 1)

def solution(maze):
    # 1 ~ 4 빨간 수레 시작, 파란 수레 시작, 빨간 수레 도착, 파란 수레 도착
    points = [0, 0, 0, 0]

    r1 = []
    history = []
    r2 = []

    for i in range(len(maze)):
        rl1 = []
        hl = []
        rl2 = []
        for j in range(len(maze[0])):
            rl1.append(-1)
            hl.append(-1)
            rl2.append(-1)
            if 1 <= maze[i][j] <= 4:
                points[maze[i][j] - 1] = (i, j)
        r1.append(rl1)
        history.append(hl)
        r2.append(rl2)

    routeA(maze, r1, points[0][0], points[0][1], 0)
    
    cp = [points[2][0] - 1, points[2][1]]
    k = r1[cp[0]][cp[1]]
    history[cp[0]][cp[1]] = r1[cp[0]][cp[1]]

    while 0 <= k:
        vec = [(1, 1), (1, -1), (-1, 1), (-1, -1)]        
        for v in vec:
            try:
                if r1[cp[0]+v[0]][cp[1]+v[1]] == k - 1:
                    cp[0] += v[0]
                    cp[1] += v[1]
                    break
            except:
                pass
        history[cp[0]][cp[1]] = r1[cp[0]][cp[1]]
        k -= 1
        
    routeB(maze, history, r2, points[1][0], points[1][1], 0)

    if r2[points[3][0]][points[3][1]] == -1:
        return 0
    
    return max(r1[points[2][0]][points[2][1]], r2[points[3][0]][points[3][1]])

maze = [[1, 0, 2], [0, 0, 0], [5, 0 ,5], [4, 0, 3]]
print(solution(maze))
