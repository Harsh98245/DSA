class Solution:
    def majorityElement(self, nums):
        candidate = None  # No candidate at the start
        count = 0  # Initial count is 0

        # Iterate through each number in the list
        for num in nums:
            if count == 0:
                candidate = num  # Set the current number as the candidate
            count += (1 if num == candidate else -1)  # If it matches, increase count, else decrease

        return candidate  # The final candidate is the majority element
