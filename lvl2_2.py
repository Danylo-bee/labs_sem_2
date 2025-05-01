def is_monoton (lst):
    ''' Перевіряє чи масив монотонний. '''

    if len(lst) <= 2:
        return True

    is_increasing = True
    for el in range(len(lst) - 1):
        if lst[el] > lst[el+1]:
            is_increasing = False
            break

    if is_increasing:
        return True

    is_decreasing = True
    for el in range(len(lst) - 1):
        if lst[el] < lst[el+1]:
            is_decreasing = False
            break
    return is_decreasing
