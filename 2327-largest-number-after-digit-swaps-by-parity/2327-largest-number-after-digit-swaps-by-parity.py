class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = list(str(num))
        odds = sorted([d for d in digits if int(d) % 2 == 1], reverse=True)
        evens = sorted([d for d in digits if int(d) % 2 == 0], reverse=True)

        result = []
        for d in digits:
            if int(d) % 2 == 0:
                result.append(evens.pop(0))  # Use next largest even
            else:
                result.append(odds.pop(0))   # Use next largest odd

        return int("".join(result))
