def fibonacci(n):
    sequence = [0, 1]

    if n <= 0:
        return []
    elif n == 1:
        return [0]

    # Generate numbers starting from index 2 up to n
    for i in range(2, n):
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)

    return sequence


print(fibonacci(7))