
with open('input.txt') as f:
    for line in f:
        s = line[::-1]
        ans = ""
        for i, c in enumerate(s):
            if c == "T":
                ans += "A"
            elif c == "A":
                ans += "T"
            elif c == "G":
                ans += "C"
            else:
                ans += "G"
        print(ans)
