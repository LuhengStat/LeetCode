class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        NumDict = {}
        if len(nums) <= 1:
            return False
        else:
            for i in range(len(nums)):
                temp = target - nums[i]
                if temp in NumDict:
                    return [NumDict[temp], i]
                else:
                    NumDict[nums[i]] = i

    test = [1, 2 ,4, 6 ,8]
    target = 12
    print twoSum(1, test, target)