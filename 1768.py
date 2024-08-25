class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) < len(word2):
            a = 0
            length = len(word1)
        else:
            a = 1
            length = len(word2)
        newword = ""
        for i in range(0, length):
            newword = newword + word1[i] + word2[i]
        if a == 0:
            newword = newword + word2[length:]
        else:
            newword = newword + word1[length:]
        return newword
