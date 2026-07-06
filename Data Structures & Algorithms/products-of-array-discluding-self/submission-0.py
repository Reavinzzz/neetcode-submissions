class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        
        for i in range(len(nums)):
            product = 1
            for j in range(0, i):
                product *= nums[j]

            for k in range(i + 1, len(nums)):
                product *= nums[k]
            result.append(product)
        return result