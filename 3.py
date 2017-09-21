ns = [[]] * 3

ns[0] = [1] * 100
ns[1] = [0] * 100
ns[2] = [0] * 100

for i in range(5, 100, 5):
    ns[1][i] = ns[1][i - 5] + 1

for i in range(10, 100, 5):
    ns[2][i] = ns[2][i - 10] + ns[1][i - 10] + ns[0][i - 10]

n = int(input())
print(ns[0][n] + ns[1][n - n % 5] + ns[2][n - n % 5])
