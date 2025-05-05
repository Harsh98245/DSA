class Solution(object):
    def unequalTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    continue
                for k in range(j + 1, n):
                    if nums[k] != nums[i] and nums[k] != nums[j]:
                        count += 1

        return count
     