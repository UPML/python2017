def nextLetter(c, step):
    if not ord('A') <= ord(c) <= ord('Z') and \
            not ord('a') <= ord(c) <= ord('z'):
        return c

    nOfLetters = ord('z') - ord('a') + 1
    newLetter = ord(c)
    if ord('A') <= ord(c) <= ord('Z'):
        newLetter = newLetter - ord('A') + step
        newLetter = ((newLetter % nOfLetters) + nOfLetters) % nOfLetters
        newLetter += ord('A')
    else:
        newLetter = newLetter - ord('a') + step
        newLetter = ((newLetter % nOfLetters) + nOfLetters) % nOfLetters
        newLetter += ord('a')
    return chr(newLetter)


step = int(input())
line = input()
newLine = ""

for i in range(len(line)):
    newLine += nextLetter(line[i], step)

print(newLine)
