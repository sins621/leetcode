# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t
# (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""


# Constraints:

# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.


class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        str1_divs = []
        str2_divs = []

        str1_divs = [str1[i:] for i in range(0, len(str1) - 1)][::-1]
        str2_divs = [str2[i:] for i in range(0, len(str2) - 1)][::-1]


        for div in str1_divs:
            if div in str2_divs:
                return div

        for div in str2_divs:
            if div in str1_divs:
                return div


solution = Solution()
print(solution.gcdOfStrings("ABCABC", "ABC"))
