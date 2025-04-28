class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        paired = zip(heights, names)    # Create (height, name) pairs
        sorted_pairs = sorted(paired, reverse=True)  # Sort descending by height
        return [name for height, name in sorted_pairs]
