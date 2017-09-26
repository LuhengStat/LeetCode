class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Remember = {}
        for i in range(len(nums)):
            if nums[i] in Remember:
                Remember[nums[i]] = 2
            else:
                Remember[nums[i]] = 1

        val = Remember.keys()
        for i in range(len(val)):
            temp = val[i]
            if Remember[temp] == 1:
                return temp

    print singleNumber(1, [1, 1, 2, 3, 2])


