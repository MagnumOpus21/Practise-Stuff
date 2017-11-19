from collections import defaultdict
import string


def compare(hashmaps2, hashmaps1):
    for a in string.ascii_lowercase:
        if hashmaps1[a] != hashmaps2[a]:
            return False
    return True


class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str1
        :type s2: str
        :rtype: bool
        """
        hashmaps1 = defaultdict(int)
        for index, letter in enumerate(s1):
            print(index,letter)
            hashmaps1[letter] += 1
        hashmaps2 = defaultdict(int)
        if len(s2) < len(s1):
            return False
        begin, ends, window = 0, 0, len(s1)
        for letter in s2:
            if ends - begin < window:
                hashmaps2[letter] += 1
                ends += 1
            else:
                if compare(hashmaps2, hashmaps1) == True:
                    return True
                else:
                    hashmaps2[s2[begin]] -= 1
                    begin += 1
                    hashmaps2[letter] += 1
                    ends += 1
        if compare(hashmaps2, hashmaps1) == True:
            return True
        print(hashmaps2,hashmaps1,sep="\n")
        return False


print(Solution().checkInclusion("abcdxabcde", "abcdeabcdx"))
