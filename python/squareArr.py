def square_Arr(nums):
    if len(nums) < 1 or len(nums) > 10**4:
        raise ValueError("Out of range")

    result = [i for i in range(len(nums))]
    left, right = 0, len(nums) - 1
    for pos in range(len(nums) - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[pos] = nums[left] ** 2
            left = left + 1
        else:
            result[pos] = nums[right] ** 2
            right = right - 1
    return result


print(square_Arr([-4, -1, 0, 3, 10]))  # [0,1,9,16,100]
print(square_Arr([-7, -3, 2, 3, 11]))  # [4,9,9,49,121]
