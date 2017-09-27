# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def Tostr(mystr):
            return [str(mystr[i]) for i in range(len(mystr))]

        l1str = Tostr(l1)
        l2str = Tostr(l2)

        def revstr(mystr):
            return [mystr[i] for i in reversed(range(len(mystr)))]

        l1revstr = revstr(l1str)
        l2revstr = revstr(l2str)
        outnum = int(''.join(l1revstr)) + int(''.join(l2revstr))
        outnum = str(outnum)
        return revstr(outnum)

    print addTwoNumbers(1, ['1', '9', '1', '9'], ['1', '2'])