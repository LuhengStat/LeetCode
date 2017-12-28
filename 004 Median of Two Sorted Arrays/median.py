class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a = nums1 + nums2
        b = sorted(a)
        n = len(a)
        med = n/2
        if n % 2 == 0:
            out = (b[med-1] + b[med]) / 2.0
        else:
            out = b[med]
        return out

    print findMedianSortedArrays(1, [1, 2, 3], [1, 2])