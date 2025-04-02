class Solution(object):
    
    def merge_sort(self,arr):
        if len(arr)>1:
            mid=len(arr)//2
            right=arr[mid:]
            left=arr[:mid]

            self.merge_sort(left)
            self.merge_sort(right)

            i=j=k=0

            while i < len(left) and j < len(right):
                # Sort in DESCENDING order
                if left[i] <= right[j]:
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

    def targetIndices(self, nums, target):
        result=[]

        sorted_arr=self.merge_sort(nums[:])
        # Iterate over sorted array and collect indices of target
        for i in range(len(sorted_arr)):
            if sorted_arr[i] == target:
                result.append(i)

        return result    
            

        