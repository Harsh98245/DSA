class Solution:
    def merge(self, nums1, m, nums2, n):
        # Set pointers for nums1, nums2, and the end of nums1
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        # Merge from the back
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If nums2 still has elements, place them in nums1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
