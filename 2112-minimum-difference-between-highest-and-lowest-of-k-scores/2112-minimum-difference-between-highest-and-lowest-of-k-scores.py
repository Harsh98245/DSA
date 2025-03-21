class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 1:
            return 0

        # Merge Sort function
        def MergeSort(nums):
            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2
            left = MergeSort(nums[:mid])
            right = MergeSort(nums[mid:])

            return merge(left, right)

        # Merging function
        def merge(left, right):
            i, j = 0, 0
            sorted_arr = []
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    sorted_arr.append(left[i])
                    i += 1
                else:
                    sorted_arr.append(right[j])
                    j += 1
            sorted_arr.extend(left[i:])
            sorted_arr.extend(right[j:])
            return sorted_arr

        # Sort the array using Merge Sort
        nums = MergeSort(nums)

        # Sliding window to find the minimum difference
        min_diff = float('inf')
        for i in range(len(nums) - k + 1):
            diff = nums[i + k - 1] - nums[i]
            min_diff = min(min_diff, diff)

        return min_diff

