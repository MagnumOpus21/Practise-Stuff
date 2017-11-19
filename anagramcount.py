import collections


def compare(hashpattern, hashstring):
    for a in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if hashstring[a] == hashpattern[a]:
            continue
        else:
            return False
    return True


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        flags = False
        hashstring = collections.defaultdict(int)
        hashpattern = collections.defaultdict(int)
        indices = []
        count = 0
        window = len(p)
        currentwindow = 0
        for a in p:
            hashpattern[a] += 1
        # iterate and find the number of anagrams
        for index, letter in enumerate(s):
            if (currentwindow < window):
                hashstring[letter] += 1
                currentwindow += 1
                # print(hashstring)
                continue
            else:
                # print(index, letter)
                flags = self.AnagramFoundAndIncrement(count, hashpattern, hashstring)
                if flags == True:
                    indices.append(index - window)
                    flags = False
                hashstring[s[index - window]] -= 1
                hashstring[s[index]] += 1
        flags = self.AnagramFoundAndIncrement(count, hashpattern, hashstring)
        if flags == True:
            indices.append(index - window + 1)
        # print("Count:{} Indices:{}".format(count, indices))
        return indices

    def AnagramFoundAndIncrement(self, count, hashpattern, hashstring):
        if compare(hashstring, hashpattern) == True:
            return True
        return False

    def incrementWindow(self, currentwindow):
        currentwindow += 1
        return currentwindow


Solution().findAnagrams('abab', 'ba')
