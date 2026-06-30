class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        h_map = {}

        for i in range(len(s)):
            h_map[s[i]] = h_map.get(s[i], 0) + 1
            h_map[t[i]] = h_map.get(t[i], 0) - 1
        
        return all(v == 0 for v in h_map.values())

