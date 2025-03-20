class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashmap = {}  # Initialize an empty hashmap
        
        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            complement = target - num  # Calculate the complement
            
            # Check if the complement is in the hashmap
            if complement in hashmap:
                return [hashmap[complement], i]  # Return the indices of the two numbers
            
            # If not, store the current number and its index in the hashmap
            hashmap[num] = i
        
        return []  # Return empty list if no solution found
