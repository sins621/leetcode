# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters.
# The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces
# between two words to a single space in the reversed string.

# Constraints

# 1 <= s.length <= 10^4
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.

# Requirements
# Should not contain leading or trailing spaces.
# Should reduce multiple spaces beween reversed srings

# Psuedo
# First use the strip() function to remove leading or trailing whitespaces
# if there is only one word return the word
# Use the split() function to split the string into an array of words, including whitespaces
# Use the reverse() function to reverse the array ()
# return the string by using the .join() function and joining the array to an empty string

# Problems
# Split does not retain the delimiter
# Solution: Add the delimiter after the fact, strip still removes
## Current Method removes white space between single letters
## Result of using "split"
# duplicate white space


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return " ".join(words[::-1])


solution = Solution()
print(solution.reverseWords("   the sky is blue   "))
