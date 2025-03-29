class Solution(object):
    def mergesort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            self.mergesort(left)
            self.mergesort(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                # Sort in DESCENDING order
                if left[i] > right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

        return arr

    def maxSubsequence(self, nums, k):
        sorted_arr = self.mergesort(nums[:])  # Use a copy of nums ( IMPORTANT )
        topkval = sorted_arr[:k]  # Get k largest values

        result = []
        for num in nums:
            if num in topkval:
                result.append(num)
                topkval.remove(num)  # Remove once to handle duplicates
        return result
