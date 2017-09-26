class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        out = []
        for i in range(n):
            temp = i+1
            tempout = ''
            if temp%3 == 0:
                tempout = 'Fizz'
            if temp%5 == 0:
                if tempout == '':
                    tempout = 'Buzz'
                else:
                    tempout = 'FizzBuzz'
            if tempout =='':
                tempout = str(temp)
            out.append(tempout)
        return out

    def fizzBuzz1(self, n):
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n + 1)]

    print fizzBuzz1(1, 2000)
    print fizzBuzz(1,  2000)