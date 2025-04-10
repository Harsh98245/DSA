class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits=[]
        for digit in str(num):
            digits.append(int(digit))

        digits.sort()
        new1=0
        new2=0

        for i in range(len(digits)):
            if i % 2 == 0:
                new1 = new1 * 10 + digits[i]  # Add digit to new1
            else:
                new2 = new2 * 10 + digits[i] 

        return new1+new2 

    