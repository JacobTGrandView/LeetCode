class Solution(object):
    def maximumWealth(self, accounts):
        richest = 0
        for i in accounts:
            if sum(i) > richest:
                richest = sum(i)
        return richest
        