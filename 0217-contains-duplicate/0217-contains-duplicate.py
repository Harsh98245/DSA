class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()  # Initialize an empty set
        for num in nums:
            if num in seen:  # If the number is already in the set, it's a duplicate
                return True
            seen.add(num)  # Add the current number to the set
        return False  # No duplicates were found
