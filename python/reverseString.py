def reverse_array(s):
    if 1 > len(s) or len(s) >= 10**5:
        raise ValueError("Value out of range")
    left = 0
    right = len(s) - 1
    while left < right:
        s[right] , s[left] = s[left] , s[right]
        left = left + 1
        right = right - 1

    return s


print(reverse_array(["h", "e", "l", "l", "o"]))
print(reverse_array(["H","a","n","n","a","h"]))