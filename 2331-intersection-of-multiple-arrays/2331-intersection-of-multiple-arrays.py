class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        # Start with the set of the first subarray
        common = set(nums[0])

        # Intersect with each subsequent subarray
        for row in nums[1:]:
            common &= set(row)

         #we have to use sorted algo rather than function   

        return sorted(common)
