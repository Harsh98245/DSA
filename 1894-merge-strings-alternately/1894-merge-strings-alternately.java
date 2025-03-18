class Solution {
    public String mergeAlternately(String word1, String word2) {

       int len1 = word1.length(), len2 = word2.length();
        char[] merged = new char[len1 + len2];
        int i, k = 0;

        // Merge characters in alternating order
        for (i = 0; i < Math.min(len1, len2); i++) {
            merged[k++] = word1.charAt(i);
            merged[k++] = word2.charAt(i);
        }

        for (; i < len1; i++) {
            merged[k++] = word1.charAt(i);
        }
        for (; i < len2; i++) {
            merged[k++] = word2.charAt(i);
        }

        return new String(merged);
    }
}