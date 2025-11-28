def second_largest(lst):
    largest = max(lst)
    second = None

    for num in lst:
        if num != largest:
            if second is None or num > second:
                second = num

    return second
print(second_largest([10, 20, 4, 45, 99]))