import random

def dice_simulation():
    results = {}  # store counts of sums

    for _ in range(100):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2

        if total in results:
            results[total] += 1
        else:
            results[total] = 1

    return results


print(dice_simulation())
