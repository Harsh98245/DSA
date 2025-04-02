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
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        valid_integers = set()  # To store unique integers

        # Loop over all triplet combinations using 3 nested loops
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    # Make sure all three indices are different to form a valid 3-digit number
                    if i != j and j != k and i != k:
                        num = digits[i] * 100 + digits[j] * 10 + digits[k]
                        
                        # Check if the number is even and does not have leading zero
                        if num % 2 == 0 and digits[i] != 0:
                            valid_integers.add(num)

        # Return the sorted list of valid integers
        return self.merge_sort(list(valid_integers))



        