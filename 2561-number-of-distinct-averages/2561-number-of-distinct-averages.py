class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i, j = 0, len(nums) - 1
        averages = set()

        while i < j:
            avg = (nums[i] + nums[j]) / 2.0
            averages.add(avg)
            i += 1
            j -= 1

        return len(averages)
