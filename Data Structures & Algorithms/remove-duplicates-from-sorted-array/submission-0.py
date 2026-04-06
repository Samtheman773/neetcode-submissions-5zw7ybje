class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) != 0:
            unique_elm = {}
            for num in nums:
                if num not in unique_elm:
                    unique_elm[num] = 1
                else:
                    continue
            return list(unique_elm)
        else:
            return 0

        