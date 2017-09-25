class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return(''.join([s[i] for i in reversed(range(len(s))) ]))