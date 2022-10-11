# Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

# Example 1:
# Input: n = 13
# Output: 6

# Example 2:
# Input: n = 0
# Output: 0

class Solution:
    def countDigitOne(self, n: int) -> int:
        if n < 10:
            return (min(1, n))
        l = len(str(n)) - 1
        dig = int(str(n)[0])
        rest = int(str(n)[1:])
        base = l * 10 ** (l - 1)
        if dig == 1:
            return base + rest + 1 + self.countDigitOne(rest)
        else:
            return 10 ** l + base * dig + self.countDigitOne(rest)
        return self.countDigitOne(n)
