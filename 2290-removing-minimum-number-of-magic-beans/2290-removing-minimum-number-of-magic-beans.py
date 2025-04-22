class Solution(object):
    def minimumRemoval(self, beans):
        """
        :type beans: List[int]
        :rtype: int
        """
        beans.sort()
        total = sum(beans)
        min_removal = float('inf')

        for i in range(len(beans)):
            x = beans[i]
            remaining_bags = len(beans) - i
            kept_beans = x * remaining_bags
            removal = total - kept_beans
            min_removal = min(min_removal, removal)

        return min_removal

        