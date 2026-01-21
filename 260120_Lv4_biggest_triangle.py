# https://school.programmers.co.kr/learn/courses/30/lessons/389629
# 가장 큰 삼각형 덩어리 문제

def solution(grid):
    N = len(grid)
    M = len(grid[0])
    
    mask = []
    for i in range(N):
        line = []
        for j in range(M):
            line.append([0, 0])
        mask.append(line)
    
    answer = 0
    for i in range(N):
        for j in range(M):
            a = map(grid, mask, j, i, 0)
            b = map(grid, mask, j, i, 1)
            if answer < a:
                answer = a
            if answer < b:
                answer = b
            
    return answer

def map(grid, mask, sx, sy, ind):  
    if mask[sy][sx][ind] == 1:
        return 0
    
    mask[sy][sx][ind] = 1
    k = 1
    
    """
    linked triangles
    
    grid value      index
    / = 1           0/1
    \\ = -1          1\\0
    
    vector index = grid + 1 + index
    
    the triangle is linked to:
    [top, right, down, left]
    """
    vectors = [
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0]
    ]
    
    vec = vectors[grid[sy][sx] + 1 + ind]
    if vec[0] == 1 and safeIndex(grid, sx, sy - 1):
        k += map(grid, mask, sx, sy - 1, 1)
    if vec[1] == 1 and safeIndex(grid, sx + 1, sy):
        newind = 1 if grid[sy][sx] == -1 else 0
        k += map(grid, mask, sx + 1, sy, newind)
    if vec[2] == 1 and safeIndex(grid, sx, sy + 1):
        k += map(grid, mask, sx, sy + 1, 0)
    if vec[3] == 1 and safeIndex(grid, sx - 1, sy):
        newind = 1 if grid[sy][sx] == 1 else 0
        k += map(grid, mask, sx - 1, sy, newind)
    
    return k

def safeIndex(grid, sx, sy):
    if sy < 0 or len(grid) <= sy:
        return False
    if sx < 0 or len(grid[0]) <= sx:
        return False
    return True

grid = [
     [1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1],
     [1, 1, -1, 1, -1, -1],
     [1, 1, 1, 1, -1, -1],
     [1, 1, 1, 1, -1, -1]
]

print(solution(grid))
