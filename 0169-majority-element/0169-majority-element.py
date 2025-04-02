class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0

        # Boyer-Moore Voting Algorithm
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
