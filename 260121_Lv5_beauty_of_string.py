# https://school.programmers.co.kr/learn/courses/30/lessons/68938
# 문자열의 아름다움

def solution(s):
    answer = 0
    tot = len(s)
    for i in range(tot):
        c = s[i]
        for j in range(tot-i):
            beauty = j
            while 0 < beauty:
                if c == s[i + beauty]:
                    beauty -= 1
                else:
                    answer += beauty
                    break
    return answer


print(solution("hello"))
