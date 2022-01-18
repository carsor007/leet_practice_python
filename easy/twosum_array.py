class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numHash = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in numHash:
                return [numHash[diff], i]
            numHash[n] = i
        return
