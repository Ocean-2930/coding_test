# https://school.programmers.co.kr/learn/courses/30/lessons/214290
# 경사로의 개수

def solution(grid, d, k):
    d = d * k
    
    answer = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            answer += walk(grid, i, j, d, 0)
    
    return answer % (10**9 + 7)

def walk(grid, i1, i2, d, ind):
    if ind == len(d):
        return 1

    res = 0
    try:
        if grid[i1+1][i2] - grid[i1][i2] == d[ind]:
            res += walk(grid, i1+1, i2, d, ind + 1)
    except IndexError:
        pass
    
    try:
        if grid[i1][i2+1] - grid[i1][i2] == d[ind]:
            res += walk(grid, i1, i2+1, d, ind + 1)
    except IndexError:
        pass
    
    try:
        if grid[i1-1][i2] - grid[i1][i2] == d[ind]:
            res += walk(grid, i1-1, i2, d, ind + 1)
    except IndexError:
        pass
    
    try:
        if grid[i1][i2-1] - grid[i1][i2] == d[ind]:
            res += walk(grid, i1, i2-1, d, ind + 1)
    except IndexError:
        pass

    return res


grid = [[3, 4, 6, 5, 3], [3, 5, 5, 3, 6], [5, 6, 4, 3, 6], [7, 4, 3, 5, 0]]
d = [1, -2, -1, 0, 2]
k = 2

print(solution(grid, d, k))
