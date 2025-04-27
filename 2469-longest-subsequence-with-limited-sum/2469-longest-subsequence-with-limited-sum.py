import bisect

class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort()
        
        # Create prefix sum array
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        answer = []
        for query in queries:
            # Find the rightmost index where prefix sum <= query
            idx = bisect.bisect_right(prefix, query) - 1
            answer.append(idx)

        return answer
