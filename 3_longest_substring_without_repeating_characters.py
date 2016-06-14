class Solution(object):
	def lengthOfLongestSubstring(self, s):
		max_len = 0
		s_index_dict = {}
		s_len_dict = {}
		
		for i in range(len(s)):
			key = s[i]
			#match the same char
			if not key in s_index_dict:
				s_len_dict[key] = 0
				s_index_dict[key] = i
			else:
				match_str_len = i - s_index_dict[key]
				if match_str_len > max_len:
					max_len = match_str_len
				
				#delete useless information after the matching
				will_del = []
				for s_tmp in s_len_dict:
					s_len = i - s_index_dict[s_tmp]
					if s_len > max_len:
						max_len = s_len
					if s_index_dict[s_tmp] < s_index_dict[key]:
						will_del.append(s_tmp)
				for s_tmp in will_del:
					del s_len_dict[s_tmp]
					del s_index_dict[s_tmp]

				s_len_dict[key] = match_str_len
				s_index_dict[key] = i

		#end of the match
		for key in s_len_dict:
			s_len = len(s) - s_index_dict[key]
			if s_len > max_len:
				max_len = s_len

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
