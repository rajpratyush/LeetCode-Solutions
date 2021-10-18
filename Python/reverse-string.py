# Time:  O(n)
# Space: O(n)

class Solution(object):
    def reverseString(self, s):
        i = 0
        j = len(s) - 1
        while i < j and j > 0:
            s[i],s[j] = s[j], s[i]
            i += 1
            j -= 1
        return

# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

