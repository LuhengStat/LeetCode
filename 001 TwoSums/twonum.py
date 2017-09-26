class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    a = [i, j]
                    return a
                    break
        return a


    test = [1, 2 ,4, 6 ,8]
    target = 12
    print twoSum(1, test, target)