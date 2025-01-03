class Solution(object):
    def lengthOfLongestSubstring(self, s):

        left = 0
        right = 0
        char_set = set()
        max_length = 0

        while right < len(s):
            if s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            else:
                char_set.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            
        return max_length

        