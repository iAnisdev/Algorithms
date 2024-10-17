from math import floor

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    sorted_arr = sorted(nums1 + nums2)
    if len(sorted_arr) % 2 == 0:
        median = sorted_arr[floor(len(sorted_arr) / 2)] + sorted_arr[(floor(len(sorted_arr) / 2) - 1)]
        return float(median / 2)
    else:
        median = sorted_arr[floor(len(sorted_arr) / 2)]
        return float(median)
