class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] += 1

        sorted_items = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)

        return [item[0] for item in sorted_items[:k]]

        
