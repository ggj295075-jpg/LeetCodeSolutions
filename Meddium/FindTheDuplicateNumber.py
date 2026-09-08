# This is my solve therefor it not be the best.


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map = {}
        for i in range(len(nums)):
            if f"{nums[i]}" in map:
                return nums[i]
            map[f"{nums[i]}"] = nums[i]

        return 0
