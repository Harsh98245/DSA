class Solution(object):
    def splitNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = sorted(str(num))  # Convert to string and sort digits
        num1, num2 = '', ''        # Initialize two number strings

        # Distribute digits alternately to form two numbers
        for i, d in enumerate(digits):
            if i % 2 == 0:
                num1 += d
            else:
                num2 += d

        # Convert to integers and return their sum
        return int(num1) + int(num2)
