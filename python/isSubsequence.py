def isSubsequence( s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    s_index = 0
    t_index = 0
    while s_index < len(s) and t_index < len(t):
        if s[s_index] == t[t_index]:
            s_index = s_index + 1
        t_index = t_index + 1

    return len(s) == s_index

print(isSubsequence("abc", "ahbgdc"))
print(isSubsequence("axc", "ahbgdc"))