class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0

        is_negative = num < 0
        digits = list(str(abs(num)))

        if is_negative:
            # Sort digits in descending order for negative numbers
            digits.sort(reverse=True)
            return -int(''.join(digits))
        else:
            # Sort digits in ascending order for positive numbers
            digits.sort()
            # Find first non-zero digit and move it to the front
            for i in range(len(digits)):
                if digits[i] != '0':
                    digits[0], digits[i] = digits[i], digits[0]
                    break
            return int(''.join(digits))

        