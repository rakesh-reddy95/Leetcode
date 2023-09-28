from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=Counter(nums)
        for key, value in zip(x.keys(), x.values()):
            if value==1:
                return key
