# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# For the purpose of this problem, we will return 0 when needle is an empty string.

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        if (haystack.find(needle) != -1):
            return haystack.find(needle)
        else:
            return -1