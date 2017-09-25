import math
def BitCal(x):
    flag = 1
    out = []
    while flag:
        if x == 0:
            a = 0
            flag = 0
        else:
            a = int(math.log(x) / math.log(2))
            x = x - 2 ** a
            out.append(a)
    return out

print BitCal(420)