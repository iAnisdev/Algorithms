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


# incase array is sorted
def twoSumSorted(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    left = 0
    right = len(numbers) - 1

    while left < right:
        curr = numbers[left] + numbers[right]
        if curr == target:
            return [left + 1, right + 1]

        if curr > target:
            right = right - 1
        else:
            left = left + 1
    return []
