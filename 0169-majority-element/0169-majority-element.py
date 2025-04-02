class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0

        # Boyer-Moore Voting Algorithm
        for num in nums:
            if count == 0:
                candidate = num
            if(candidate==num):
                count+=1
            else:
                count-=1

        return candidate
