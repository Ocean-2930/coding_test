# https://school.programmers.co.kr/learn/courses/30/lessons/340210
# 수식의 복원
def revmatch(a, b):
    ap = a
    bp = b
    if len(ap) > len(bp):
        bp = "0" * (len(ap) - len(bp)) + bp
    elif len(bp) > len(ap):
        ap = "0" * (len(bp) - len(ap)) + ap

    return (ap[::-1], bp[::-1])


def solution(expressions):
    pos = [2, 9]
    for l in expressions:
        for c in l:
            try:
                k = int(c)
                if pos[0] < k + 1:
                    pos[0] = k + 1
            except:
                pass
                
    algebra = [k.split(" ") for k in expressions]
    hint = [k for k in algebra if k[4] != "X"]
    lost = [k for k in algebra if k[4] == "X"]
    
    for l in hint:
        a, b = revmatch(l[0], l[2])
        c = l[4][::-1] + "0" * (len(a) - len(l[4]) if 0 < len(a) - len(l[4]) else 0)

        if l[1] == "+":
            for ind in range(len(a)):
                adigit = int(a[ind])
                bdigit = int(b[ind])
                cdigit = int(c[ind])
                if cdigit < adigit + bdigit:
                    k = adigit + bdigit - cdigit
                    pos = [k, k]
                    break
        else:
            for ind in range(len(a)):
                adigit = int(a[ind])
                bdigit = int(b[ind])
                cdigit = int(c[ind])
                if adigit - bdigit < 0:
                    k = cdigit - adigit + bdigit
                    pos = [k, k]
                    break

    answer = []

    if pos[0] == pos[1]:
        k = pos[0]
        for l in lost:
            a, b = revmatch(l[0], l[2])
            is_plus = l[1] == "+"
            c = ""
            f_bit = 0
            for ind in range(len(a)):
                adigit = int(a[ind])
                bdigit = int(b[ind])
                s = (adigit + bdigit + f_bit) if is_plus else (adigit - bdigit - f_bit)
                c = str((s+k)%k) + c
                f_bit = 1 if (is_plus and k <= s) or (not is_plus and s < 0) else 0                
            l[4] = str(int(str(f_bit) + c))
            answer.append(" ".join(l))

        return answer
            

    for l in lost:
        a, b = revmatch(l[0], l[2])
        is_plus = l[1] == "+"
        c = ""
        for ind in range(len(a)):
            adigit = int(a[ind])
            bdigit = int(b[ind])
            s = (adigit + bdigit) if is_plus else (adigit - bdigit)
            if 0 <= s < pos[0]:
                c = str(s) + c
            else:
                c = "?"
                break
        if c != "?":
            c = str(int(c))
        l[4] = c
        answer.append(" ".join(l))
        
    return answer

exps = ["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "8 + 4 = X"]
for line in solution(exps):
    print(line)

