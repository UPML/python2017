alreadySeen = set()
twiceSeen = set()
uniqueElements = []

line = input()
for n in line.split(" "):
    if (n in alreadySeen):
        twiceSeen.add(n)
    alreadySeen.add(n)
    uniqueElements.append(n)

for i in uniqueElements:
    if i in alreadySeen.symmetric_difference(twiceSeen):
        print(i, end=" ")
