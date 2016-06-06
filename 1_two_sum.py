class Solution(object):
    def twoSum(self, nums, target):
        nums_dict = {}
        for i in range(len(nums)):
            if (target-nums[i]) in nums_dict:
                return [i, nums_dict[target-nums[i]]]
            nums_dict[nums[i]] = i
        return []