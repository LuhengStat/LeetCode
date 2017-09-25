class Solution(object):
    import math
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
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

    print hammingDistance(1, 1, 4)
