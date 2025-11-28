def file_stats(filename):
    lines = 0
    words = 0
    characters = 0

    with open(filename, "r") as file:
        for line in file:
            lines += 1
            words += len(line.split())
            characters += len(line)

    return lines, words, characters
print(file_stats("example.txt"))