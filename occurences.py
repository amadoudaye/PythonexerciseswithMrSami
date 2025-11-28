def censor_word(sentence, word):
    return sentence.replace(word, "***")

sentence = "Hello World, World is big"
word = "World"

result = censor_word(sentence, word)
print(result)