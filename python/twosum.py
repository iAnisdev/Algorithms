from typing import List


def twoSum(nums: List[int], target: int):
    hash = {}
    for i in range(len(nums)):
        hash[nums[i]] = i
    for i in range(len(nums)):
        if target - nums[i] in hash:
            if hash[target - nums[i]] != i:
                return [i, hash[target - nums[i]]]
    return []
