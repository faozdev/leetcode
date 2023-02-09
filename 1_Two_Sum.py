class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in range(0, len(nums)):
            temp = 0
            for n in range(num+1, len(nums)):
                temp = nums[num] + nums[n]
                if ( temp == target):
                    first_index = nums.index(nums[num])
                    second_index = len(nums) - nums[::-1].index(nums[n]) - 1
                    return first_index,second_index