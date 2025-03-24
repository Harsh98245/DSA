class Solution:
    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            self.merge_sort(left)
            self.merge_sort(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
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

    def minMovesToSeat(self, seats, students):
        # Sort both arrays first
        self.merge_sort(seats)
        self.merge_sort(students)

        # Now pair and compute total moves
        total_moves = 0
        for i in range(len(seats)):
            total_moves += abs(seats[i] - students[i])

        return total_moves
