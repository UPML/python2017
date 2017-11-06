import random


def british_word(word, param):
    if len(word) >= param + 2:
        last_to_change = min(param, len(word) - 2)
        positions = random.sample(range(1, len(word) - 1), last_to_change)
        characters = []
        for j in positions:
            characters.append(word[j])
        random.shuffle(characters)
        new_shuffle = list(word)
        for i, j in enumerate(positions):
            new_shuffle[j] = characters[i]
        shuffled_string = ''
        for s in new_shuffle:
            shuffled_string += s
        return shuffled_string
    else:
        return word


def prepare_to_british_scientists(text, param):
    shuffled_text = ''
    word = ''
    for c in text:
        if ord('a') <= ord(c) <= ord('z') or \
                ord('A') <= ord(c) <= ord('Z'):
            word += c
        else:
            shuffled_text += british_word(word, param)
            shuffled_text += c
            word = ''
    shuffled_text += british_word(word, param)
    return shuffled_text

# print(prepare_to_british_scientists("Namespaces are one honking great ", 2))