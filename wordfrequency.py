def word_frequency(sentence):
    words = sentence.split()   # split into words
    freq = {}                  # empty dictionary

    for word in words:
        if word in freq:
            freq[word] += 1    # increase count
        else:
            freq[word] = 1     # first time seeing the word

    return freq
text = "apple banana apple orange banana apple"
print(word_frequency(text))