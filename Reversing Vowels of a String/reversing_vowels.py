class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        v = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"] # convert to set for x2 perf
        l = []

        for c in s:
            if c in v:
                l.append(c)

        i = len(l)

        for j in range(0, len(s)):
            if s[j] in v:
                s[j] = l[i - 1]
                i -= 1

        return "".join(s)

# Better Solution
# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         s = list(s)
#         vowels = {'a','e','i','o','u','A','E','I','O','U'}
#         left, right = 0, len(s) - 1
#         while left < right:
#             if s[left] not in vowels:
#                 left += 1
#             elif s[right] not in vowels:
#                 right -= 1
#             else:
#                 s[left], s[right] = s[right], s[left]
#                 left += 1
#                 right -= 1
#         return ''.join(s)

solution = Solution()
print(solution.reverseVowels("leetcode"))
