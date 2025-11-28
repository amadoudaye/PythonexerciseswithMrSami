def sum_even_numbers(lst):
    total = 0
    for num in lst:
        if num % 2 == 0:   # check if even
            total += num
    return total
print(sum_even_numbers([1, 2, 3, 4, 5, 6]))