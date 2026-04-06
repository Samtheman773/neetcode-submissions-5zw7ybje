class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = set()
        seenTwo = set()

        for ch in s:
            seen.add(ch)
        for x in t:
            seenTwo.add(x)

        if seen == seenTwo:
            return True
        else:
            return False
        
        