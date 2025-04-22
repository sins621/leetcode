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


# class Solution(object):
#     def gcdOfStrings(self, str1, str2):
#         """
#         :type str1: str
#         :type str2: str
#         :rtype: str
#         """
#         len1, len2 = len(str1), len(str2)

#         def isDivisor(l):
#             if len1 % l or len2 % l:
#                 return False
#             (
#                 f1,
#                 f2,
#             ) = (
#                 len1 // l,
#                 len2 // l,
#             )
#             return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

#         for l in range(min(len1, len2), 0, -1):
#             if isDivisor(l):
#                 return str1[:l]
#         return ""


class Solution(object):
    def gcdOfStrings(self, str1, str2):
        len1, len2 = len(str1), len(str2)

        def isDivisor(l):
            if len1 % l == 0 and len2 % l == 0:
                f1, f2 = len1 // l, len2 // l
                return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        for l in range(min(len1, len2), 0, -1):
            if isDivisor(l):
                return str1[:l]
        return ""


solution = Solution()

test1 = solution.gcdOfStrings("ABCABC", "ABC")

if test1 == "ABC":
    print("Passed Case 1")
else:
    print(f"Case 1 Failed, output '{test1}', expected 'ABC'")

test2 = solution.gcdOfStrings("ABABAB", "ABAB")

if test2 == "AB":
    print("Passed Case 2")
else:
    print(f"Case 2 Failed, output '{test2}', expected 'AB'")

test3 = solution.gcdOfStrings("LEET", "CODE")

if test3 == "":
    print("Passed Case 3")
else:
    print(f"Case 3 Failed, output '{test3}', expected 'Null'")
