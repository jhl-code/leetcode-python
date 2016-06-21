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
            max_len = 0
            for i in range(len(l)):
                if max_len >= len(s) - l[i]:
                    break
                if i >= len(l) - 1:
                    break
                for j in range(i+1, len(l))[::-1]:
                    if max_len >= l[j]-l[i]+1:
                        break
                    if self.checkPalindrome(s, l[i], l[j]):
                        if len(substring) < l[j]-l[i]+1:
                            substring = s[l[i]:l[j]+1]
                            max_len = l[j]-l[i]+1
                        break
        return substring

    def checkPalindrome(self, s, i1, i2):
        if s[i1:i2+1][::-1] == s[i1:i2+1]:
            return True
        else:
            return False

test = Solution()
test_str = "123456787654567"
print "%s:%s" % (test_str, (test.longestPalindrome(test_str)))
test_str = "a"
print "%s:%s" % (test_str, (test.longestPalindrome(test_str)))
test_str = "cccaccc"
print "%s:%s" % (test_str, (test.longestPalindrome(test_str)))
test_str = "aaabaaaa"
print "%s:%s" % (test_str, (test.longestPalindrome(test_str)))
test_str = "aaaabaaa"
print "%s:%s" % (test_str, (test.longestPalindrome(test_str)))
test_str = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"
print "%s:%s" % (test_str, (test.longestPalindrome(test_str)))
test_str = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
print "%s:%s" % (test_str, (test.longestPalindrome(test_str)))
test_str = "tembwxtvddsttolegryohdlhxhycymqybzfzcbkzdwcekzfapmpfyeivfoeeqoqdhylziqpnyzuzeeutpqpalbddlliuehvkhqevgjdkskvphidcjmpcmetzwqkzcnxjcjywhfzplntbkuddmbcovearburjqyirbladcrhfkfdfgsmyhdsfmmxmslwkymkgaguilxghmfgaldcogtfnbqakctqtqakupwrxkmbjpmzqngwldmaugzizgwmediyzxevspxdwruyzrmnhchtxlgtb"
print "%s:%s" % (test_str, (test.longestPalindrome(test_str)))

