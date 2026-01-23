# https://school.programmers.co.kr/learn/courses/30/lessons/250135?language=python3
# 아날로그 시계

def solution(h1, m1, s1, h2, m2, s2):
    time_s = h1 * 3600 + m1 * 60 + s1
    time_e = h2 * 3600 + m2 * 60 + s2

    deg_s = s1 * 720
    deg_m = m1 * 720 + s1 * 12
    deg_h = (h1 % 12) * 3600 + m1 * 60 + s1

    m_s = deg_m - deg_s
    h_s = deg_h - deg_s

    answer = 0
    if m_s < 0:
        answer -= 1
    if h_s < 0:
        answer -= 1

    
    for _ in range(time_e - time_s + 1):
        if m_s == 0 and h_s == 0:
            answer -= 1
        
        if m_s <= 0:
            m_s += 43200
            answer += 1
        m_s -= 708
        
        if h_s <= 0:
            h_s += 43200
            answer += 1
        h_s -= 719
    
    return answer


a = [0, 5, 30, 0, 7, 0]
b = [12, 0, 0, 12, 0, 30]
c = [0, 0, 0, 23, 59, 59]

print(solution(*c))
