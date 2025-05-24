def KMP(haystack, needle):
    haystack_len = len(haystack)
    needle_len = len(needle)
    p = [0] * needle_len
    j = 0
    i = 1

    if needle_len == 0:
        return 0

    while i < needle_len:
        if needle[j] == needle[i]:
            p[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                p[i] = 0
                i += 1
            else:
                j = p[j-1]

    i = 0
    j = 0

    while i < haystack_len:
        if haystack[i] == needle[j]:
            i += 1
            j += 1    
            if j == needle_len:
                return i - needle_len
        else:
            if j > 0:
                j = p[j-1]
            else:
                i += 1
    if i == haystack_len:
        return None
