import  math
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        firstnum=max(nums)
        secondnum=max(nums)

        for i in nums:
            if i< firstnum:
                firstnum=i
            if i>firstnum:
                secondnum=min(i, secondnum)
            if i> secondnum:
                return True
        return False