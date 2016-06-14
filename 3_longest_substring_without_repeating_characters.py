class Solution(object):
	def lengthOfLongestSubstring(self, s):
		max_len = 0
		s_index_dict = {}
		index = 0

		for i in range(len(s)):
			if s[i] in s_index_dict:
				index = max(index, s_index_dict[s[i]] + 1)
			max_len = max(max_len, i - index + 1)
			s_index_dict[s[i]] = i

		return max_len

#test
test = Solution()
test_str = "abcabcbb"
print test_str + " max_len:%d\n" % (test.lengthOfLongestSubstring(test_str));
test_str = "bbbbb"
print test_str + " max_len:%d\n" % (test.lengthOfLongestSubstring(test_str));
test_str = "pwwkew"
print test_str + " max_len:%d\n" % (test.lengthOfLongestSubstring(test_str));
test_str = "asdgghfbdfghdfgh"
print test_str + " max_len:%d\n" % (test.lengthOfLongestSubstring(test_str));
test_str = "qwertyui234567ujwefghrty"
print test_str + " max_len:%d\n" % (test.lengthOfLongestSubstring(test_str));
test_str = "aab"
print test_str + " max_len:%d\n" % (test.lengthOfLongestSubstring(test_str));
test_str = "dvdf"
print test_str + " max_len:%d\n" % (test.lengthOfLongestSubstring(test_str));
test_str = "c"
print test_str + " max_len:%d\n" % (test.lengthOfLongestSubstring(test_str));
