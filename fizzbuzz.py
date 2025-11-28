def advanced_fizzbuzz():
    for i in range(1, 101):
        result = ""

        if i % 3 == 0 or "3" in str(i):
            result += "Fizz"

        if i % 5 == 0 or "5" in str(i):
            result += "Buzz"

        if result == "":
            result = i

        print(result)

# -------------------------
# Run the program
# -------------------------

advanced_fizzbuzz()
