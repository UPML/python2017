def generate(words, word):
    if len(word) > 0:
        print(word)
    for i in range(len(words)):
        generate(words[:i] + words[i + 1:], word + words[i])


line = input()
words = line.split(" ")
words = sorted(words)

generate(words, "")
