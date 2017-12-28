def haimingDistance(x, y):

    import math
    def BitCal(x):
        # obtain the bitcal of a number
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

    xbit = BitCal(x)
    ybit = BitCal(y)

    Union = xbit[:]
    InterSec = []
    for i in ybit:
        if i not in xbit:
            Union.append(i)
        if i in xbit:
            InterSec.append(i)

    return len(Union) - len(InterSec)

print haimingDistance(1,4)