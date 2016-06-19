class Solution(object):
    def longestPalindrome(self, s):
        substring = ""
        d = {}

        for i in range(len(s)):
            if s[i] in d:
                l = d[s[i]];
                l.append(i)
            else:
                d[s[i]] = [i]

        for k in d:
            l = d[k]
            if len(l) == 1:
                if len(substring) < 1:
                    substring = s[l[0]]
                continue
            for i in range(len(l)):
                if i >= len(l) - 1:
                    break
                if self.checkPalindrome(s, l[i], l[i+1]):
                    if len(substring) < l[i+1]-l[i]+1:
                        substring = s[l[i]:l[i+1]+1]
        return substring

    def checkPalindrome(self, s, i1, i2):
        while i1 <= i2:
            if s[i1] != s[i2]:
                return False
            i1 += 1
            i2 -= 1
            return True

test = Solution()
test_str = "123456787654567"
print "%s:%s" % (test_str, (test.longestPalindrome(test_str)))
test_str = "a"
print "%s:%s" % (test_str, (test.longestPalindrome(test_str)))
test_str = "cccaccc"
print "%s:%s" % (test_str, (test.longestPalindrome(test_str)))
