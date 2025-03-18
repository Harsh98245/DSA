class Solution {
    public String gcdOfStrings(String str1, String str2) {
    
        // Check if the concatenation in both orders is equal, ensuring a common divisor exists
        if (!(str1 + str2).equals(str2 + str1)) {
            return "";
        }

        // Calculate GCD of the lengths manually without a helper function
        int a = str1.length(), b = str2.length();
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }

        // Return the substring from the start of str1 with length a (GCD of lengths)
        return str1.substring(0, a);
    }
}



