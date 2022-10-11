# You are given a 0-indexed array of unique strings words.

# A palindrome pair is a pair of integers (i, j) such that:

# 0 <= i, j < word.length,
# i != j, and
# words[i] + words[j] (the concatenation of the two strings) is a palindrome string.
# Return an array of all the palindrome pairs of words.
 
# Example 1:
# Input: words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]

# Example 2:
# Input: words = ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]

# Example 3:
# Input: words = ["a",""]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["a","a"]

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans =set()
        val_pos = {w:idx for idx,w in enumerate(words)}
        for i,word in enumerate(words):
            for j in range(len(word)+1):
                pref = word[:j] 
                suf = word[j:]
                inv_pref = pref[::-1]
                inv_suf = suf[::-1]
                if(pref==inv_pref):
                    if(inv_suf in val_pos and val_pos[inv_suf]!=i):ans.add((val_pos[inv_suf],i))
            
                if(suf==inv_suf):
                    if(inv_pref in val_pos and val_pos[inv_pref]!=i):ans.add((i,val_pos[inv_pref]))

        return [list(pair) for pair in ans]
