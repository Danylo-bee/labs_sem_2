def find_board_size(n, w, h):
    left = min(w, h)
    right= max(w, h) * n
    count = 1

    while left < right:
        count += 1
        mid = (right + left) // 2
        if (mid // w) * (mid // h) >= n:
            right = mid
        else:
            left = mid + 1

    return (left, count)

#test
print(find_board_size(1_000_000_000, 50, 90))
